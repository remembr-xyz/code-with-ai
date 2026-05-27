# Resources

Curated reading. No filler. Every link below points to something specific and worth your time.

## The files

| File | What it covers |
|---|---|
| [`tools.md`](tools.md) | Cursor, Claude Code, Aider, Continue, opencode, Cline. When to pick which. Comparison table at the bottom. |
| [`python-libs.md`](python-libs.md) | `anthropic`, `openai`, `pydantic-ai`, `instructor`, `litellm`, agent frameworks. Grouped by purpose. |
| [`mcp-servers.md`](mcp-servers.md) | The 4 starter MCPs, the official registry vs third-party marketplaces, vetting checklist. |
| [`prompting.md`](prompting.md) | Prompt libraries, leaked system prompts of real tools, named patterns (ReAct, few-shot, plan-and-execute). |
| [`safeguards.md`](safeguards.md) | **Read this.** Lethal Trifecta + 5 real incidents + Five Guards + OWASP ASI Top 10. |
| [`local-models.md`](local-models.md) | Ollama, LM Studio, model recommendations by RAM tier, how to wire local models into Cursor/Claude Code/Aider. |
| [`repos-to-study.md`](repos-to-study.md) | Repos worth cloning and reading end-to-end. Reference agents, learning paths, methodologies. |
| [`further-reading.md`](further-reading.md) | Newsletters, papers, books, channels, a 30-day reading plan. |
| [`figma-experiments.md`](figma-experiments.md) | Figma → code workflows. Pairs with [`../starter/examples/mcp/figma.md`](../starter/examples/mcp/figma.md). |
| [`glossary.md`](glossary.md) | **Bookmark this.** Plain-English definitions of every term in the workshop. |

## Reading order

### If you've done the workshop and want to keep going (recommended)

1. [`glossary.md`](glossary.md) — 5 min, just to anchor terms
2. [`safeguards.md`](safeguards.md) — the deep dive on Lab 4
3. [`prompting.md`](prompting.md) — biggest day-to-day lever
4. [`tools.md`](tools.md) — when to switch tools
5. [`further-reading.md`](further-reading.md) → pick the 30-day plan at the bottom

### If you want to build your own agent

1. [`repos-to-study.md`](repos-to-study.md) — read 2 reference agents before writing your own
2. [`python-libs.md`](python-libs.md) — what to install
3. [`mcp-servers.md`](mcp-servers.md) — how to give your agent tools
4. [`safeguards.md`](safeguards.md) — what not to do

### If you're optimizing for privacy / offline

1. [`local-models.md`](local-models.md) — start here
2. [`tools.md`](tools.md) — sections on Aider and Continue (best local-model UX)
3. [`safeguards.md`](safeguards.md) — local models still need scope discipline

### If you read [Learn Agentic AI](https://learnagentic.substack.com) and want depth

1. [`safeguards.md`](safeguards.md)
2. [`repos-to-study.md`](repos-to-study.md)
3. [`further-reading.md`](further-reading.md) — papers + books section

## See also

- [`../starter/examples/`](../starter/examples/) — the **inspiration gallery** of real AGENTS.md, cursor rules, MCP configs, CLAUDE.md
- [`../labs/`](../labs/) — the hands-on path through the workshop material
