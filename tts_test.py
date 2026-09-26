"""Generate a WAV file with Gemini 3.8 Flash TTS (Gemini API)."""

import argparse
import json
import sys
import wave
from datetime import datetime
from pathlib import Path

from dotenv import dotenv_values
from google import genai

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
# Speaker name -> replicated voice ID, written by create_voice.py.
VOICE_DIR = ROOT / "myvoice"
VOICE_REGISTRY = VOICE_DIR / "voices.json"
MODEL = "gemini-3.8-flash-tts"
DEFAULT_TEXT = "こんにちは、私はgemini 3.8 TTS です。"

# Used only if the API returns headerless PCM instead of WAV (24 kHz, mono, 16-bit).
SAMPLE_RATE = 24000
CHANNELS = 1
SAMPLE_WIDTH = 2


def save_wav(data: bytes, path: Path) -> None:
    if data[:4] == b"RIFF":
        path.write_bytes(data)
        return
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(data)


def load_api_key() -> str | None:
    # Read only from this directory's .env so shell variables (GOOGLE_API_KEY etc.) can't override it.
    return (dotenv_values(ENV_FILE).get("GEMINI_API_KEY") or "").strip() or None


def load_registry() -> dict:
    return json.loads(VOICE_REGISTRY.read_text()) if VOICE_REGISTRY.is_file() else {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default=DEFAULT_TEXT)
    parser.add_argument("--voice", default="Kore", help="voice name/ID, or a speaker name registered by create_voice.py")
    parser.add_argument("--style", help='delivery direction, e.g. "cheerful and friendly"')
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("-o", "--out", type=Path, help="default: output/<speaker>_<time>.wav for registered speakers, else output/out.wav")
    args = parser.parse_args()

    registry = load_registry()
    speaker = args.voice if args.voice in registry else None
    voice_id = registry[speaker]["id"] if speaker else args.voice
    if args.out is None:
        args.out = Path(f"output/{speaker}_{datetime.now():%Y%m%d-%H%M%S}.wav" if speaker else "output/out.wav")

    part = {"text": args.text}
    if args.style:
        part["speech_metadata"] = {"style": args.style}

    api_key = load_api_key()
    if api_key is None:
        print(f"GEMINI_API_KEY is not set in {ENV_FILE}", file=sys.stderr)
        return 1

    # Gemini API only: enterprise=False ignores GOOGLE_GENAI_USE_* / GOOGLE_CLOUD_PROJECT.
    client = genai.Client(api_key=api_key, enterprise=False)
    response = client.models.generate_content(
        model=args.model,
        contents=[{"role": "user", "parts": [part]}],
        config={
            "response_modalities": ["AUDIO"],
            "speech_config": {"voice_config": {"voice": voice_id}},
        },
    )

    try:
        inline = response.candidates[0].content.parts[0].inline_data
    except (IndexError, TypeError, AttributeError):
        inline = None
    if inline is None or not inline.data:
        print(f"no audio in response:\n{response}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    save_wav(inline.data, args.out)
    with wave.open(str(args.out), "rb") as wf:
        duration = wf.getnframes() / wf.getframerate()
        fmt = f"{wf.getframerate()} Hz, {wf.getnchannels()} ch, {wf.getsampwidth() * 8} bit"
    print(f"saved {args.out}: {duration:.2f}s, {fmt} (mime={inline.mime_type}, voice={args.voice}{f' = {voice_id}' if speaker else ''})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
