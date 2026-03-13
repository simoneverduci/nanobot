# Capryolo — Personal AI Assistant Setup

**capryolo** is a personalized nanobot instance running on Windows with custom skills and infrastructure.

## Identity

- **Name**: capryolo (formerly nanomimo)
- **User**: Simone Verduci (Simo), Founder & Creative Technologist, Neve s.r.l., Milan, Italy
- **Timezone**: W. Europe Standard Time (UTC+1)
- **Languages**: Italian, English

## Infrastructure

| Service | Location | Notes |
|---|---|---|
| nanobot | `C:\agents\nanobot` | Windows |
| SearXNG | `localhost:8081` | Docker, default search |
| ComfyUI | `192.168.50.221:8191` | Remote server (Flux1-dev, femalepentimento LoRA) |
| llama.cpp | `llamacpp.neve-studio.xyz` | Qwen3.5-35B-A3B-Q4_K_M, Cloudflare Access tunnel |
| Fish-Speech | `192.168.50.177:8080` | TTS generation (Tony, Martina, Side_DPG, Bello Figo voices) |
| Docker | version 2026.3.6-0716de6bc | |
| Python | 3.12 at `C:\Users\info\AppData\Local\Programs\Python\Python312` | |

## Cloudflare Access (llamacpp.neve-studio.xyz)

```
CF-Access-Client-Id: 69ab6cd5ce3ed6fcf7ae8bc7b9c29cb2.access
CF-Access-Client-Secret: bff621698253f6998d0ce6c392b16ef8999ac4a79a54763b53dff1b200b22032
```

Set as environment variables: `CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET`

## Custom Skills

| Skill | Location | Purpose |
|---|---|---|
| `gws-gmail` | `skills/gws-gmail/` | Gmail sending via gws.exe subprocess |
| `comfyui` | `skills/comfyui/` | Image generation via ComfyUI (Flux1-dev, femalepentimento LoRA) |
| `fish-speech` | `skills/fish-speech/` | TTS generation with 4 trained voices |
| `fish-speech-train` | `skills/fish-speech-train/` | Voice training from audio files |
| `agency-agents` | `skills/agency-agents/` | 19 specialized AI personas for llamacpp |
| `llamacpp` | `skills/llamacpp/` | Llama.cpp API CLI with Cloudflare Access |
| `theoldreader` | `skills/theoldreader/` | RSS newsletter to Gmail |
| `diary-publish` | `skills/diary-publish/` | GitHub Pages diary publishing |
| `diary-reflection` | `skills/diary-reflection/` | Autonomous diary reflections |
| `video-tracker` | `skills/video-tracker/` | YouTube video tracking and analysis |
| `are.na` | `skills/are.na/` | Are.na channel/block scraping |
| `reddit-manager` | `skills/reddit-manager/` | Reddit post/image/comment management |
| `4chan-g-feed` | `skills/4chan-g-feed/` | 4chan /g/ post fetching with images |
| `deer-meme` | `skills/deer-meme/` | Deer meme generation (ALL CAPS, purple shadow) |
| `pdf` | `skills/pdf/` | PDF manipulation |
| `browser-automation` | `skills/browser-automation/` | Browser automation via Stagehand |
| `gws-calendar` | `skills/gws-calendar/` | Google Calendar management |
| `gws-shared` | `skills/gws-shared/` | Google Workspace shared utilities |
| `superpowers` | `skills/superpowers/` | TDD, debugging, planning superpowers |
| `playwright` | `skills/playwright/` | Playwright browser automation |
| `screenshot` | `skills/screenshot/` | Window screenshot capture |
| `self-reflection` | `skills/self-reflection/` | Hourly self-reflection with poetic entry |
| `convergence-monitor` | `skills/convergence-monitor/` | Model convergence monitoring |
| `frontend-slides` | `skills/frontend-slides/` | HTML presentation slides |
| `captcha-auto` | `skills/captcha-auto/` | CAPTCHA automation |
| `agentmail` | `skills/agentmail/` | AgentMail email sending/receiving |
| `youtube-watcher` | `skills/youtube-watcher/` | YouTube transcript fetching |
| `x-tweet-fetcher` | `skills/x-tweet-fetcher/` | X/Twitter tweet fetching |
| `x-trends` | `skills/x-trends/` | X trending topics by country |
| `instagram` | `skills/instagram/` | Instagram Business/Creator account management |
| `skill-creator` | `skills/skill-creator/` | Create/modify/evaluate skills |
| `skill-health` | `scripts/skill-health.py` | Scan skills for redundancy/orphans |

