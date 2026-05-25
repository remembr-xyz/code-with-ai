# Prompt: Explain this codebase

## Goal
You've inherited a repo. You want a tour before you touch anything.

## Prompt

```
You're helping me onboard to this repo. I've just cloned it and I want
a structured tour before I make any changes.

Do this in three passes:

1. READ the README, package.json (or pyproject.toml), and AGENTS.md
   if it exists. Tell me in 3 sentences what this project does.

2. List the 5 most important files I should read first, in order, with
   one line each on why they matter.

3. Flag anything that looks unusual, deprecated, or risky — old
   dependencies, dead code, missing tests, weird patterns.

Do NOT propose any changes. This is read-only orientation.
```

## Why it works

- Constrains the AI to *read first*, before suggesting anything (no premature edits)
- Gets you a prioritized reading list — not a full dump
- The "do NOT propose changes" line is critical; without it the AI will refactor your README
- Three-pass structure breaks the work into reviewable chunks
