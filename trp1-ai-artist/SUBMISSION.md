# TRP1 AI Content Generation - Exploration & Submission

## 1. Environment Setup Documentation

**APIs Configured:**
- GEMINI_API_KEY (Google) ✅
- AIMLAPI_KEY (MiniMax) ✅

**Setup Steps Taken:**
1. Cloned repo: `git clone https://github.com/10xac/trp1-ai-artist.git`
2. Copied `.env.example` to `.env` and added API keys.
3. Installed dependencies: `pip install -r requirements.txt`
4. Verified CLI: `uv run ai-content --help`
5. Verified providers: `uv run ai-content list-providers`
6. Verified presets: `uv run ai-content list-presets`

**Issues Encountered & Resolution:**
- _[Fill in if you faced any setup errors, e.g., API key issues, missing packages]_

---

## 2. Codebase Understanding

**Architecture Description:**
- `cli/` – Command line interface for music, video generation
- `core/` – Provider abstraction, job tracking, result handling
- `providers/` – Individual provider implementations (Google Lyria/Veo/Imagen, AIMLAPI MiniMax)
- `pipelines/` – Orchestration of generation workflows
- `presets/` – Preset definitions for music/video
- `config/` – API keys and configuration loader
- `utils/` – Helper utilities (file handling, lyrics parsing, retries)

**Provider System Insights:**
- Lyria: Instrumental only
- MiniMax: Instrumental + vocals, requires lyrics file
- Veo: Video generation
- Imagen: Image generation
- Presets simplify style selection; pipelines handle orchestration.

**Pipeline Orchestration:**
- `base.py`: common methods for generating content
- `music.py` / `video.py`: specific pipelines for content type
- `full.py`: full orchestration combining prompts → provider → output

---

## 3. Generation Log

**Music Providers Available:**
- lyria, minimax

**Video Providers Available:**
- veo, kling

**Music Presets (style, mood, BPM):**
- jazz: nostalgic (95 BPM)
- blues: soulful (72 BPM)
- ethiopian-jazz: mystical (85 BPM)
- cinematic: epic (100 BPM)
- electronic: euphoric (128 BPM)
- ambient: peaceful (60 BPM)
- lofi: relaxed (85 BPM)
- rnb: sultry (90 BPM)
- salsa: fiery (180 BPM)
- bachata: romantic (130 BPM)
- kizomba: sensual (95 BPM)

**Video Presets (style, aspect ratio):**
- nature: 16:9
- urban: 21:9
- space: 16:9
- abstract: 1:1
- ocean: 16:9
- fantasy: 21:9
- portrait: 9:16

**CLI Commands Explored:**
- Music: `uv run ai-content music --style <preset> --provider <lyria|minimax>`
- Music w/ prompt: `uv run ai-content music --prompt "..." --provider lyria --duration 30`
- Music w/ lyrics: `uv run ai-content music --prompt "..." --provider minimax --lyrics path/to/file.txt`
- Video: `uv run ai-content video --style <preset> --provider veo`
- Video w/ prompt: `uv run ai-content video --prompt "..." --provider veo --aspect 16:9 --duration 5`