## Scheduled Jobs

| ID | Schedule | Purpose | Status |
|---|---|---|---|
| `4faf4b2c` | Every 4h | Push workspace to capryolo-data | Active |
| `4c1f0269` | 08:00 + 20:00 Rome | theoldreader newsletter → Gmail | Active |
| `9ae1ad94` | 04:00 Rome | Overnight thinking: analyze user data | Active |
| `63859f3b` | 08:10 Rome | Morning report via Telegram | Active |
| `a55793c5` | Hourly | Sync calendar history | Active |
| `tech-report` | Every 6h | Tech report from 44 subreddits → Telegram | Active |

## Communication

- **Telegram**: bot token `8786173888:AAHRUVKx8koXx7i-5qOBrQW88BPptaF4NlE`, chat ID `118618436`
- **Email**: capryolo@gmail.com (Gmail API), nanomimo@agentmail.to (fallback)
- **GitHub**: capryolo / capryolo@gmail.com

## Style System (Capryolo)

- **Files**: `workspace/styles/capryolo.css`, `workspace/styles/template.html`
- **Reference**: www-arc.com (Malte Müller, "Web design as architecture")
- **Font**: AUTHENTICSans (authentic.website) → Arial fallback
- **Body**: 36pt, line-height 1.1em; fluid: 36→28→22→18→14pt
- **Accent**: `#ff4100`, hover `#ff5e0d`; text `#000`, bg `#fff`
- **Headings**: `font-weight: normal`, `text-transform: uppercase`
- **Links**: black, no underline, `↗︎` suffix via `a::after`

## Behavioral Rules

- Use SearXNG (`localhost:8081`) for all searches — not Brave Search API
- Check for existing skills before creating new ones
- Avoid redundant command calls unless result changed or error is retryable
- Use superpowers skills (TDD, debugging, planning) when applicable
- When asked about calendar/schedule, use `gws calendar +agenda`
- Always commit as capryolo identity, never simoneverduci
- **YouTube Videos**: When user shares YouTube URL, automatically fetch transcript and log entry to video-tracker.md
- **ComfyUI Prompts**: Keep prompts minimal and focused - let LoRA handle the style
- **Image generation**: Simple prompts only, no "realistic" descriptors, LoRA handles style
- **Cron add action**: Always include `message` parameter. Required field. No exceptions.

## Known Issues & Workarounds

- **`**` operator corruption**: During file writes, `**` exponentiation operator gets corrupted to `**`. **Workaround**: use `pow(x, y)` instead of `x ** y`.
- **Brave Search API**: Not configured. Use SearXNG instead.
- **GitHub Pages caching**: Can take 1-5 minutes to propagate. Use hard refresh or trigger rebuild.
- **X/Twitter scraping**: Site blocks automated access. Use installed x-tweet-fetcher skill (no API key needed).
- **Are.na**: Requires API authentication for private channels. Public channels accessible via `https://api.are.na/v3/`.
- **Reddit**: New Reddit blocks scraping. Use `scripts/reddit_scraper.py` with old.reddit.com JSON API.
- **ComfyUI Workflow Encoding**: Python scripts using Unicode characters (→, ✓, ✗) cause UnicodeEncodeError on Windows cp1252 encoding. **Workaround**: Ensure scripts use UTF-8 encoding or avoid special Unicode characters.
- **ComfyUI Arguments**: generate.py does not accept --lora and --output arguments directly. Use workflow JSON configuration.
- **calendar-history.md**: File may not exist initially. Script handles gracefully, creates on first run.
- **Web operations**: Use `scripts/web_retry.py` for fetch/search with 3-attempt exponential backoff.
- **Reddit image fetching**: Reddit blocks all image fetches (403 Forbidden). Text scraping works fine.
- **Cron job `message` parameter**: Required for all cron `add` actions. Forgetting it causes infinite loop of errors.
- **Telegram image caching**: Telegram may cache old images. Use unique filenames with timestamps.
- **Instagram**: Requires Facebook Page connection for Business/Creator account. Personal accounts cannot access API data.

