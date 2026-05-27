# Glossary

> **TL;DR** Plain-English definitions of every jargon term you'll hit in this workshop. Bookmark it. Bring it back to whichever lab confused you.

## Agent

A program that uses an LLM in a loop: the model decides whether to answer or call a tool, the tool runs, the result feeds back, repeat until done. See slide 5 ("An agent is a loop") in the deck.

## AGENTS.md

The cross-tool "briefing document" for any AI agent working on your project. Cursor reads it. Claude Code reads it (via the `@AGENTS.md` import pattern). Codex reads it. Spec lives at [agents.md](https://agents.md/). See [`../starter/examples/agents-md/`](../starter/examples/agents-md/) for real examples.

## CLAUDE.md

Claude Code's project-memory file. Closely related to AGENTS.md — the recommended pattern is one line in `CLAUDE.md`: `@AGENTS.md` (which imports it). See [`../starter/examples/claude-md/`](../starter/examples/claude-md/).

## .cursorrules

Cursor-specific operating rules file. Injected into the system prompt of every conversation in this project. Two formats: legacy single `.cursorrules` file (simple projects) and modern `.cursor/rules/*.mdc` directory (larger projects, path-scoped). See [`../starter/examples/cursor-rules/`](../starter/examples/cursor-rules/).

## Guarded agent

An AI agent with rails on: scoped to a folder, locked to an allow-list of tools, forced to ask before destructive actions, logs every action. The thesis of this workshop.

## MCP (Model Context Protocol)

[Anthropic's open standard](https://modelcontextprotocol.io) for plugging external capabilities into AI clients. Cursor, Claude Code, Codex, and Continue all speak it. An MCP server can expose Tools, Resources, and Prompts.

## Tool (in MCP)

A function the model can call. `read_file`, `run_query`, `send_message`. Tools are *active* — the model invokes them.

## Resource (in MCP)

Read-only data the model can fetch. A config file, a record set, a Notion doc. Resources are *passive* — the model pulls them in.

## Prompt (in MCP)

A templated workflow the *user* triggers. `/summarize_pr`, `/file_bug`. Sequential-thinking is a Prompt (it's a reasoning aid), not a Tool.

## Prompt injection

Attack where malicious text inside something an agent reads (a webpage, a file, an email) gets interpreted as instructions rather than data. OWASP ASI01 — "Agent Goal Hijack." Mitigated by the Lethal Trifecta framework: break the trifecta and you break the attack.

## Lethal Trifecta

Simon Willison's framework. An agent with **(a)** access to private data, **(b)** exposure to untrusted content, and **(c)** ability to externally communicate is *unconditionally vulnerable* to prompt injection. Strip away any one of the three to be safe. See [`safeguards.md`](safeguards.md).

## OWASP ASI Top 10

[OWASP's catalogue](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) of the top 10 security risks in *agentic* AI applications. Published Dec 2025. The "OWASP Top 10" but for agents. ASI01–ASI10. See [`safeguards.md`](safeguards.md).

## OWASP LLM Top 10

[OWASP's older catalogue](https://genai.owasp.org/llm-top-10/) of risks in any LLM-touching application (not specifically agentic). LLM01–LLM10. Foundational; ASI is its agentic sequel.

## Sandbox

An isolated environment for running untrusted code. Options range from `subprocess` with a timeout (no isolation) to managed services like [E2B](https://e2b.dev) or [Modal](https://modal.com) (full VM isolation).

## RAG (Retrieval-Augmented Generation)

Pattern where you retrieve documents from a corpus, stuff them into the prompt, and let the model answer based on the retrieved context. Useful when your data doesn't fit in context or changes often.

## ReAct

Reason → Act (call tool) → Observe → Reason. The basic agent loop pattern. From [the ReAct paper](https://arxiv.org/abs/2210.03629).

## Tool use / function calling

The mechanism by which an LLM can request that the host run a function and feed the result back. Anthropic calls it "tool use", OpenAI calls it "function calling" — same concept.

## Auto-Run (Cursor)

Cursor's mode where the agent can run shell commands without per-command approval. Off by default. Has documented bypass vulnerabilities ([Cursor advisory GHSA-534m-3w6r-8pqr](https://github.com/cursor/cursor/security/advisories/GHSA-534m-3w6r-8pqr)). Keep it off until you trust the project.

## Skill (Claude Code / Anthropic)

A markdown file + optional scripts that teaches Claude how to perform a specific procedure. [`anthropics/skills`](https://github.com/anthropics/skills) has examples.

## Hook (Claude Code)

A shell command Claude Code runs in response to events (e.g., before every tool call, after the agent stops). Configured in `settings.json`. Lets you intercept and modify or block actions.

## System prompt

The "instructions to the model" portion of a conversation, distinct from the user's message. Usually contains role, guardrails, available tools, output format. Leaked system prompts of real tools: [`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks).

## Context window

The maximum number of tokens (roughly words ÷ 0.75) a model can "see" at once. Claude Opus has 1M tokens; many local models have 8K–128K. Hits the wall and the model starts losing track of earlier content.

## Token

The model's unit of input/output. ~4 characters of English text on average. A 4K-token response is roughly 3,000 words. You're billed per token on cloud APIs.

## Quantization

Compressing a model from fp16 (16 bits per weight) down to 8, 4, 3, or 2 bits — trading quality for size. A 7B model in fp16 is ~14 GB; in 4-bit quant, it's ~4 GB. Most local-model recommendations assume 4-bit (the default for Ollama).

## GGUF

The file format Ollama, LM Studio, and llama.cpp use. Successor to GGML. If a Hugging Face model has a GGUF variant, you can run it locally.

## Evals

Tests for AI behavior. Run your prompts against expected outputs and score them. Distinct from unit tests because you're checking model behavior, not deterministic code. Start with [`promptfoo`](https://github.com/promptfoo/promptfoo).

## Local model

An LLM running on your laptop instead of in the cloud. Ollama is the easiest way to run one. Quality trails frontier cloud models (~70% as good in 2026); privacy and cost are the wins. See [`local-models.md`](local-models.md).

## Vibe coding

Term coined by Karpathy (Feb 2025) for "I prompt, the model writes, I don't look too closely." Sometimes effective for prototypes; the cause of most production incidents in this workshop's [`safeguards.md`](safeguards.md). The opposite of building a guarded agent.

## See also

- [`safeguards.md`](safeguards.md) — security-specific terms in context (Lethal Trifecta, ASI items)
- [`prompting.md`](prompting.md) — prompting-specific terms (chain-of-thought, few-shot, ReAct, etc.)
- [`mcp-servers.md`](mcp-servers.md) — MCP-specific terms
