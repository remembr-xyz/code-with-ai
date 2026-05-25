# Lab 0 — Setup

**Time:** 10 minutes (6:30–6:40)
**Goal:** Everyone in the room has Cursor open, a model selected, and a project folder ready. No one falls behind in Lab 1.

> If you're reading this from home: same five steps. Should take ~10 minutes.

---

## Step 1 — Open Cursor

You should already have it installed from the pre-workshop email. If not:

1. Download from [cursor.sh](https://cursor.sh)
2. Install and open it
3. Sign in (free tier is fine for tonight)

**Check:** You see the Cursor welcome screen.

---

## Step 2 — Pick your model

Cursor needs to know which AI to use as the brain.

1. Open Settings — `Cmd/Ctrl + ,`
2. Go to **Models**
3. Toggle on **Claude Sonnet 4.6** (or **GPT-5** if you prefer)
4. If prompted for an API key:
   - **Easiest path:** use Cursor's built-in plan (free tier includes some Claude calls)
   - **Better path:** sign up at [console.anthropic.com](https://console.anthropic.com) and paste your API key. You get $5 free credit — that's hundreds of prompts.

**Check:** The model dropdown in the bottom-right of Cursor shows your chosen model.

---

## Step 3 — Create your workshop folder

Open your terminal (inside Cursor: `Ctrl + ` `` ` ``).

```bash
mkdir -p ~/sait-workshop
cd ~/sait-workshop
git init
```

Then in Cursor: **File → Open Folder → ~/sait-workshop**.

**Check:** Cursor's file explorer shows an empty `sait-workshop` folder.

---

## Step 4 — Grab the starter files

Two options:

### Option A — Clone the workshop repo (easiest)

```bash
# From inside ~/sait-workshop:
git clone https://github.com/remembr-xyz/code-with-ai.git
cp -r code-with-ai/starter/* code-with-ai/starter/.cursorrules code-with-ai/starter/.gitignore .
rm -rf code-with-ai
```

### Option B — Just download the two files

Grab these from the repo:
- [`starter/AGENTS.md`](../starter/AGENTS.md) → save to `~/sait-workshop/AGENTS.md`
- [`starter/.cursorrules`](../starter/.cursorrules) → save to `~/sait-workshop/.cursorrules`

**Check:** Your folder contains `AGENTS.md`, `.cursorrules`, `.gitignore`, and a `prompts/` folder.

---

## Step 5 — Pick a project (5 min, parallel to setup)

Your guarded agent will work on **a project**. Pick one — small is better than ambitious tonight.

If you came with an idea, use that.

If you didn't, pick from this menu:

| Idea | What you'd build | Why it's a good first project |
|------|------------------|-------------------------------|
| **PDF summarizer CLI** | Drop PDFs into a folder, get markdown summaries | Touches files, AI calls, output — full loop |
| **Personal study helper** | Q&A bot that knows your class notes | Demos memory + scoping |
| **Discord/Slack bot** | Responds to one specific command in your server | Real users, real feedback |
| **Web scraper + summarizer** | "Read this URL, give me 5 bullets" | Quick win, useful daily |
| **Code reviewer for your own repos** | Runs against `git diff`, gives feedback | Meta: AI reviewing AI's work |
| **Daily standup writer** | Reads yesterday's git log, drafts your update | Tiny but ships |

You don't have to finish it tonight. You just need **something concrete enough that the AGENTS.md you write in Lab 1 is real, not made up**.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Cursor won't install | Use VS Code + GitHub Copilot or the Continue.dev extension instead — same concepts work |
| Model says "no API key" | In Cursor Settings → Models, paste an Anthropic key from [console.anthropic.com](https://console.anthropic.com) |
| Terminal won't open in Cursor | Use any external terminal — Cursor doesn't need to host it |
| `git init` says "command not found" | Install Git: [git-scm.com/downloads](https://git-scm.com/downloads) |
| You don't know what to build | Pick the PDF summarizer from the menu — it's the lowest-friction option |

---

## When you're done

You should be staring at:
- Cursor open
- Your `~/sait-workshop/` folder visible in the file tree
- `AGENTS.md` and `.cursorrules` in there (with the template content, you'll customize in Lab 1)
- A project idea in your head

**Tap your neighbor on the shoulder. If they're behind, help them.** Next: [Lab 1 — `AGENTS.md` for your guarded agent](01-agents-md.md).
