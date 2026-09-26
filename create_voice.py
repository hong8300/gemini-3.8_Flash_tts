"""Create a custom voice for Gemini 3.8 Flash TTS and register it by name in myvoice/voices.json.

Voice Replication (default): from recordings in myvoice/.
Voice Design (--design): from a text description of the voice.

Recordings: myvoice/<name>_approved.wav (consent) and one other myvoice/<name>_*.wav (reference).
Files that are not 24 kHz mono 16-bit are converted to <stem>_24k.wav with macOS afconvert.
"""

import argparse
import base64
import json
import subprocess
import sys
import wave
from pathlib import Path

from google import genai

from tts_test import MODEL, VOICE_DIR, VOICE_REGISTRY, load_api_key, load_registry


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def is_24k(path: Path) -> bool:
    try:
        with wave.open(str(path)) as wf:
            return (wf.getframerate(), wf.getnchannels(), wf.getsampwidth()) == (24000, 1, 2)
    except (wave.Error, EOFError):
        return False


def to_24k(path: Path) -> Path:
    if is_24k(path):
        return path
    out = path.with_name(f"{path.stem}_24k.wav")
    if not out.is_file() or out.stat().st_mtime < path.stat().st_mtime:
        subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16@24000", "-c", "1", "--mix", str(path), str(out)], check=True)
        print(f"converted {path.name} -> {out.name}")
    return out


def find_recordings(name: str, source: Path | None, consent: Path | None) -> tuple[Path, Path]:
    consent = consent or VOICE_DIR / f"{name}_approved.wav"
    if source is None:
        candidates = sorted(p for p in VOICE_DIR.glob(f"{name}_*.wav") if p != consent and not p.stem.endswith("_24k"))
        if len(candidates) != 1:
            found = ", ".join(p.name for p in candidates) or "none"
            raise SystemExit(f"need exactly one reference recording myvoice/{name}_*.wav (found: {found}); use --source")
        source = candidates[0]
    missing = [p for p in (source, consent) if not p.is_file()]
    if missing:
        raise SystemExit("not found: " + ", ".join(map(str, missing)))
    return to_24k(source), to_24k(consent)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("name", help="speaker name, e.g. hong")
    parser.add_argument("--source", type=Path, help="reference audio (default: the one myvoice/<name>_*.wav)")
    parser.add_argument("--consent", type=Path, help="consent audio (default: myvoice/<name>_approved.wav)")
    parser.add_argument("--design", metavar="PROMPT", help="Voice Design: create the voice from this description instead of recordings")
    parser.add_argument("--gender", help='Voice Design only, e.g. "female"')
    parser.add_argument("--language", default="ja-JP", help="Voice Design only (default: ja-JP)")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--replace", action="store_true", help="replace the voice already registered for <name>")
    args = parser.parse_args()

    registry = load_registry()
    old = registry.get(args.name)
    if old and not args.replace:
        print(f"{args.name} is already registered ({old['id']}); use --replace to recreate", file=sys.stderr)
        return 1

    if args.design:
        spec = {"type": "prompted", "language_code": args.language, "prompted": {"input": args.design}}
        if args.gender:
            spec["gender"] = args.gender
        info = {"design": args.design}
    else:
        source, consent = find_recordings(args.name, args.source, args.consent)
        spec = {
            "type": "replicated",
            "replicated": {
                "source_audio": {"mime_type": "audio/wav", "data": b64(source)},
                "consent_audio": {"mime_type": "audio/wav", "data": b64(consent)},
            },
        }
        info = {"source": source.name, "consent": consent.name}

    api_key = load_api_key()
    if api_key is None:
        print("GEMINI_API_KEY is not set in .env", file=sys.stderr)
        return 1

    client = genai.Client(api_key=api_key, enterprise=False)
    try:
        voice = client.voices.create(store=True, voice={"model": args.model, "display_name": args.name, **spec})
    except Exception as e:
        print(f"voice creation failed: {e}", file=sys.stderr)
        return 1

    registry[args.name] = {
        "id": voice.id,
        "model": args.model,
        **info,
        "expire_time": voice.expire_time.isoformat() if voice.expire_time else None,
    }
    VOICE_REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n")
    print(f"created {args.name}: {voice.id} (expires {registry[args.name]['expire_time']})")
    if voice.sample_audio:
        sample = Path(f"output/{args.name}_sample.wav")
        sample.parent.mkdir(parents=True, exist_ok=True)
        sample.write_bytes(base64.b64decode(voice.sample_audio.data))
        print(f"sample: {sample}")
    if voice.usage:
        print(f"tokens: in {voice.usage.total_input_tokens}, out {voice.usage.total_output_tokens}")

    # Delete the old voice only after the new one exists, so a failed re-creation keeps it.
    if old:
        client.voices.delete(id=old["id"])
        print(f"deleted old voice {old['id']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
