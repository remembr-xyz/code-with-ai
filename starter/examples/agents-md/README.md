# `AGENTS.md` in the wild

> **TL;DR** Seven real `AGENTS.md` files from public repos, each one teaching something different. Slide 33 says to read three end-to-end — these are those three, and four more if you want to go deeper.

The cross-tool standard lives at [agents.md](https://agents.md/). One file, every agent — Cursor, [Claude Code](https://code.claude.com/docs/en/memory), [Codex](https://github.com/openai/codex), and others all read it.

## Quick picks

| If you want… | Read |
|---|---|
| The shortest, easiest to digest | [`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md) (~4 KB) |
| The most rigorous "this is how we encode institutional memory" | [`openai/codex`](https://github.com/openai/codex/blob/main/AGENTS.md) (~18 KB) |
| The best monorepo example | [`vercel/ai`](https://github.com/vercel/ai/blob/main/AGENTS.md) (~13 KB) |
| The most opinionated "shape how the agent talks" | [`temporalio/temporal`](https://github.com/temporalio/temporal/blob/main/AGENTS.md) (~8 KB) |
| The biggest, strictest, most production-grade | [`apache/airflow`](https://github.com/apache/airflow/blob/main/AGENTS.md) (~28 KB) |

## The full catalog (annotated)

### 1. [`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md) — start here

**Size:** ~4 KB · ~120 lines · **Read time:** 5 min

Compact and almost entirely "what good code looks like in this repo" with side-by-side Good/Bad TypeScript snippets. Teaches by example, not by exhortation.

**What to notice:**
- Meta-rules with *names*: "Tests cannot run from repo root (guard: `do-not-run-tests-from-root`)" — the rule is greppable, so the agent can verify it
- Default branch is `dev`, not `main`. Exactly the kind of obvious-to-humans, invisible-to-agents fact AGENTS.md exists for
- Short enough that a model can hold all of it in context at once

### 2. [`openai/codex`](https://github.com/openai/codex/blob/main/AGENTS.md) — the rigorous one

**Size:** ~18 KB · **Read time:** 20 min

Every rule cites an authority — a Clippy lint ID, an ADR number, an exact PR hash like `3c7f013f9735`. This is what *institutional memory written down* looks like.

**What to notice:**
- "Resist adding code to codex-core" — a worked example of using `AGENTS.md` to *defend an architectural decision* against drift
- The anti-pattern discipline: "Never add or modify any code related to `CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR`," with the reason (the sandbox sets it at runtime)
- It's not a style guide — it's a record of decisions the team made and doesn't want re-litigated

### 3. [`vercel/ai`](https://github.com/vercel/ai/blob/main/AGENTS.md) — the monorepo example

**Size:** ~13 KB · **Read time:** 15 min

Maps every `packages/*` to its purpose with a directory table. The ASCII dependency graph (`ai → @ai-sdk/provider-utils → @ai-sdk/provider`) gives the agent a model of the system in eight lines.

**What to notice:**
- The identical content lives at [`CLAUDE.md`](https://github.com/vercel/ai/blob/main/CLAUDE.md) — the "one source of truth across tools" pattern in action
- Package-level scoping: this is how you teach an agent which directory to add a new feature to

### 4. [`apache/airflow`](https://github.com/apache/airflow/blob/main/AGENTS.md) — the strict, mature one

**Size:** ~28 KB · **Read time:** 30 min

A long-running project encoding decades of "we got burned doing X" into rules.

**What to notice:**
- First rule is a *naming* rule: "Write **Dag** in prose, `DAG` only in code." Airflow has lived through that mistake
- "Never run pytest directly on the host — always use `breeze`," with rationale + exact commands. This is the *your project has special tooling, document it* pattern
- A complete tour of what a fully-grown `AGENTS.md` looks like in a real production codebase

### 5. [`browser-use/browser-use`](https://github.com/browser-use/browser-use/blob/main/AGENTS.md) — AGENTS.md "v2"

**Size:** ~38 KB · **Read time:** 30 min

Embeds *product* rules ("always default to and recommend `ChatBrowserUse`") alongside engineering rules. Uses `<guidelines>` / `<browser_use_docs>` XML-ish tags as section anchors.

**What to notice:**
- Part product-spec, part style-guide, part style-of-voice — demonstrates how an opinionated project shapes *what the agent recommends to users*, not just how it codes
- The XML tagging convention is something many internal Anthropic prompts also use — worth seeing in the wild

### 6. [`temporalio/temporal`](https://github.com/temporalio/temporal/blob/main/AGENTS.md) — shape the voice

**Size:** ~8 KB · **Read time:** 10 min

Opens with a *role* assignment ("experienced developer… background in distributed systems") plus a rare "Tone and Style" section: *"Aim for fewer than 3 lines of text output… No chitchat… No preambles."*

**What to notice:**
- `AGENTS.md` being used to *narrow the agent's voice*, not just its code
- If you find the AI is too chatty for your taste, this is the pattern to copy

### 7. [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain/blob/master/AGENTS.md) — the baseline

**Size:** ~13 KB · **Read time:** 15 min

Representative of a "normal" mature project's `AGENTS.md`. Not flashy, not minimal — the kind you'd expect from a well-run open-source project. Worth reading as a baseline of what's typical.

## What didn't make the cut

Some commonly-cited candidates from the [agents.md spec page](https://agents.md/) returned **404** when checked on 2026-05-26:

- `elysiajs/elysia`
- `cline/cline`
- `microsoft/semantic-kernel`

The `agents.md` standard is still spreading — not every adopter listed on the spec page has actually shipped one yet. Don't assume "claimed in spec ⇒ has the file."

## Reading order

### Beginner — 15 minutes total

1. [`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md) — the small one (5 min)
2. Your own [`starter/AGENTS.md`](../../AGENTS.md) template (5 min)
3. [`temporalio/temporal`](https://github.com/temporalio/temporal/blob/main/AGENTS.md) — read the *Tone and Style* section (5 min)

### Going deeper — 60 minutes total

1. [`openai/codex`](https://github.com/openai/codex/blob/main/AGENTS.md) — what mature, rigorous looks like (20 min)
2. [`vercel/ai`](https://github.com/vercel/ai/blob/main/AGENTS.md) — monorepo pattern (15 min)
3. [`apache/airflow`](https://github.com/apache/airflow/blob/main/AGENTS.md) — the strictness ceiling (25 min)

## See also

- [`../claude-md/`](../claude-md/) — how this relates to Claude Code's `CLAUDE.md`
- [`../../../resources/repos-to-study.md`](../../../resources/repos-to-study.md) — broader catalog of repos worth reading
- [agents.md](https://agents.md/) — the cross-tool spec itself

---

*Verified 2026-05-26. If an annotation says "X file is ~Y KB" and you find something different, the upstream repo has evolved — please open an issue.*