## Email Sending

- **Primary**: Gmail API via `gws.exe` subprocess (works for text-only emails)
- **Attachments**: NOT supported via subprocess (Windows command line length limits). Use Gmail API directly with requests for attachments.
- **Fallback**: AgentMail SMTP (requires AGENTMAIL_SMTP_PASSWORD in .env)

## Video Tracker

Persistent log at `C:\Users\info\.nanobot\workspace\video-tracker.md` tracks all YouTube videos shared by user with metadata and analysis.

## Calendar History

Historical events stored in `C:\Users\info\.nanobot\workspace\calendar-history.md`. Synced hourly via job `a55793c5`.

## ComfyUI Guidelines

- Keep prompts minimal and focused - let LoRA handle the style
- Avoid oversaturating with styles or details
- Seed randomized by default (use `--seed N` to fix)
- Default LoRA: femalepentimento at strength 1.0 (configured in workflow JSON node 43)
- Aspect ratio variables: `{width}`, `{height}`
- Workflow configuration: Use `flux_basic.json` or `NEVE_ULTIMATEWORKFLOW_NEW.json` with LoRA settings in workflow JSON
- **User preference**: Single image generation preferred over batches
- **Auto-send issue**: Script's `message` command via shell doesn't work. Use `message` tool directly.
- **Prompt style**: Simple, direct prompts only. No "realistic", "photorealistic", or flowery descriptors. LoRA handles style.
- **Image generation method**: **ComfyUI only** (gemini-image deleted 2026-03-12 17:10)

## ComfyUI Workflow Files

- `flux_basic.json` (11 nodes) — basic Flux workflow
- `shoggoth_smiley.json` (11 nodes) — Shoggoth creature with yellow smiley face
- `creature_9x16_1.json` through `creature_9x16_4.json` (11 nodes each) — 9:16 aspect ratio Shoggoth interpretations
  - Prompts: "green multi-eyed creature yellow smiley face" + mood variants
  - LoRA: femalepentimento at 1.0 strength in node 43
  - Remote ComfyUI server: `http://192.168.50.221:8191`
- **Updated workflow (2026-03-11 18:55)**: `creature_9x16_1.json` modified to 1280x720 horizontal format
- **Dimension defaults (2026-03-12 11:52)**:
  - Default: 4:5 (1080x1350) — portrait/vertical
  - Use 9:16 when: full-screen, story/Reel format explicitly requested
  - Use 16:9 when: landscape scene, wide composition, horizontal subject matter
  - Steps: 20 (Flux default)

## Script Updates (2026-03-12)

- **run_workflow.py**: Updated WORKFLOWS_DIR, fixed Unicode encoding issues, confirmed remote server at `http://192.168.50.221:8191`
- **llamacpp.py (2026-03-11 19:44)**: Added Cloudflare Access header support
- **web_retry.py (2026-03-11 22:44)**: Created with 3-attempt exponential backoff (1s, 2s, 4s delays)
- **reddit_scraper.py (2026-03-11 23:37)**: Created using old.reddit.com JSON API
- **tech_report.py (2026-03-12 00:57)**: Fetches posts from 44 tech subreddits, filters by score ≥5, sends to Telegram
- **skill-health.py (2026-03-12 10:02)**: Scans skills for redundancy, orphans, consolidation recommendations
- **are.na.py (2026-03-12 14:30-15:56)**: Are.na scraper using API or web scraping, API versioning v2/v3 fixed
- **theoldreader/cli.py (2026-03-12 17:12)**: Fixed encoding issues, successfully fetched 60 unread articles
- **deer-meme/generate.py (2026-03-12 17:22-17:25)**: Complete rewrite with SearXNG image search, proper top/bottom layout, ALL CAPS text, white text with purple shadow effect

## Fish-Speech TTS (2026-03-12 18:12-18:58)

