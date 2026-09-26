# gemini-3.8_Flash_tts

Gemini 3.8 Flash TTS（`gemini-3.8-flash-tts`）でテキストを読み上げ、WAV に保存するテストスクリプト。自分の声を録音して、その声で読み上げさせることもできる（[自分の声を作る](#自分の声を作るvoice-replication)）。Gemini API を API キーだけで呼ぶ（Google Cloud 側の設定は不要）。

## セットアップ

```bash
uv sync
cp .env.example .env   # GEMINI_API_KEY= に API キーを書く
```

必要なもの:
- Python 3.11+ / [uv](https://docs.astral.sh/uv/)
- `google-genai` 2.25.0+（`speech_metadata` と `VoiceConfig.voice` に必要）、`python-dotenv`
- Gemini API キー（[Google AI Studio](https://aistudio.google.com/apikey) で発行。課金の設定が必要。下の「料金」を参照）

キーはこのディレクトリの `.env` からだけ読む（`#` のコメント行は可）。シェルの `GOOGLE_API_KEY` や `GOOGLE_GENAI_USE_VERTEXAI` などは無視される。`.env` は git に含めない。

## 使い方

```bash
uv run python tts_test.py
uv run python tts_test.py --text "今日はいい天気ですね。" --voice Kore --style "cheerful and friendly" -o output/hello.wav
afplay output/hello.wav
```

| オプション | 内容 | 既定値 |
|---|---|---|
| `--text` | 読み上げる文章（下記のタグも書ける） | `こんにちは、私はgemini 3.8 TTS です。` |
| `--voice` | 声の名前・ID、または `create_voice.py` で登録した名前（`hong` など） | `Kore` |
| `--style` | 話し方の指示（英語の短い文） | なし |
| `-o`, `--out` | 出力ファイル（フォルダがなければ作る） | 登録した名前なら `output/<名前>_<日時>.wav`、それ以外は `output/out.wav` |
| `--model` | モデル名 | `gemini-3.8-flash-tts` |

出力は WAV（24 kHz / モノラル / 16 bit）。`output/` は git に含めない。言語は自動判定で、日本語に対応している。

## `--voice` に指定できるもの

### 1. 標準の 30 声（言語共通）

| 名前 | 特徴 | 名前 | 特徴 | 名前 | 特徴 |
|---|---|---|---|---|---|
| Zephyr | Bright | Puck | Upbeat | Charon | Informative |
| Kore | Firm | Fenrir | Excitable | Leda | Youthful |
| Orus | Firm | Aoede | Breezy | Callirrhoe | Easy-going |
| Autonoe | Bright | Enceladus | Breathy | Iapetus | Clear |
| Umbriel | Easy-going | Algieba | Smooth | Despina | Smooth |
| Erinome | Clear | Algenib | Gravelly | Rasalgethi | Informative |
| Laomedeia | Upbeat | Achernar | Soft | Alnilam | Firm |
| Schedar | Even | Gacrux | Mature | Pulcherrima | Forward |
| Achird | Friendly | Zubenelgenubi | Casual | Vindemiatrix | Gentle |
| Sadachbia | Lively | Sadaltager | Knowledgeable | Sulafat | Warm |

### 2. Extended Voice Library（言語別の声）

`ja-jp-podcaster-3` のような ID を `--voice` に渡す。2026-09-26 時点で日本語（`ja-JP`）は 115 声あり、アクセントは東京 73、大阪 22、福岡 20 の内訳。

全 115 声の一覧（性別・ピッチ・アクセント・説明つき）は [voices-ja-JP.md](voices-ja-JP.md)。用途は接頭辞からの目安。

| ID の接頭辞 | 用途 | 数 |
|---|---|---|
| `ja-jp-advisor-N` | 医師・弁護士・研究者などの落ち着いた説明役 | 12 |
| `ja-jp-assistant-N` | 友人・家族のようなアシスタント | 12 |
| `ja-jp-commercial-N` | CM ナレーション | 7 |
| `ja-jp-concierge-N` | コンシェルジュ・秘書 | 12 |
| `ja-jp-csagent-N` | コールセンター | 12 |
| `ja-jp-podcaster-N` | ポッドキャスト・ニュース | 12 |
| `ja-jp-storyteller-N` | 朗読・ナレーション | 12 |
| `ja-jp-techagent-N` | 技術サポート | 12 |
| `ja-jp-training-N` | 研修・解説動画 | 12 |
| `ja-jp-tutor-N` | 家庭教師 | 12 |

ID の一覧はドキュメントのページには載っていない（上の数と内訳は `voices.list` API の結果から集計したもの）。一覧を見る方法は次の 2 つ:
- AI Studio で見て試聴する: https://aistudio.google.com/generate-speech
- API で取得する（下のコマンド。`gender` / `pitch` / `search` などで絞り込める。フィルタの説明は https://ai.google.dev/gemini-api/docs/speech-generation#voice-library ）

```bash
uv run python -c '
from dotenv import dotenv_values; from google import genai
c = genai.Client(api_key=dotenv_values(".env")["GEMINI_API_KEY"], enterprise=False)
for v in c.voices.list(language_code=["ja-JP"], page_size=200).voices:
    print(v.id, v.gender, v.pitch, v.accent, v.description, sep=" | ")
'
```

### 3. 自分で作った声

`create_voice.py` で作って登録した名前（`hong` など）を `--voice` に渡す。作り方は次の節。Voice Design や Voice Replication で作った `voice_...` / `voicekey_...` の ID を直接渡してもよい。

## 自分の声を作る（Voice Replication）

自分の声を 2 本録音して API に送ると、自分の声の voice ID（`voice_...`）が発行される。`create_voice.py` はこの ID を名前（例: `hong`）と対応づけて `myvoice/voices.json` に保存するので、以後は `--voice hong` で読み上げられる。

### 1. 録音する

録音ソフトは何でもよい。Mac なら Audacity を Homebrew で入れると、ほかのアプリ（MuseHub）が付いてこない。

```bash
brew install --cask audacity
```

本人（成人）が、同じマイク・同じ部屋で、静かで反響の少ない場所で次の 2 本を録る。

| 内容 | 長さ | ファイル名 |
|---|---|---|
| 参照音声: 普段どおりの自然な話し声（内容は何でもよい） | 10〜30 秒 | `myvoice/<名前>_<何でも>.wav`（例: `hong_30sec.wav`） |
| 同意音声: 下の同意文を一字一句そのまま読む | 数秒 | `myvoice/<名前>_approved.wav`（例: `hong_approved.wav`） |

日本語の同意文:

> 私はこの音声の所有者であり、Googleがこの音声を使用して音声合成モデルを作成することを承認します。

- 書き出しは WAV（モノラル・16 bit）。サンプリングレートは 44100 Hz などのままでよい。`create_voice.py` が macOS の `afconvert` で 24 kHz に変換し、`<元の名前>_24k.wav` を作る
- 参照音声として使えるのは、`myvoice/<名前>_*.wav` のうち、`_approved.wav` と `_24k.wav` 以外の 1 本だけ。2 本以上あるときは `--source` で指定する
- 音割れ（入力レベルの上げすぎ）とノイズ除去などの加工は避ける

### 2. 声を作る

```bash
uv run python create_voice.py hong
```

```
created hong: voice_xxxxxxxxxxxx (expires 2027-09-26T03:32:17+00:00)
```

| オプション | 内容 |
|---|---|
| `名前` | 登録する名前（`myvoice/<名前>_*.wav` を探す） |
| `--source` | 参照音声を指定する |
| `--consent` | 同意音声を指定する |
| `--replace` | 登録済みの名前で作り直す（新しい声ができてから古い声を削除する） |
| `--design "説明"` | 録音の代わりに、声の説明文から作る（Voice Design、下記） |
| `--gender` | Voice Design のときの性別（`female` / `male`） |
| `--language` | Voice Design のときの言語（既定は `ja-JP`） |
| `--model` | モデル名（既定は `gemini-3.8-flash-tts`） |

### 3. 読み上げる

```bash
uv run python tts_test.py --voice hong --text "これは私の声のテストです。"
afplay output/hong_20260926-123222.wav   # 表示されたファイル名で再生する
```

`--style` やタグも標準の声と同じように使える。

### 声の一覧と削除

```bash
cat myvoice/voices.json   # 名前と voice ID の対応
uv run python -c '
from dotenv import dotenv_values; from google import genai
c = genai.Client(api_key=dotenv_values(".env")["GEMINI_API_KEY"], enterprise=False)
for v in c.voices.list(type_=["replicated", "prompted"]).voices:
    print(v.id, v.type, v.display_name, v.expire_time, sep=" | ")
'
```

削除は `c.voices.delete(id="voice_...")`。削除したら `myvoice/voices.json` からもその名前を消す。

### 声の説明文から作る（Voice Design）

録音の代わりに、英語の 1〜2 文で声を説明して作ることもできる。架空のキャラクター向け。できた声の試聴用音声が `output/<名前>_sample.wav` に保存される。

```bash
uv run python create_voice.py narrator --gender female \
  --design "A calm Japanese woman in her 30s with a clear, warm voice and standard Tokyo accent, speaking at a relaxed pace."
uv run python tts_test.py --voice narrator --text "こんにちは。"
```

作るたびに違う声になり、特定の声に似せるのは難しい。一度作った声は、同じ ID なら何度読み上げても同じ声になる。

### 注意

- **本人の生の声だけが使える。** AI で作った声（ほかの TTS の出力など）を渡すと、次のエラーで拒否される。SDK は 500 エラーとして表示するが、中身は入力の拒否
  ```
  Voice replication failed safety checks.
  Reference or consent audio contains synthetic speech or AI provenance watermarks (SynthID/C2PA).
  ```
- 同意音声の話者が参照音声と違う場合や、同意文が違う場合も拒否される
- 作った声は 1 年で期限切れになる。1 プロジェクトにつき最大 200 声（Voice Design の声と合わせて）
- 声を作る料金はドキュメントに載っていない。Voice Design で試したときは、1 回あたり音声出力 400〜1,300 トークン（出力料金で換算して 2 円以下）だった
- 生成した音声には SynthID の透かしが入る
- `myvoice/`（録音と `voices.json`）は git に含めない。自分の声と同意音声は悪用されうるので、公開しない
- AI Studio の画面から声を作る機能は、イリノイ州・テキサス州・EEA・英国・スイス・インドでは使えない

## `--style` と `--text` 内のタグ

### 使い分け

| | 効く範囲 | 書く場所 | 例 |
|---|---|---|---|
| `--style` | 発話全体に続く話し方（感情・速さ・トーン） | `--style "..."`（英語の短文） | `"angry tone"`, `"speaking rapidly"`, `"whispering"` |
| タグ | 書いた位置で一瞬だけ起きる声や間 | `--text` の中に `<...>` | `<cough>`, `<sigh>`, `<short pause>` |

### `--style` の例

- 感情・トーン: `"cheerful and friendly"`, `"casual, friendly"`, `"angry tone"`, `"sarcastic"`, `"monotone and flat"`
- 話し方: `"whispering"`, `"muttering"`, `"out of breath"`, `"muttering, then reassuring"`
- 速さ: `"speaking rapidly"`, `"speaking slowly"`
- 声の高さ・抑揚: `"high pitch, cheerful and excited inflection"`

年齢・性別・アクセントのような話者そのものの特徴は `--style` に書かず、声（`--voice`）の選択で決める（ドキュメントの推奨）。

### タグ一覧

日本語の文章でもタグは英語のまま書く。出るのは人の声だけで、足音やドアのような効果音は出ない。下の「意味」と「使いどころ」は英単語からの目安で、ドキュメントに日本語の説明はない。効き方は声や文脈で変わるので、試しながら調整する。

**呼吸・ため息**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<breath>` | 息を吸う音 | 話し始める前、長い文の区切り | `<breath> それでは始めます。` |
| `<heavy breath>` | 荒い・深い呼吸 | 走った後、緊張、疲れ | `<heavy breath> やっと着いた…` |
| `<exhales>` | 息を吐く（ふうっ） | ほっとした、気持ちを落ち着ける | `<exhales> よし、落ち着こう。` |
| `<sigh>` / `<sighs>` | ため息（はあ） | 疲れ、がっかり、呆れ | `今日も残業か… <sigh>` |
| `<pant>` | ハアハアと息を切らす | 運動や全力疾走の直後 | `<pant> ちょ、ちょっと待って…` |
| `<yawn>` | あくび | 眠い、退屈 | `<yawn> もうこんな時間か。` |
| `<pff>` / `<phew>` | ふうっ・ぷはっと息を吹き出す | 安堵（phew）、呆れ（pff） | `<phew> 間に合った。` |

**笑い**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<laugh>` / `<laughter>` | 声を出して笑う（はは） | 面白い話、冗談 | `それ本当？<laugh> 最高だね。` |
| `<chuckle>` / `<chuckles>` | くすっと笑う、含み笑い（ふふ） | 軽い面白さ、苦笑、余裕 | `<chuckle> まあ、そういうこともあるよね。` |
| `<giggle>` | くすくす笑う | 照れ、はしゃぎ | `<giggle> 内緒だよ。` |
| `<cackle>` | 甲高い高笑い（悪役・魔女風） | 悪役、意地悪なキャラ | `<cackle> これで私の勝ちだ！` |
| `<snicker>` | 人を小ばかにした忍び笑い | からかい、嘲笑 | `<snicker> また転んでる。` |
| `<snort>` | 鼻を鳴らす（ふんっ）、思わず吹き出す | 軽蔑、笑いをこらえきれない | `<snort> そんなの信じるわけないでしょ。` |

**驚き・叫び・喜び**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<gasp>` | はっと息をのむ | 驚き、ショック | `<gasp> 財布がない！` |
| `<scream>` | 悲鳴（きゃー） | 恐怖、パニック | `<scream> 誰かいる！` |
| `<shriek>` | 金切り声（scream より高く鋭い） | 驚き、恐怖、興奮 | `<shriek> 虫がいる！` |
| `<shout>` | 叫び声・大声 | 遠くの人を呼ぶ、怒鳴る | `<shout> おーい、こっちだ！` |
| `<cheer>` | 歓声（やったー） | 喜び、応援 | `<cheer> 合格した！` |

**泣き**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<cry>` | 泣き声 | 悲しみ、感極まる | `<cry> ずっと会いたかった…` |
| `<sob>` | しゃくり上げて泣く（嗚咽） | 激しい悲しみ | `<sob> もう無理だよ…` |
| `<whimper>` | 弱々しいすすり泣き | 怯え、痛み、心細さ | `<whimper> 痛いよ…` |

**苛立ち・うめき・うなり**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<argh>` | ああもう！という叫び | 苛立ち、悔しさ | `<argh> また失敗した！` |
| `<groan>` | うめき声（うう…） | 痛み、うんざり | `<groan> また月曜日か…` |
| `<moan>` | 低く長いうめき（うーん…） | 痛み、不満、だるさ | `<moan> 頭が痛い…` |
| `<grunt>` | 短いうなり（ふんっ、うっ） | 力む、そっけない返事 | `<grunt> この箱、重すぎる。` |
| `<growl>` | 低くうなる | 怒り、威嚇 | `<growl> 二度とするな。` |
| `<grr>` | ぐぬぬ（ややコミカルなうなり） | 悔しさ、軽い怒り | `<grr> 次は負けないからな。` |
| `<hiss>` | 歯の間から出す鋭い息の音（シーッ、スーッ） | 威嚇、痛みをこらえる、静かにさせる | `<hiss> 熱っ！` |
| `<tsk>` | 舌打ち（ちっ） | 不満、呆れ | `<tsk> また遅刻か。` |

**体の音**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<cough>` | 咳（ごほっ） | 風邪、むせる | `<cough> すみません、風邪気味で。` |
| `<sneeze>` | くしゃみ | 花粉症、寒い | `<sneeze> 花粉がひどい。` |
| `<throat-clearing>` | 咳払い（んんっ） | 話を切り出す、注意を引く、気まずさ | `<throat-clearing> えー、本日はお集まりいただき…` |

**ささやき・間**

| タグ | 意味 | 使いどころ | 例 |
|---|---|---|---|
| `<whispers>` / `<whispering>` | ささやく | 一部だけ小声にする（全体なら `--style "whispering"`） | `実はね <whispers> 明日サプライズなんだ。` |
| `<short pause>` | 短い間 | 考える、区切りを入れる | `えっと <short pause> 少し待ってください。` |
| `<long pause>` | 長い間 | 沈黙、溜め | `答えは <long pause> 42 です。` |

### その他のコツ

- 読点や「…」でも、自然なためらいや間が出る（ドキュメントでは `,` `--` `...` が挙げられている）
- 大文字にした単語は強調される（例: `This is VERY important`）。日本語には大文字がないので、英単語にだけ使える
- 言いよどみを含めて、実際に話すとおりに書くと自然になる（例: `えっと、あの…そうですね`）

```bash
uv run python tts_test.py --text "えっと <short pause> それは <laugh> 知らなかったです。" --style "surprised, then amused"
```

## 料金

2026-09-26 時点の [料金ページ](https://ai.google.dev/gemini-api/docs/pricing) の有料（Paid Tier）価格。100 万トークンあたりの USD。料金はほぼ出力音声の長さで決まり、入力テキストの分はごくわずか。

| モデル | 入力（テキスト） | 出力（音声） | 音声 1 分 | 音声 1 時間 |
|---|---|---|---|---|
| **3.8 Flash TTS**（このスクリプト、〜2026-12-31） | $0.50 | $9.00 | $0.0135 | $0.81 |
| 3.8 Flash TTS（2027-01-01〜） | $1.00 | $18.00 | $0.027 | $1.62 |
| 3.8 Flash-Lite TTS（〜2026-12-31） | $0.50 | $6.00 | $0.009 | $0.54 |
| 3.8 Flash-Lite TTS（2027-01-01〜） | $1.00 | $12.00 | $0.018 | $1.08 |
| 3.1 Flash TTS Preview | $1.00 | $20.00 | $0.03 | $1.80 |
| 2.5 Flash Preview TTS | $0.50 | $10.00 | $0.015 | $0.90 |
| 2.5 Pro Preview TTS | $1.00 | $20.00 | $0.03 | $1.80 |

- 「音声 1 分」「音声 1 時間」は、出力料金を音声 1 秒 = 25 トークンで換算した値（3.8 系はページの「10 秒あたり」の記載と一致）
- 既定の文（数秒の音声）なら 1 回 $0.001 未満。前払いの最低額 $10 で、今の料金なら約 740 分の音声を生成できる
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api) 経由だと半額。ただし結果はすぐには返らず、最長 24 時間後に受け取る（このスクリプトは通常の即時リクエストなので半額にはならない）
- 課金を設定していないプロジェクトには無料枠があり、3.8 Flash TTS も無料で使える。ただし送ったデータが製品改善に使われる。課金を設定したプロジェクトでは有料価格になる

## ドキュメント

- TTS 全般: https://ai.google.dev/gemini-api/docs/speech-generation
  - 声の一覧・Extended Voice Library: https://ai.google.dev/gemini-api/docs/speech-generation#voices
  - style とタグの制御: https://ai.google.dev/gemini-api/docs/speech-generation#controllable
  - プロンプトの書き方: https://ai.google.dev/gemini-api/docs/speech-generation#prompting-guide
  - 対応言語: https://ai.google.dev/gemini-api/docs/speech-generation#languages
- Voice Replication（自分の声を作る）: https://ai.google.dev/gemini-api/docs/voice-replication
- Voice Design（説明文から声を作る）: https://ai.google.dev/gemini-api/docs/voice-design
- 課金（前払い / 後払い）: https://ai.google.dev/gemini-api/docs/billing
- 料金: https://ai.google.dev/gemini-api/docs/pricing
- Batch API: https://ai.google.dev/gemini-api/docs/batch-api

## 注意（2026-09 時点）

- `gemini-3.8-flash-tts` は Gemini API でだけ使える。Gemini Enterprise Agent Platform（旧 Vertex AI）では見つからない（NOT_FOUND）
- 新規の利用者は前払い（Prepay）が基本。残高が 0 になると、その請求先アカウントにつながる全プロジェクトのキーが 402 エラーで止まる
- Google Cloud の Welcome クレジットや無料トライアルのクレジットは Gemini API には使えない

## ファイル

- `tts_test.py`: 読み上げスクリプト本体
- `create_voice.py`: 自分の声（Voice Replication）や説明文からの声（Voice Design）を作り、名前で登録する
- `myvoice/`: 録音と `voices.json`（名前と voice ID の対応）を置く。中身は git に含めない
- `voices-ja-JP.md`: 日本語の声 115 個の一覧
- `.env.example`: `.env` のひな形
