# 日本語の声一覧（Extended Voice Library, ja-JP）

`client.voices.list(language_code=["ja-JP"])` の結果（2026-09-26 取得、全 115 声）。ID をそのまま `tts_test.py --voice` に渡す。説明文は API が返した英語のまま。

- アクセント: 東京 73 / 大阪 22 / 福岡 20
- 性別: 女性 61 / 男性 51 / 中性 3
- 試聴: https://aistudio.google.com/generate-speech

```bash
uv run python tts_test.py --voice ja-jp-podcaster-3 --text "こんにちは。"
```

## 目次

見出しの用途は ID の接頭辞から付けた目安。実際のペルソナは各行の「ペルソナ」列を見る（接頭辞と違うものもある）。

- [advisor](#advisor) — 医師・弁護士・研究者などの説明役（12）
- [assistant](#assistant) — 友人・家族のようなアシスタント（12）
- [commercial](#commercial) — CM ナレーション（7）
- [concierge](#concierge) — コンシェルジュ・秘書（12）
- [csagent](#csagent) — コールセンター（12）
- [podcaster](#podcaster) — ポッドキャスト・ニュース（12）
- [storyteller](#storyteller) — 朗読・ナレーション（12）
- [techagent](#techagent) — 技術サポート（12）
- [training](#training) — 研修・解説動画（12）
- [tutor](#tutor) — 家庭教師（12）

## advisor

医師・弁護士・研究者などの説明役

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-advisor-1` | 男性 | 低 | 大阪 | High-Trust Advisor / Authoritative Advisor (Doctor) | 44-year-old Doctor from Osaka. Speaks Osaka Japanese. Tone is objective, direct, and helpful |
| `ja-jp-advisor-2` | 女性 | 低 | 東京 | High-Trust Advisor / Authoritative Advisor (Doctor) | 37-year-old Doctor from Tokyo. Speaks Tokyo Japanese. Currently sitting next to you on the bus. Sounds confident and clear. |
| `ja-jp-advisor-3` | 男性 | 低 | 東京 | High-Trust Advisor / Authoritative Advisor (Lawyer) | 40-year-old Lawyer from Tokyo. Speaks Tokyo Japanese. Currently on podcast. Sounds confident and clear. |
| `ja-jp-advisor-4` | 女性 | 中 | 大阪 | High-Trust Advisor / Authoritative Advisor (Lawyer) | 41-year-old Lawyer from Osaka. Speaks Osaka Japanese. Currently on npr. Voice is warm and engaging. |
| `ja-jp-advisor-5` | 女性 | 高 | 東京 | High-Trust Advisor / Authoritative Advisor (Researcher) | 25-year-old Researcher from Tokyo. Speaks Tokyo Japanese. Currently brainstorming in a meeting. Sounds confident and clear. |
| `ja-jp-advisor-6` | 男性 | 低 | 大阪 | High-Trust Advisor / Authoritative Advisor (Lawyer) | 42-year-old Lawyer from Osaka. Speaks Osaka Japanese. Voice is relaxed. |
| `ja-jp-advisor-7` | 女性 | 高 | 東京 | High-Trust Advisor / Authoritative Advisor (Lawyer) | 39-year-old Lawyer from Tokyo. Speaks Tokyo Japanese. Tone is objective, direct, and helpful |
| `ja-jp-advisor-8` | 男性 | 低 | 東京 | High-Trust Advisor / Authoritative Advisor (Lawyer) | 39-year-old Lawyer from Tokyo. Speaks Tokyo Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-advisor-9` | 男性 | 低 | 福岡 | High-Trust Advisor / Authoritative Advisor (Researcher) | 58-year-old Researcher from Fukuoka. Speaks Fukuoka Japanese. Voice is textured, resonant, and soothing. |
| `ja-jp-advisor-10` | 男性 | 低 | 東京 | High-Trust Advisor / Authoritative Advisor (Financial Advisor) | 32-year-old Financial Advisor from Tokyo. Speaks Tokyo Japanese. Currently on podcast. Voice is warm and engaging. |
| `ja-jp-advisor-11` | 女性 | 高 | 東京 | High-Trust Advisor / Authoritative Advisor (Researcher) | 62-year-old Researcher from Tokyo. Speaks Tokyo Japanese. Voice is cool, confident, and collaborative. |
| `ja-jp-advisor-12` | 女性 | 高 | 東京 | High-Trust Advisor / Authoritative Advisor (Doctor) | 50-year-old Doctor from Tokyo. Speaks Tokyo Japanese. Voice is natural and clear. |

## assistant

友人・家族のようなアシスタント

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-assistant-1` | 女性 | 高 | 東京 | Companion & Peer / Digital Assistant (Parent) | 36-year-old Parent from Tokyo. Speaks Tokyo Japanese. Voice is textured, resonant, and soothing. |
| `ja-jp-assistant-2` | 男性 | 低 | 大阪 | Companion & Peer / Digital Assistant (Parent) | 38-year-old Parent from Osaka. Speaks Osaka Japanese. Currently on podcast. Sounds confident and clear. |
| `ja-jp-assistant-3` | 男性 | 低 | 福岡 | Companion & Peer / Digital Assistant (Friend) | 30-year-old Friend from Fukuoka. Speaks Fukuoka Japanese. Currently sitting on couch. Tone is professional yet approachable. |
| `ja-jp-assistant-4` | 女性 | 中 | 東京 | Companion & Peer / Digital Assistant (Best Friend) | 22-year-old Best Friend from Tokyo. Speaks Tokyo Japanese. Currently sitting on couch. Sounds confident and clear. |
| `ja-jp-assistant-5` | 女性 | 低 | 大阪 | Companion & Peer / Digital Assistant (Friend) | 30-year-old Friend from Osaka. Speaks Osaka Japanese. Currently in an indie film. Tone is professional yet approachable. |
| `ja-jp-assistant-6` | 女性 | 中 | 東京 | Tech Support Agent / Tech Advisor (Grandparent) | 74-year-old Grandparent from Tokyo. Speaks Tokyo Japanese. Currently on podcast. Tone is professional yet approachable. |
| `ja-jp-assistant-7` | 女性 | 高 | 東京 | Companion & Peer / Digital Assistant (Friend) | 31-year-old Friend from Tokyo. Speaks Tokyo Japanese. Voice is bright, breezy, and youthful. |
| `ja-jp-assistant-8` | 女性 | 高 | 大阪 | Companion & Peer / Digital Assistant (Sibling) | 24-year-old Sibling from Osaka. Speaks Osaka Japanese. Voice is laid-back, encouraging, and chill. |
| `ja-jp-assistant-9` | 中性 | 高 | 東京 | Companion & Peer / Digital Assistant (Friend) | 29-year-old Friend from Tokyo. Speaks Tokyo Japanese. Voice is resonant and witty. |
| `ja-jp-assistant-10` | 男性 | 中 | 福岡 | Companion & Peer / Digital Assistant (Friend) | 28-year-old Friend from Fukuoka. Speaks Fukuoka Japanese. Voice is bright, breezy, and youthful. |
| `ja-jp-assistant-11` | 男性 | 低 | 福岡 | Companion & Peer / Digital Assistant (Parent) | 35-year-old Parent from Fukuoka. Speaks Fukuoka Japanese. Voice is light, airy, and precise |
| `ja-jp-assistant-12` | 男性 | 低 | 東京 | Companion & Peer / Digital Assistant (Friend) | 44-year-old Friend from Tokyo. Speaks Tokyo Japanese. Voice is crisp and eager. |

## commercial

CM ナレーション

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-commercial-1` | 女性 | 高 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Influencer) | 21-year-old Influencer from Tokyo. Speaks Tokyo Japanese. Voice is deep, velvety, and unhurried. |
| `ja-jp-commercial-2` | 男性 | 低 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Fashion Consultant) | 22-year-old Fashion Consultant from Tokyo. Speaks Tokyo Japanese. Voice is resonant and witty. |
| `ja-jp-commercial-3` | 女性 | 高 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Influencer) | 28-year-old Influencer from Tokyo. Speaks Tokyo Japanese. Voice is highly approachable. |
| `ja-jp-commercial-4` | 男性 | 低 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Influencer) | 28-year-old Influencer from Tokyo. Speaks Tokyo Japanese. Voice is bright, breezy, and youthful. |
| `ja-jp-commercial-5` | 男性 | 低 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Fashion Consultant) | 22-year-old Fashion Consultant from Tokyo. Speaks Tokyo Japanese. Voice is resonant and witty. |
| `ja-jp-commercial-6` | 女性 | 高 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Influencer) | 25-year-old Influencer from Tokyo. Speaks Tokyo Japanese. Currently in an oscar winning film. Sounds confident and clear. |
| `ja-jp-commercial-7` | 女性 | 高 | 大阪 | Advertising Pitch & Commerce / Commercial Voiceover (Influencer) | 23-year-old Influencer from Osaka. Speaks Osaka Japanese. Voice is deep, velvety, and unhurried. |

## concierge

コンシェルジュ・秘書

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-concierge-1` | 女性 | 高 | 東京 | Concierge & EA (Executive Assistant) | 30-year-old Executive Assistant from Tokyo. Speaks Tokyo Japanese. Currently at an appointment. Tone is professional yet approachable. |
| `ja-jp-concierge-2` | 男性 | 低 | 福岡 | Concierge & EA (Event Planner) | 36-year-old Event Planner from Fukuoka. Speaks Fukuoka Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-concierge-3` | 女性 | 低 | 大阪 | Concierge & EA (Executive Assistant) | 30-year-old Executive Assistant from Osaka. Speaks Osaka Japanese. Currently on the phone. Tone is professional yet approachable. |
| `ja-jp-concierge-4` | 男性 | 低 | 東京 | Concierge & EA | 34-year-old Concierge from Tokyo. Speaks Tokyo Japanese. Voice is resonant and witty. |
| `ja-jp-concierge-5` | 女性 | 高 | 東京 | Concierge & EA (Hotel Concierge) | 38-year-old Hotel Concierge from Tokyo. Speaks Tokyo Japanese. Voice is engaging and empathic. |
| `ja-jp-concierge-6` | 男性 | 中 | 東京 | Concierge & EA (Event Planner) | 52-year-old Event Planner from Tokyo. Speaks Tokyo Japanese. Voice is crisp and eager. |
| `ja-jp-concierge-7` | 女性 | 中 | 東京 | Concierge & EA (Tour Guide) | 24-year-old Tour Guide from Tokyo. Speaks Tokyo Japanese. Tone is reflective, calm, and reassuring |
| `ja-jp-concierge-8` | 男性 | 低 | 東京 | Concierge & EA | 33-year-old Concierge from Tokyo. Speaks Tokyo Japanese. Currently sitting on couch. Tone is professional yet approachable. |
| `ja-jp-concierge-9` | 中性 | 中 | 東京 | Concierge & EA (Hotel Concierge) | 34-year-old Hotel Concierge from Tokyo. Speaks Tokyo Japanese. Voice is relaxed. |
| `ja-jp-concierge-10` | 女性 | 高 | 大阪 | Concierge & EA (Executive Assistant) | 57-year-old Executive Assistant from Osaka. Speaks Osaka Japanese. Currently at an appointment. Tone is professional yet approachable. |
| `ja-jp-concierge-11` | 女性 | 高 | 福岡 | Concierge & EA (Event Planner) | 63-year-old Event Planner from Fukuoka. Speaks Fukuoka Japanese. Currently at a meditation retreat. Tone is professional yet approachable. |
| `ja-jp-concierge-12` | 男性 | 低 | 東京 | Concierge & EA | 42-year-old Concierge from Tokyo. Speaks Tokyo Japanese. Voice is engaging and empathic. |

## csagent

コールセンター

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-csagent-1` | 男性 | 低 | 東京 | Customer Support Agent / Call Center Agent (Sales Associate) | 30-year-old Sales Associate from Tokyo. Speaks Tokyo Japanese. Currently on npr. Tone is professional yet approachable. |
| `ja-jp-csagent-2` | 女性 | 高 | 大阪 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 23-year-old Customer Service Agent from Osaka. Speaks Osaka Japanese. Voice is natural and clear. |
| `ja-jp-csagent-3` | 男性 | 低 | 東京 | Character & Theatrical (Person Giving Driving Directions) | 39-year-old Person Giving Driving Directions from Tokyo. Speaks Tokyo Japanese. Voice is intimate talkshow. |
| `ja-jp-csagent-4` | 女性 | 中 | 東京 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 64-year-old Customer Service Agent from Tokyo. Speaks Tokyo Japanese. Voice is natural and clear. |
| `ja-jp-csagent-5` | 男性 | 低 | 福岡 | Customer Support Agent / Call Center Agent (Social Worker) | 25-year-old Social Worker from Fukuoka. Speaks Fukuoka Japanese. Voice is comforting someone who is stressed. |
| `ja-jp-csagent-6` | 女性 | 中 | 大阪 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 35-year-old Customer Service Agent from Osaka. Speaks Osaka Japanese. Currently in a bookstore. Tone is professional yet approachable. |
| `ja-jp-csagent-7` | 男性 | 低 | 東京 | Customer Support Agent / Call Center Agent (Sales Associate) | 51-year-old Sales Associate from Tokyo. Speaks Tokyo Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-csagent-8` | 女性 | 高 | 東京 | Customer Support Agent / Call Center Agent (Sales Associate) | 23-year-old Sales Associate from Tokyo. Speaks Tokyo Japanese. Currently in an oscar winning film. Voice is warm and engaging. |
| `ja-jp-csagent-9` | 男性 | 低 | 東京 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 39-year-old Customer Service Agent from Tokyo. Speaks Tokyo Japanese. Currently on npr. Tone is professional yet approachable. |
| `ja-jp-csagent-10` | 男性 | 中 | 福岡 | Customer Support Agent / Call Center Agent (Social Worker) | 29-year-old Social Worker from Fukuoka. Speaks Fukuoka Japanese. Voice is energetic, colorful, and fast |
| `ja-jp-csagent-11` | 女性 | 高 | 東京 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 32-year-old Customer Service Agent from Tokyo. Speaks Tokyo Japanese. Currently in an indie film. Voice is warm and engaging. |
| `ja-jp-csagent-12` | 女性 | 低 | 東京 | Customer Support Agent / Call Center Agent (Customer Service Agent) | 59-year-old Customer Service Agent from Tokyo. Speaks Tokyo Japanese. Currently sitting on couch. Sounds confident and clear. |

## podcaster

ポッドキャスト・ニュース

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-podcaster-1` | 男性 | 低 | 東京 | News & Podcast Host / Podcaster (Podcast Interviewer) | 57-year-old Podcast Interviewer from Tokyo. Speaks Tokyo Japanese. Voice is engaging and empathic. |
| `ja-jp-podcaster-2` | 女性 | 高 | 東京 | News & Podcast Host / Podcaster (Podcast Interviewer) | 28-year-old Podcast Interviewer from Tokyo. Speaks Tokyo Japanese. Currently on npr. Sounds confident and clear. |
| `ja-jp-podcaster-3` | 女性 | 低 | 大阪 | Companion & Peer / Digital Assistant (Podcast Interviewer) | 33-year-old Podcast Interviewer from Osaka. Speaks Osaka Japanese. Currently sitting next to you on the bus. Sounds confident and clear. |
| `ja-jp-podcaster-4` | 男性 | 低 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Political Activist) | 39-year-old Political Activist from Tokyo. Speaks Tokyo Japanese. Currently sitting on couch. Tone is professional yet approachable. |
| `ja-jp-podcaster-5` | 男性 | 中 | 大阪 | Video Voiceover & Host / Training Voiceover (Trivia Host) \| News & Podcast Host / Podcaster (Trivia Host) | 38-year-old Trivia Host from Osaka. Speaks Osaka Japanese. Tone is objective, direct, and helpful |
| `ja-jp-podcaster-6` | 女性 | 中 | 東京 | News & Podcast Host / Podcaster (Podcast Interviewer) | 37-year-old Podcast Interviewer from Tokyo. Speaks Tokyo Japanese. Currently in an oscar winning film. Sounds confident and clear. |
| `ja-jp-podcaster-7` | 男性 | 低 | 東京 | News & Podcast Host / Podcaster (Podcast Interviewer) | 65-year-old Podcast Interviewer from Tokyo. Speaks Tokyo Japanese. Voice is energetic, colorful, and fast |
| `ja-jp-podcaster-8` | 男性 | 低 | 東京 | News & Podcast Host / Podcaster (Radio Host) | 34-year-old Radio Host from Tokyo. Speaks Tokyo Japanese. Voice is bright, breezy, and youthful. |
| `ja-jp-podcaster-9` | 女性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Trivia Host) \| News & Podcast Host / Podcaster (Trivia Host) | 43-year-old Trivia Host from Tokyo. Speaks Tokyo Japanese. Voice is light, airy, and precise |
| `ja-jp-podcaster-10` | 女性 | 中 | 東京 | Companion & Peer / Digital Assistant (Radio Host) | 56-year-old Radio Host from Tokyo. Speaks Tokyo Japanese. Voice is light, airy, and precise |
| `ja-jp-podcaster-11` | 男性 | 中 | 東京 | Video Voiceover & Host / Training Voiceover (Trivia Host) \| News & Podcast Host / Podcaster (Trivia Host) | 38-year-old Trivia Host from Tokyo. Speaks Tokyo Japanese. Tone is objective, direct, and helpful |
| `ja-jp-podcaster-12` | 女性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Trivia Host) \| News & Podcast Host / Podcaster (Trivia Host) | 38-year-old Trivia Host from Tokyo. Speaks Tokyo Japanese. Voice is light, airy, and precise |

## storyteller

朗読・ナレーション

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-storyteller-1` | 女性 | 高 | 東京 | Storyteller & Narrator (Nature Documentary Narrator) | 29-year-old Nature Documentary Narrator from Tokyo. Speaks Tokyo Japanese. Voice is engaging and empathic. |
| `ja-jp-storyteller-2` | 男性 | 低 | 大阪 | Storyteller & Narrator | 27-year-old Storyteller from Osaka. Speaks Osaka Japanese. Voice is engaging and empathic. |
| `ja-jp-storyteller-3` | 女性 | 低 | 福岡 | Storyteller & Narrator (Philosopher) | 48-year-old Philosopher from Fukuoka. Speaks Fukuoka Japanese. Voice is engaging and empathic. |
| `ja-jp-storyteller-4` | 男性 | 低 | 東京 | Storyteller & Narrator (Philosopher) | 49-year-old Philosopher from Tokyo. Speaks Tokyo Japanese. Currently sitting next to you on the bus. Tone is professional yet approachable. |
| `ja-jp-storyteller-5` | 男性 | 低 | 東京 | Storyteller & Narrator (Nature Documentary Narrator) | 24-year-old Nature Documentary Narrator from Tokyo. Speaks Tokyo Japanese. Currently on npr. Tone is professional yet approachable. |
| `ja-jp-storyteller-6` | 男性 | 低 | 大阪 | Storyteller & Narrator (Nature Documentary Narrator) | 27-year-old Nature Documentary Narrator from Osaka. Speaks Osaka Japanese. Voice is light, airy, and precise |
| `ja-jp-storyteller-7` | 女性 | 中 | 福岡 | Storyteller & Narrator | 29-year-old Storyteller from Fukuoka. Speaks Fukuoka Japanese. Voice is comforting someone who is stressed. |
| `ja-jp-storyteller-8` | 女性 | 中 | 東京 | Storyteller & Narrator (Nature Documentary Narrator) | 59-year-old Nature Documentary Narrator from Tokyo. Speaks Tokyo Japanese. Currently at an appointment. Tone is professional yet approachable. |
| `ja-jp-storyteller-9` | 男性 | 低 | 大阪 | Storyteller & Narrator (Philosopher) | 38-year-old Philosopher from Osaka. Speaks Osaka Japanese. Currently sitting next to you on the bus. Tone is professional yet approachable. |
| `ja-jp-storyteller-10` | 女性 | 高 | 東京 | Storyteller & Narrator | 57-year-old Storyteller from Tokyo. Speaks Tokyo Japanese. Currently on the phone. Tone is professional yet approachable. |
| `ja-jp-storyteller-11` | 女性 | 中 | 東京 | Storyteller & Narrator (Philosopher) | 36-year-old Philosopher from Tokyo. Speaks Tokyo Japanese. Voice is intimate talkshow. |
| `ja-jp-storyteller-12` | 男性 | 低 | 東京 | Storyteller & Narrator (Philosopher) | 26-year-old Philosopher from Tokyo. Speaks Tokyo Japanese. Currently brainstorming in a meeting. Tone is professional yet approachable. |

## techagent

技術サポート

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-techagent-1` | 女性 | 高 | 福岡 | Advertising Pitch & Commerce / Commercial Voiceover (Architect) | 43-year-old Architect from Fukuoka. Speaks Fukuoka Japanese. Tone is reflective, calm, and reassuring |
| `ja-jp-techagent-2` | 男性 | 低 | 東京 | Tech Support Agent / Tech Advisor (Architect) | 49-year-old Architect from Tokyo. Speaks Tokyo Japanese. Voice is resonant and witty. |
| `ja-jp-techagent-3` | 女性 | 低 | 大阪 | Tech Support Agent / Tech Advisor (Architect) | 37-year-old Architect from Osaka. Speaks Osaka Japanese. Tone is reflective, calm, and reassuring |
| `ja-jp-techagent-4` | 男性 | 低 | 東京 | Tech Support Agent / Tech Advisor (Architect) | 47-year-old Architect from Tokyo. Speaks Tokyo Japanese. Tone is peer-to-peer and curious |
| `ja-jp-techagent-5` | 女性 | 中 | 大阪 | Tech Support Agent / Tech Advisor | 41-year-old Tech Support Agent from Osaka. Speaks Osaka Japanese. Voice is light, airy, and precise |
| `ja-jp-techagent-6` | 女性 | 中 | 東京 | Tech Support Agent / Tech Advisor (Architect) | 31-year-old Architect from Tokyo. Speaks Tokyo Japanese. Currently on the phone. Voice is warm and engaging. |
| `ja-jp-techagent-7` | 女性 | 高 | 東京 | Tech Support Agent / Tech Advisor | 32-year-old Tech Support Agent from Tokyo. Speaks Tokyo Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-techagent-8` | 男性 | 低 | 福岡 | Tech Support Agent / Tech Advisor | 33-year-old Tech Support Agent from Fukuoka. Speaks Fukuoka Japanese. Currently on the phone. Voice is warm and engaging. |
| `ja-jp-techagent-9` | 女性 | 低 | 福岡 | Tech Support Agent / Tech Advisor (Architect) | 48-year-old Architect from Fukuoka. Speaks Fukuoka Japanese. Voice is textured, resonant, and soothing. |
| `ja-jp-techagent-10` | 男性 | 中 | 東京 | Tech Support Agent / Tech Advisor (Architect) | 32-year-old Architect from Tokyo. Speaks Tokyo Japanese. Voice is bright, breezy, and youthful. |
| `ja-jp-techagent-11` | 男性 | 低 | 福岡 | Tech Support Agent / Tech Advisor (Architect) | 46-year-old Architect from Fukuoka. Speaks Fukuoka Japanese. Currently on npr. Voice is warm and engaging. |
| `ja-jp-techagent-12` | 男性 | 低 | 東京 | Tech Support Agent / Tech Advisor (Architect) | 38-year-old Architect from Tokyo. Speaks Tokyo Japanese. Voice is crisp and eager. |

## training

研修・解説動画

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-training-1` | 女性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 62-year-old Instructional Video Host from Tokyo. Speaks Tokyo Japanese. Currently on npr. Sounds confident and clear. |
| `ja-jp-training-2` | 男性 | 中 | 福岡 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 40-year-old Instructional Video Host from Fukuoka. Speaks Fukuoka Japanese. Tone is conversational, slightly dry humor, and warm |
| `ja-jp-training-3` | 女性 | 中 | 大阪 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 61-year-old Cooking Show Host from Osaka. Speaks Osaka Japanese. Voice is engaging and empathic. |
| `ja-jp-training-4` | 男性 | 低 | 東京 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 63-year-old Instructional Video Host from Tokyo. Speaks Tokyo Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-training-5` | 女性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 27-year-old Cooking Show Host from Tokyo. Speaks Tokyo Japanese. Voice is clear, medium-pitch, and friendly. |
| `ja-jp-training-6` | 女性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 23-year-old Instructional Video Host from Tokyo. Speaks Tokyo Japanese. Currently on npr. Tone is professional yet approachable. |
| `ja-jp-training-7` | 女性 | 中 | 福岡 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 47-year-old Instructional Video Host from Fukuoka. Speaks Fukuoka Japanese. Voice is intimate talkshow. |
| `ja-jp-training-8` | 女性 | 高 | 大阪 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 61-year-old Cooking Show Host from Osaka. Speaks Osaka Japanese. Voice is engaging and empathic. |
| `ja-jp-training-9` | 女性 | 低 | 福岡 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 37-year-old Cooking Show Host from Fukuoka. Speaks Fukuoka Japanese. Currently in an oscar winning film. Tone is professional yet approachable. |
| `ja-jp-training-10` | 女性 | 低 | 東京 | Video Voiceover & Host / Training Voiceover (Instructional Video Host) | 60-year-old Instructional Video Host from Tokyo. Speaks Tokyo Japanese. Tone is reflective, calm, and reassuring |
| `ja-jp-training-11` | 中性 | 高 | 東京 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 41-year-old Cooking Show Host from Tokyo. Speaks Tokyo Japanese. Tone is objective, direct, and helpful |
| `ja-jp-training-12` | 女性 | 中 | 東京 | Video Voiceover & Host / Training Voiceover (Cooking Show Host) | 60-year-old Cooking Show Host from Tokyo. Speaks Tokyo Japanese. Currently in an oscar winning film. Tone is professional yet approachable. |

## tutor

家庭教師

| ID | 性別 | ピッチ | アクセント | ペルソナ | 説明 |
|---|---|---|---|---|---|
| `ja-jp-tutor-1` | 女性 | 中 | 東京 | Video Voiceover & Host / Training Voiceover (Librarian) | 42-year-old Librarian from Tokyo. Speaks Tokyo Japanese. Tone is conversational, slightly dry humor, and warm |
| `ja-jp-tutor-2` | 男性 | 低 | 東京 | Storyteller & Narrator (Therapist) | 36-year-old Therapist from Tokyo. Speaks Tokyo Japanese. Voice is cool, confident, and collaborative. |
| `ja-jp-tutor-3` | 女性 | 高 | 東京 | Educational Tutor (Professor) | 25-year-old Professor from Tokyo. Speaks Tokyo Japanese. Tone is conversational, slightly dry humor, and warm |
| `ja-jp-tutor-4` | 男性 | 低 | 東京 | Educational Tutor (Professor) | 24-year-old Professor from Tokyo. Speaks Tokyo Japanese. Currently on podcast. Tone is professional yet approachable. |
| `ja-jp-tutor-5` | 女性 | 高 | 福岡 | Educational Tutor (Teacher) | 26-year-old Teacher from Fukuoka. Speaks Fukuoka Japanese. Currently in a bookstore. Tone is professional yet approachable. |
| `ja-jp-tutor-6` | 女性 | 低 | 福岡 | Educational Tutor (Teacher) | 45-year-old Teacher from Fukuoka. Speaks Fukuoka Japanese. Currently brainstorming in a meeting. Tone is professional yet approachable. |
| `ja-jp-tutor-7` | 男性 | 低 | 大阪 | Coach & Motivational Guide (Lifestyle Coach) | 22-year-old Lifestyle Coach from Osaka. Speaks Osaka Japanese. Voice is comforting someone who is stressed. |
| `ja-jp-tutor-8` | 女性 | 高 | 東京 | Educational Tutor (Writing Tutor) | 64-year-old Writing Tutor from Tokyo. Speaks Tokyo Japanese. Voice is cool, confident, and collaborative. |
| `ja-jp-tutor-9` | 男性 | 低 | 東京 | Tech Support Agent / Tech Advisor (Librarian) | 40-year-old Librarian from Tokyo. Speaks Tokyo Japanese. Currently on npr. Sounds confident and clear. |
| `ja-jp-tutor-10` | 女性 | 中 | 東京 | Advertising Pitch & Commerce / Commercial Voiceover (Chess Instructor) | 55-year-old Chess Instructor from Tokyo. Speaks Tokyo Japanese. Currently sitting on couch. Tone is professional yet approachable. |
| `ja-jp-tutor-11` | 男性 | 高 | 福岡 | Educational Tutor (Professor) | 31-year-old Professor from Fukuoka. Speaks Fukuoka Japanese. Currently in a bookstore. Sounds confident and clear. |
| `ja-jp-tutor-12` | 男性 | 低 | 大阪 | Storyteller & Narrator (Counselor) | 39-year-old Counselor from Osaka. Speaks Osaka Japanese. Currently sitting next to you on the bus. Tone is professional yet approachable. |