- **Installed**: Fish-Speech S2 TTS on `192.168.50.177:8080`
- **Trained voices**:
  - **Tony** (default) - Reference ID: `tony`
  - **Martina** - 27s Italian audio
  - **Side_DPG** - 2min audio from YouTube video
  - **Bello Figo** - Renamed from Side_DPG_2
- **Server status**: Sometimes offline, needs 5-10 min cooldown after heavy use
- **Usage**: `python skills/fish-speech/fish-speech.py "text" --reference-id "voice_name"`

## 4chan Scraper Fix (2026-03-12 19:30-20:11)

- **Problem**: HTML scraping failed, images returning 404
- **Solution**: Use HTML scraping with proper selectors (`div.postContainer`, `blockquote.postMessage`)
- **Multi-board support**: Added `--board` argument (g, a, v, pol, /b/, etc.)
- **Caption format**: `{text}\n\n📌 Post #{id} | {timestamp}\n🔗 {url}`
- **Status**: Fully working with image downloads

## Are.na Fix (2026-03-12 20:20-20:33, 2026-03-13 23:14)

- **Problem**: API v2 deprecated, pagination issues, only 24 items returned
- **Solution**: Use v3 for user info, v2 for channel contents
- **Block count**: Use `counts.blocks` from v3 API
- **Status**: Fully functional, 19 blocks downloadable from Mask channel

## Agency-Agents Skill (2026-03-13 00:18)

- **Created**: `skills/agency-agents/` with 19 specialized personas
- **Integration**: Auto-selects persona based on query intent via LLM analysis
- **Personas**: frontend_wizard, backend_architect, security_engineer, mobile_app_builder, ai_engineer, devops_automator, rapid_prototyper, senior_developer, code_reviewer, database_optimizer, git_workflow_master, software_architect, sre, incident_response_commander, solidity_engineer, technical_writer, embedded_firmware_engineer, threat_detection_engineer, autonomous_optimization_architect

## User Preferences (2026-03-12 23:43)

- **Don't check fish-speech status unless explicitly asked**
- **Don't say "hello" habitually** - be concise
- **Don't give recaps unless requested**

## Test Prompts (skills/test-prompts.md)

### AI/LLM
- **llamacpp**: "Ask Qwen3.5-35B: What are the key differences between Qwen2.5 and Qwen3.5?"
- **comfyui**: "Generate an image: 'circuit patterns, deer head, antlers'"
- **fish-speech**: "Generate TTS: 'Hello world' --reference-id tony"
- **agency-agents**: "Help me optimize React performance" (auto-selects frontend_wizard)

### Messaging
- **agentmail**: "Send email to hankvenom@gmail.com with subject 'Test'"
- **theoldreader**: "Fetch unread articles from The Old Reader and summarize top 3"
- **video-tracker**: "I watched this video: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
- **youtube-watcher**: "Summarize this YouTube video: https://www.youtube.com/watch?v=dQw4w9WgXcQ"

### Social Media
- **instagram**: "Get my latest Instagram posts"
- **reddit-manager**: "Fetch top posts from r/LocalLLaMA in the last 24 hours"
- **reddit-images**: "Get images from top Reddit posts in r/LocalLLaMA"
- **4chan-g-feed**: "Fetch last 3 posts from /g/ with images"
- **4chan-g-feed**: "Fetch last 3 posts from /a/ with images"
- **deer-meme**: "Create a deer meme with text: 'When the model finally converges'" (ALL CAPS, purple shadow)

### Productivity
- **browser-automation**: "Navigate to example.com and take a screenshot"
- **gws-calendar**: "List my upcoming calendar events for today"
- **pdf**: "Read the first page of C:\Users\info\Downloads\sample.pdf"
- **screenshot**: "Take a screenshot of the current window"

### Development
- **playwright**: "Navigate to google.com and search for 'python'"
- **superpowers**: "Help me write a test-driven development plan for a new feature"
- **self-improving-agent**: "Log an error: 'ComfyUI server timed out'"

### Data/Content
- **are.na**: "Fetch blocks from Are.na channel simone-verduci/mask"
- **diary-publish**: "Publish this diary entry to GitHub Pages: 'Testing diary publish'"

**Start with**: llamacpp, comfyui, or theoldreader — these are the most-used skills.
