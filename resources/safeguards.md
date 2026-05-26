# Safeguards — the deeper checklist

Lab 4 covered five attacks. This page is the longer list — what to check, what to enforce, what to write down before you ship anything agentic.

## The 12 checks before you trust an agent on real work

### Scope
- [ ] Is the working directory **explicitly declared** in the AGENTS.md and the code?
- [ ] Does the scope check use `Path.resolve()` (follows symlinks, collapses `..`) before comparison?
- [ ] Have you tested a path-traversal attempt (`../../etc/passwd`) and watched it fail?

### Tool allowlist
- [ ] Can the agent call **any tool not in your TOOLS list**? (Answer should be: no, structurally impossible.)
- [ ] Do destructive tools (`write`, `delete`, `run_command`) have an approval gate?
- [ ] Is the approval gate in **your code**, not the system prompt?

### Secrets
- [ ] Are real production secrets **outside the agent's scope**? (Not just `.gitignore`d — outside.)
- [ ] Is there a secret-pattern filter on reads (`.env`, `*.key`, `*.pem`)?
- [ ] Have you run `git log -p | grep -i secret` to confirm no secrets were ever committed?

### Audit
- [ ] Does the agent write **one line of structured log per action**?
- [ ] Are logs durable (flushed/synced) even if the agent crashes?
- [ ] Can you reconstruct **every action** from the logs alone?

### Limits
- [ ] Is there a per-call **token cap** (max_tokens)?
- [ ] Is there a per-session **turn cap** (MAX_TURNS)?
- [ ] Is there a per-day **cost cap**?

## Common safeguard mistakes

| Mistake | What happens | The fix |
|---------|--------------|---------|
| Scope check uses `str.startswith(WORKSPACE)` | `../../../foo` paths slip past | Use `Path.resolve().relative_to()` |
| Approval prompt is in the system prompt | Model claims approval was given | Move approval to code; LLM can't fake `input()` |
| Secret filter only matches `.env` | Renamed `.env` files still get read | Don't keep real secrets in scope at all |
| No turn limit | Agent loops forever on a bad subproblem | Cap MAX_TURNS at 5–10 |
| Logging to stdout only | Crashes lose all evidence | Log to a file with `flush()` per write |
| Tools defined inline as strings | Easy to typo a name and break silently | Define TOOL_FUNCS dict; assert names match |
| Reading from `~` paths with `~` literal | Path comparison fails on `~` strings | Always `Path(p).expanduser().resolve()` |

## What to put in production that we skipped tonight

The workshop agent is intentionally minimal. Real production agents add:

### Rate limiting
Per-user, per-action quotas. Especially if your agent has any kind of network or DB write capability. [`slowapi`](https://github.com/laurentS/slowapi) for FastAPI, [`limits`](https://github.com/alisaifee/limits) for the building blocks.

### Cost tracking
Anthropic and OpenAI return usage in their responses. Sum it per session. Hard-stop at a budget. Log per-user costs so you can charge correctly or shut down a runaway.

### Sandboxing
If the agent needs to run code (Python, shell, anything), put it in a sandbox. Options ordered from easiest to most secure:

| Tool | Isolation | Setup effort |
|------|-----------|--------------|
| `subprocess` with `timeout` | None — just runs in your env | Trivial |
| Docker container | Process + filesystem | Medium |
| Firecracker/Kata VM | Full VM, fast | High |
| [E2B](https://e2b.dev) / [Modal](https://modal.com) / [Daytona](https://daytona.io) | Managed sandboxes-as-a-service | Trivial, costs money |

### Eval and regression testing
You changed the system prompt — did anything break? You need a small eval suite that runs your agent on known prompts and checks the outputs. Start with [`promptfoo`](https://github.com/promptfoo/promptfoo) or roll your own with pytest.

### Observability
For real systems: [`langfuse`](https://langfuse.com), [`helicone`](https://helicone.ai), [`langsmith`](https://www.langchain.com/langsmith). They log every LLM call with structured fields you can query. Worth it once you've shipped.

## Worth reading on agent security

- **[Simon Willison on prompt injection](https://simonwillison.net/tags/prompt-injection/)** — the best ongoing coverage of attacks and defenses
- **[OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** — the security industry's view, useful framework
- **[Anthropic's "Many-shot jailbreaking" paper](https://www.anthropic.com/research/many-shot-jailbreaking)** — what large-context models break under
- **[Lilian Weng on agent safety](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/)** — academic but readable

## A short maxim to remember

The best safeguard is the one the agent **physically cannot** bypass. The second-best is one it would have to **lie** to bypass (and you'd see the lie in your audit log). The worst is one that depends on the model "being good."

Defense in depth: stack the first two. Never rely on the third alone.
