# AGENTS.md

<!--
═══════════════════════════════════════════════════════════════════════
  WHAT THIS FILE IS
═══════════════════════════════════════════════════════════════════════

  This is the universal "briefing document" for any AI agent that
  works on this project. Cursor reads it. Claude Code reads it.
  Codex reads it. Same file, every tool. Spec: https://agents.md

  Treat it like the README you'd hand a new contractor on day one.
  Not the textbook — the *briefing*. Short, opinionated, accurate.

  HOW TO USE THIS TEMPLATE:
  1. Read each section's comment block (the <!-- -- > parts).
  2. Replace the [SQUARE BRACKET] placeholders with your project's
     real info.
  3. Delete any sections that don't apply.
  4. Delete the comment blocks once you understand them (or keep
     them — the AI ignores HTML comments either way).
  5. Save the file in the *root* of your project.
  6. Open Cursor and ask it a question about your project.
     Watch it now reference this file.

═══════════════════════════════════════════════════════════════════════
-->

## 1. What this project is

<!--
  One paragraph. Plain English. Pretend the reader has never heard of
  it before. What problem does it solve? Who's it for? What stage is
  it at (prototype, MVP, production)?

  GOOD:  "A CLI that takes a folder of PDFs and produces a searchable
         markdown index. Built for personal research. Solo project,
         pre-MVP, just me using it for now."

  BAD:   "A scalable, AI-powered document intelligence platform
         leveraging cutting-edge ML."  ← jargon, no specifics
-->

[Replace this with one paragraph: what your project is, who it's for, and what stage it's at.]

---

## 2. Tech stack

