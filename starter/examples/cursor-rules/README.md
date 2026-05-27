# Cursor rules — where to crib from

> **TL;DR** There are two formats for Cursor rules: the legacy `.cursorrules` single file (still works) and the modern `.cursor/rules/*.mdc` directory. Big projects use the directory form. This page lists curated real examples of both and shows you where to find more.

Official docs: [docs.cursor.com/context/rules](https://docs.cursor.com/context/rules)

## Two formats, one purpose

| Format | When to use | Where it lives |
|---|---|---|
| `.cursorrules` (legacy single file) | Small project, one global rule set, <30 lines | Repo root |
| `.cursor/rules/*.mdc` (modern directory) | Larger project, path-scoped or topic-scoped rules | `.cursor/rules/` directory |

Big projects have **mostly migrated to the directory form**. It lets you scope a rule to a specific path (e.g., "this rule only applies in `src/components/`") via the `globs:` frontmatter field. For a workshop project, the single-file form is fine. For your real projects, consider the directory form once your rules exceed ~30 lines.

## Curated sources to crib from

### Community catalogs

| Source | What's there |
|---|---|
| [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) (39.7k stars) | ~190 `.mdc` files in [`rules/`](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules), one per stack — React, Next.js, FastAPI, Rust, Go, Solidity, etc. Each has frontmatter. Drop-in friendly. |
| [`cursor.directory`](https://cursor.directory/) | Community-curated catalog with a UI. Browse by stack, copy individual rules. |
| [`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks) | Leaked system prompts from major AI tools. Not rules per se — but gold for understanding what *good* prompting looks like internally. |

### Real production examples (`.cursor/rules/*.mdc`)

| Repo | Path | What to notice |
|---|---|---|
| [`shadcn-ui/ui`](https://github.com/shadcn-ui/ui/blob/main/.cursor/rules/registry-bases-parity.mdc) | `.cursor/rules/registry-bases-parity.mdc` | Narrow invariant ("registry bases must stay in parity"). Not generic style advice — the exact use case rules are designed for. |
| [`supabase/supabase`](https://github.com/supabase/supabase/tree/master/.cursor/rules/docs) | `.cursor/rules/docs/*` | Path-scoped rules organized by documentation subdomain (`docs-embeddings-generation/RULE.md`, `docs-graphql/RULE.md`, etc.) |
| [`vercel/next.js`](https://github.com/vercel/next.js/tree/canary/.cursor) | `.cursor/commands/`, `.cursor/worktrees.json` | Not rules — but shows that `.cursor/` is also where Cursor *commands* and worktree config live. Worth knowing it's more than rules. |

## What goes in (and what doesn't)

From slide 15 of the deck:

### DO put in rules
- "Always run tests after editing"
- "Prefer pytest over unittest"
- "Don't touch migrations without asking"
- "Explain before non-trivial edits"

### DON'T put in rules
- Details that change daily (move to AGENTS.md or PR descriptions)
- The whole architecture (move to AGENTS.md)
- Secrets, tokens, keys (move to environment / vault)
- Anything the AI can read from the code

**Rules are for the invisible** — preferences, priorities, prior incidents. If a rule tries to summarize the code, it'll go stale before the week is out.

## Rules look different by stack

The deck (slide 16) breaks this out by role. Verbatim from the appendix:

### Backend
```
- Run pytest after every src/ change
- Show migration SQL before applying
- Type hints required; mypy clean
```

### Frontend
```
- Use design system tokens; no custom colors
- Aria labels on every interactive element
- Verify mobile-first at 380px
```

### DevOps / SRE
```
- terraform plan before any apply
- Audit log every infra change
- Dry-run all destructive commands
```

### Data
```
- Never log row contents; PII flagged
- Parameterized queries only
- Verify counts before & after migrations
```

Same skeleton, different priorities. Pick the role closest to your project and adapt.

## By language — deep links into `awesome-cursorrules`

[`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) is **flat** — all 256 rule files sit one level deep in [`rules/`](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules), no subdirectories by language. Below are deep links to specific `.mdc` files per language (all verified 2026-05-27).

### Python

| File | Size | Use for |
|---|---|---|
| [`python.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/python.mdc) | 3.3 KB | Generic Python |
| `python-fastapi-cursorrules-prompt-file.mdc` | – | FastAPI stack |
| `python-django-cursorrules-prompt-file.mdc` | – | Django stack |
| `python-flask-cursorrules-prompt-file.mdc` | – | Flask stack |
| `python-llm-ml-workflow-cursorrules-prompt-file.mdc` | – | ML/LLM workflow projects |

Browse the [full list of Python `.mdc` files](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules) — there are 13+ Python-flavored entries.

### React Native (mobile JS/TS)

| File | Size | Use for |
|---|---|---|
| [`react-native-expo-cursorrules-prompt-file.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/react-native-expo-cursorrules-prompt-file.mdc) | 997 B | Expo-based RN projects |
| `react-native-expo-router-typescript-windows-cursorrules-prompt-file.mdc` | – | Expo + Expo Router + TS on Windows |

### Kotlin (Android + backend)

| File | Size | Use for |
|---|---|---|
| [`kotlin-ktor-development-cursorrules-prompt-file.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/kotlin-ktor-development-cursorrules-prompt-file.mdc) | 9.3 KB | Ktor server framework |
| [`kotlin-springboot-best-practices-cursorrules-prompt-file.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/kotlin-springboot-best-practices-cursorrules-prompt-file.mdc) | 7.2 KB | Spring Boot in Kotlin |
| `android-jetpack-compose-cursorrules-prompt-file.mdc` | 2.8 KB | Modern Android apps (Compose) |

### Swift / iOS

| File | Size | Use for |
|---|---|---|
| [`swiftui-guidelines-cursorrules-prompt-file.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/swiftui-guidelines-cursorrules-prompt-file.mdc) | 4.4 KB | SwiftUI apps |
| [`swift-uikit-cursorrules-prompt-file.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/swift-uikit-cursorrules-prompt-file.mdc) | 23.9 KB | UIKit (the biggest single rule file in the repo — exhaustive) |

### Go

| File | Size | Use for |
|---|---|---|
| [`go.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/go.mdc) | 1.2 KB | Generic Go |
| `go-backend-scalability-cursorrules-prompt-file.mdc` | – | Scalable backend services |
| `go-servemux-rest-api-cursorrules-prompt-file.mdc` | – | REST APIs with stdlib `net/http` |
| `go-temporal-dsl-cursorrules-prompt-file.mdc` | – | Temporal workflow code |

### Rust

| File | Size | Use for |
|---|---|---|
| [`rust.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/rust.mdc) | 4.2 KB | Generic Rust |
| [`rust-general.mdc`](https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/rust-general.mdc) | 2.2 KB | Alternative generic Rust ruleset |

### TypeScript / Node

The repo has 30+ TypeScript-flavored rules. Search [`rules/`](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules) for `typescript-*`, `next-*`, `react-*`, `node-*` to find the one matching your stack.

> **Tip:** the file naming convention is `<stack>[-<framework>-...]-cursorrules-prompt-file.mdc` for stack-specific ones, or just `<language>.mdc` for generic ones. Newer additions tend to use the longer naming. If a deep link 404s, browse [the index](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules) and grep.

## A note on the `.cursorrules` we ship

The [`starter/.cursorrules`](../../.cursorrules) in this repo uses the legacy single-file form on purpose — it's easier for a workshop. If you find yourself adding rule #20, that's the signal to migrate to `.cursor/rules/*.mdc` instead.

## See also

- [`../agents-md/`](../agents-md/) — AGENTS.md is the *briefing*; cursor rules are the *standing orders*
- [`../../../resources/prompting.md`](../../../resources/prompting.md) — patterns that often want to be rules
