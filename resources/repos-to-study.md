# Repos to study

> **TL;DR** Read 3 real agent codebases before you write your own. Best three: [`sst/opencode`](https://github.com/sst/opencode) (clean, modern), [`paul-gauthier/aider`](https://github.com/paul-gauthier/aider) (small, Pythonic), [`anthropics/anthropic-cookbook`](https://github.com/anthropics/anthropic-cookbook) (recipes). For AGENTS.md examples specifically, jump to [`../starter/examples/agents-md/`](../starter/examples/agents-md/).

You learn more from reading good code than from any tutorial. This is the list of repos worth cloning and reading end-to-end — not because you'll use them, but because the patterns inside them will rewire how you build.

## Reference agents to read

### [`anthropics/anthropic-cookbook`](https://github.com/anthropics/anthropic-cookbook)
Official Anthropic recipes. Notebooks demonstrating tool use, structured outputs, RAG, multi-turn agents. Read `tool_use/` and `agents/` first.

### [`anthropics/claude-code`](https://github.com/anthropics/claude-code)
The actual Claude Code source. Read the `src/` layout to see how a real coding agent is structured. Pay attention to how it handles permissions and tool approval.

### [`openai/openai-cookbook`](https://github.com/openai/openai-cookbook)
Same energy from the other side. Strong notebooks on function calling, evals, embeddings. The "Assistants API" notebooks are useful even if you don't use Assistants.

### [`cline/cline`](https://github.com/cline/cline)
Full agent in TypeScript with a UI. Read `src/core/` for how it manages the agent loop, approval flow, and tool execution.

### [`sst/opencode`](https://github.com/sst/opencode)
Newer, well-architected. Multi-model, plugin-friendly, both CLI and web UI. Worth reading for how to structure an agent for extensibility.

### [`paul-gauthier/aider`](https://github.com/paul-gauthier/aider)
Terminal-native, git-integrated. The codebase is Python and small enough to read in a weekend. Strong patterns for diff editing and undo.

## Learning paths, free courses, structured curricula

### [`mlabonne/llm-course`](https://github.com/mlabonne/llm-course)
The best free LLM curriculum on GitHub by a wide margin. Three tracks: fundamentals, the LLM scientist, the LLM engineer. Lots of Colab notebooks, no fluff.

### [`anthropics/courses`](https://github.com/anthropics/courses)
Anthropic's free course catalog. Prompt engineering, tool use, RAG, real-world workflows. All in notebooks, all hands-on.

### [`anthropics/prompt-eng-interactive-tutorial`](https://github.com/anthropics/prompt-eng-interactive-tutorial)
Nine-chapter prompting tutorial. Anthropic shipped it free. Skip the books — start here.

### [`microsoft/generative-ai-for-beginners`](https://github.com/microsoft/generative-ai-for-beginners)
21 lessons, code in Python and TypeScript. Microsoft's free curriculum. Broad rather than deep, good for orientation.

### [`karpathy/nn-zero-to-hero`](https://github.com/karpathy/nn-zero-to-hero)
Karpathy's "neural networks from zero to hero" YouTube series, with notebooks. **Watch "Let's build GPT" at minimum.** Two hours. Changes how you think about every model after.

### [`rasbt/LLMs-from-scratch`](https://github.com/rasbt/LLMs-from-scratch)
Sebastian Raschka's book repo. Build a tiny LLM end to end. The chapter notebooks are free even without the book.

## Methodologies and design philosophies

### [12-Factor Agents](https://github.com/humanlayer/12-factor-agents)
The "Twelve-Factor App" treatment for agents. Twelve principles for shipping agents reliably. Short, opinionated, worth a 15-minute read.

### [`openai/openai-cookbook` — "Reliable agents" section](https://github.com/openai/openai-cookbook)
Production patterns: retries, fallbacks, structured outputs, observability. Search the cookbook for "reliable" and "evaluation."

### [`humanlayer/humanlayer`](https://github.com/humanlayer/humanlayer)
Library + philosophy for human-in-the-loop agents. The README is the most important file — it's a manifesto for safe agentic workflows.

## Workflow examples to copy

### Real-world `AGENTS.md` files in the wild

The curated, annotated reading guide for AGENTS.md examples lives at [`../starter/examples/agents-md/`](../starter/examples/agents-md/) — including a **by-language section** with verified examples for Python (pydantic-ai, ruff, uv), React Native (gesture-handler, firebase, repack), Kotlin (IntelliJ Community, Ktor, Now in Android), Swift/iOS (Vapor, stripe-ios), Go (Kubernetes, Grafana, Prometheus), and Rust (uv, Deno, Rerun).

Cross-stack picks, ordered from shortest to most thorough:

1. [`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md) — start here, ~4 KB
2. [`temporalio/temporal`](https://github.com/temporalio/temporal/blob/main/AGENTS.md) — voice-shaping
3. [`vercel/ai`](https://github.com/vercel/ai/blob/main/AGENTS.md) — monorepo pattern
4. [`openai/codex`](https://github.com/openai/codex/blob/main/AGENTS.md) — the rigorous one
5. [`apache/airflow`](https://github.com/apache/airflow/blob/main/AGENTS.md) — strictest, most mature

Plus the cross-tool spec at [agents.md](https://agents.md/).

### Real-world `.cursorrules` files

The curated reading guide for cursor rules lives at [`../starter/examples/cursor-rules/`](../starter/examples/cursor-rules/). Highlights:

- **[`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules)** — 39.7k stars, ~190 `.mdc` files indexed by stack
- **[`cursor.directory`](https://cursor.directory)** — community-curated catalog with a UI
- **[`shadcn-ui/ui/.cursor/rules/`](https://github.com/shadcn-ui/ui/blob/main/.cursor/rules/registry-bases-parity.mdc)** — narrow invariant example
- **[`supabase/supabase/.cursor/rules/docs/`](https://github.com/supabase/supabase/tree/master/.cursor/rules/docs)** — path-scoped rules pattern

## Agent frameworks worth studying (even if you don't adopt)

You don't have to use these — but reading their docs once teaches you patterns you'll reach for in plain code.

- **[`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph)** — graph-based agent orchestration. Read their "agentic concepts" docs.
- **[`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI)** — multi-agent roles. Skim the role/task docs.
- **[`microsoft/autogen`](https://github.com/microsoft/autogen)** — multi-agent conversations. Read the architecture doc.
- **[`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai)** — type-safe agents. Read the quickstart and one example.
- **[`run-llama/llama_index`](https://github.com/run-llama/llama_index)** — retrieval-heavy. Skim the "agents" subsection.

## A reading order if you have 10 hours

If you're going to spend a full weekend leveling up:

1. **Hours 1–2:** `karpathy/nn-zero-to-hero` — Let's build GPT (2 videos, ~2 hours).
2. **Hours 3–4:** `anthropics/anthropic-cookbook` — the tool use and agents notebooks.
3. **Hours 5–6:** `cline/cline` — read `src/core/` end to end, take notes on tool approval flow.
4. **Hour 7:** [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) — read in one sitting.
5. **Hour 8:** Pick three `.cursorrules` files from `cursor.directory` for stacks you don't know. Read them, note patterns.
6. **Hours 9–10:** Build something. Anything. Apply what you read.

Two days well spent will get you 90% of the way to being dangerous.