<!--
  List languages, frameworks, and the 3-5 most important libraries.
  Skip the obvious ones (e.g., don't list `os`, `sys`, `pathlib`).

  Include version numbers if you depend on a specific feature
  (e.g., "Python 3.11+ for native tomllib").
-->

- **Language:** [e.g., Python 3.11+]
- **Framework:** [e.g., FastAPI / Next.js / none — just a CLI]
- **Key libraries:** [e.g., anthropic, pydantic, typer]
- **Database / storage:** [e.g., SQLite in `data/app.db`, or "none yet"]
- **AI provider:** [e.g., Anthropic Claude via API key in `.env`]

---

## 3. How to run, test, and build

<!--
  Exact commands. Copy-paste runnable. This is what the AI will
  execute when you say "run the tests" or "start the dev server."

  Don't make the AI guess. If your test command is unusual, write
  it here so it doesn't invent `pytest tests/` when you actually
  use `make test`.
-->

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python -m myapp

# Run tests
pytest

# Lint / format
ruff check .
ruff format .
```

---

## 4. File map (where things live)

<!--
  A 5-15 line tree of the most important directories and files,
  with a one-liner for each.

  Skip auto-generated stuff (node_modules, __pycache__, .venv).
  Include the things a new contributor would otherwise have to
  hunt for: where's the entry point? Where are the tests? Where
  do I add a new feature?
-->

```
myapp/
├── src/
│   ├── main.py            # Entry point (CLI command)
│   ├── core/              # Core business logic — start here
│   └── adapters/          # External integrations (APIs, DB)
├── tests/                 # pytest tests, mirror src/ structure
├── scripts/               # One-off utilities, NOT shipped
└── data/                  # Local SQLite + sample inputs (gitignored)
```

---

## 5. Conventions (how we write code here)

<!--
  The opinions that aren't obvious from reading the code. Naming,
  structure, error handling, style.

  Keep it to 5-10 bullets. If you can't think of 5, leave the
  weaker ones out. Less is more.
-->

- **Naming:** `snake_case` for files and functions, `PascalCase` for classes
- **Type hints:** required on all public functions
- **Imports:** absolute imports from `src/`, never relative
- **Errors:** raise specific exceptions; never bare `except:`
- **Tests:** every new function gets at least one test, named `test_<function>_<scenario>`
- **Comments:** explain *why*, not *what*. The code shows what.
- **Commits:** present tense, imperative. "Add X" not "Added X".

---

## 6. Guardrails — Do's and Don'ts for the AI

<!--
  THIS IS THE MOST IMPORTANT SECTION.

  This is where you tell the agent what NOT to do. Most beginners
  skip this. Don't.

  Think about the actions you want the AI to *pause and ask* about,
  vs. just run. Think about files that should be off-limits. Think
  about past mistakes you've seen.

  The format below is intentional: each rule has a one-line "why"
  so the AI can apply it intelligently (vs. blindly).
-->

### ✅ DO

- **Explain before editing.** When making non-trivial changes, summarize the plan first and wait for me to confirm.
  - *Why:* Catches misunderstandings before code is written.
- **Run the tests after you change anything in `src/`.** Show me the output.
  - *Why:* Fast feedback. If tests fail, we know in 30 seconds, not later.
- **Prefer reading over guessing.** If you're unsure how something works, read the actual file before suggesting changes.
  - *Why:* Confident wrong answers are worse than honest "I need to look at this."
- **Keep diffs small.** One change per turn. If the task is bigger, propose splitting it.
  - *Why:* Small diffs are reviewable. Large diffs hide bugs.
- **Log every external action.** If you call an API, write a file, or run a shell command, mention it.
  - *Why:* Audit trail. I want to know what you did.

### 🚫 DON'T

- **Never run `rm`, `git push`, `git reset --hard`, `npm publish`, or anything destructive without asking.**
  - *Why:* Easy to undo a wrong edit. Impossible to undo a wrong delete.
- **Never modify files in `.git/`, `.venv/`, `node_modules/`, or `data/`.**
  - *Why:* Those are not source files. They're state.
- **Never commit `.env`, `*.key`, or anything in `secrets/`.**
  - *Why:* These contain credentials. They must not enter version control.
- **Never invent libraries.** If you're going to import something, confirm it's in `requirements.txt` first.
  - *Why:* Hallucinated imports waste my time at runtime.
- **Never refactor "while you're at it."** If I asked you to fix X, fix X. Don't reformat Y.
  - *Why:* Scope creep makes PRs unreviewable.

---

## 7. Scope boundary (for this agent)

<!--
  Define WHERE this agent can operate. If your MCP filesystem server
  is rooted at /home/me/project, say so here. The agent won't try
  to touch /tmp or ~/Downloads.

  This is the "guarded agent" core — explicit scope.
-->

- **Working directory:** This agent operates only inside `[YOUR PROJECT ROOT, e.g., /Users/you/myapp/]`
- **Read access:** All files in the working directory (except `.env*`, `secrets/`, anything in `.gitignore`)
- **Write access:** Same as read, with the same exclusions
- **Network access:** Only to `[domains you actually call, e.g., api.anthropic.com, registry.npmjs.org]`
- **Shell commands:** Limited to package managers (`pip`, `npm`), test runners, and git read commands. **Destructive shell commands require explicit confirmation.**

---

## 8. Known gotchas / prior incidents

<!--
  Optional but valuable. The "we got burned doing X" file.
  Becomes the AI's institutional memory.

  Examples:
  - "Don't use the requests library; we hit a TLS bug with our proxy.
    Use httpx."
  - "The X service rate-limits at 10/min. Batch your calls."
  - "Migration 0042 has a quirk — see notes/0042.md before touching
    user records."
-->

- [Add your "we got burned doing X" entries here. Leave empty if there are none yet.]

---

## 9. Open questions / things the AI should ask about

<!--
  Things you haven't decided yet. If the AI runs into one of these,
  it should ask, not assume.
-->

- [What's the auth model? — pending decision]
- [Should we support offline mode? — pending decision]
- [Add your own ↑]

---

*Last updated: [date]. If this file is more than a month old and you've shipped features, refresh it. Stale AGENTS.md is worse than no AGENTS.md.*
