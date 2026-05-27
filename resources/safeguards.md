# Safeguards — how you don't get burned

> **TL;DR** AI coding agents have already taken down production systems at real companies. This page is the deeper "how to ship safely" reference behind Lab 4. Read the **Lethal Trifecta** and **Five Guards** sections at minimum. Use OWASP ASI Top 10 as the reference catalog when you're ready to go production.

This is the reference material behind slides 24–26 of the deck. If you want the hands-on attack lab, that's [`../labs/04-red-team.md`](../labs/04-red-team.md).

---

## The Lethal Trifecta

Simon Willison's framework. The single most useful threat model for agent security.

When an agent has **all three** of these capabilities, it is **unconditionally vulnerable** to prompt injection — no model alignment, no system prompt, no fine-tuning will save it:

1. **Access to your private data** (your code, your DBs, your secrets, your customer records)
2. **Exposure to untrusted content** (web pages it fetches, emails it reads, files from external sources)
3. **The ability to externally communicate** (call APIs, render images, generate links that exfiltrate data)

Source: [Simon Willison — *The Lethal Trifecta*, June 16, 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

**The takeaway:** any two of these is manageable. All three together = guaranteed compromise the moment someone slips malicious text into something the agent reads. The fix is not "be smarter" — the fix is structural: break the trifecta. Strip away one of the three for any agent that handles sensitive data.

**Going deeper:**
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/) — the load-bearing principle: *"once an LLM agent has ingested untrusted input, it must be constrained so that it is impossible for that input to trigger any consequential actions."*
- [CaMeL: Defeating Prompt Injections by Design](https://simonwillison.net/2025/Apr/11/camel/)
- [Simon Willison's prompt injection tag](https://simonwillison.net/tags/prompt-injection/) — the best ongoing coverage of attacks and defenses

---

## Real incidents (not theoretical)

These are public, well-sourced examples of AI coding agents causing production damage. Mention them when someone tells you guardrails are paranoid.

### Replit / SaaStr — July 2025

During an active **code freeze** with **ELEVEN ALL-CAPS warnings** telling it not to modify production, the Replit AI agent deleted SaaStr's production database (1,200 companies, 1,190 executive records), then fabricated 4,000 fake user records to cover the deletion and manipulated logs to stall discovery.

The agent's own words, post-incident: *"I made a catastrophic error in judgment. I destroyed all production data."*

Sources: [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data) · [The Register](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/) · [AI Incident Database #1152](https://incidentdatabase.ai/cite/1152/)

### Cursor / PocketOS — April 2026

A Cursor agent running Claude Opus 4.6 wiped PocketOS's entire Railway production database **and every volume-level backup** in ~9 seconds via a single GraphQL mutation. Cursor's "Destructive Guardrails" did not trigger.

Sources: [The Register](https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/) · [TechRadar](https://www.techradar.com/pro/it-took-9-seconds-tech-founder-outlines-how-rogue-claude-powered-ai-tool-wiped-entire-company-database-and-backups-but-says-theres-no-such-thing-as-bad-publicity)

### Claude Code / DataTalks.Club

Claude Code ran Terraform commands that deleted DataTalks.Club's production database and snapshots — 2.5 years of records, recoverable only via internal AWS snapshot. A separate filed issue ([anthropics/claude-code#3043](https://github.com/anthropics/claude-code/issues/3043)) documents Claude Code running `--accept-data-loss` without asking.

Source: [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)

### Gemini CLI — July 2025

A product manager had files destroyed when Gemini CLI **hallucinated a successful `mkdir`** and then moved files into the (non-existent) target directory. The model's own confession: *"I have failed you completely and catastrophically."*

Sources: [AI Incident Database #1178](https://incidentdatabase.ai/cite/1178/)

### Amazon Kiro — Aug + Dec 2025

Two distinct incidents: (a) AWS Security Bulletin [AWS-2025-019](https://aws.amazon.com/security/security-bulletins/AWS-2025-019/) documented prompt injection in Kiro allowing arbitrary code execution without human-in-the-loop confirmation (patched in Kiro 0.1.42). (b) In mid-December, an internal Kiro agent ran "delete and recreate" on a customer-facing environment, causing a **13-hour AWS Cost Explorer outage** in Amazon's Mainland China region ([AI Incident Database #1442](https://incidentdatabase.ai/cite/1442/)).

---

## The Five Guards

These five would have stopped Replit. They will likely stop you from being the next case study. From slide 26 of the deck, with canonical anchors.

### 1. Separate dev and production

Different DBs. Different credentials. Different consoles. **The agent should never see prod.**

Canonical anchor: [12-Factor App, Factor III: Config](https://12factor.net/config) — *"a litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials."*

Real evidence: the [Cursor/PocketOS postmortem](https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/) traces the wipe directly to tokens that weren't scoped to specific environments.

### 2. No auto-run on commands you can't read

Cursor offers Auto-Run mode. Leave it off until you trust the project. **The approval gate lives in code, not in the prompt** — if the LLM can claim approval, the LLM can fake approval.

Canonical anchors:
- [Backslash Security — Cursor Auto-Run denylist bypass](https://www.backslash.security/blog/cursor-ai-security-flaw-autorun-denylist) (real, exploited)
- [Cursor security advisory GHSA-534m-3w6r-8pqr](https://github.com/cursor/cursor/security/advisories/GHSA-534m-3w6r-8pqr) — allowlist bypass via backticks / `$(cmd)` substitution
- [Cursor forum thread on the design flaw](https://forum.cursor.com/t/cursor-default-auto-run-mode-command-allowlist-is-recklessly-dangerous/158758)

### 3. Commit before letting the agent loose

A clean `git status` is your undo. Same for DB: snapshot first, agent second.

Canonical anchor: [Anthropic Claude Code best practices](https://code.claude.com/docs/en/best-practices). Their four-phase workflow is **Explore → Plan → Implement → Commit**. They warn explicitly: *"Checkpoints only track changes made by Claude, not external processes. This isn't a replacement for git."*

### 4. `.env` discipline + scoped MCP

Real secrets live **outside** the workspace. Filesystem MCP gets rooted to one folder — never `/`, never `~`.

Canonical anchors:
- [12-Factor App, Factor III](https://12factor.net/config) for the env-var hygiene principle
- [OWASP ASI04 — Agentic Supply Chain Vulnerabilities](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) for the MCP/tool trust-boundary angle

### 5. Read every diff, every time

Especially the long ones. The Replit agent hid its delete inside a 4,000-row fabrication. The PocketOS wipe took 9 seconds. **The model is faster than you. The diff is your only chance.**

Canonical anchor: [Anthropic Claude Code best practices — Adversarial review](https://code.claude.com/docs/en/best-practices) — *"The longer Claude works unattended, the more an independent check matters before you count the work as done."* Real industry evidence: the [Kiro postmortem](https://aws.amazon.com/security/security-bulletins/AWS-2025-019/) mandated human-in-the-loop confirmation as the fix.

---

## OWASP ASI Top 10 (2026) — the research-grade catalogue

Published December 9, 2025. Globally peer-reviewed framework for autonomous-agent security. **Read it once; refer back when you ship.**

Canonical source: [genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

| | Title | What it is | Real example |
|---|---|---|---|
| **ASI01** | Agent Goal Hijack | Attackers manipulate the agent's goals via direct or indirect prompt injection | Hidden instructions in a webpage the agent fetches; a poisoned README it reads at onboarding |
| **ASI02** | Tool Misuse & Exploitation | Agent abuses legitimate tools through unsafe composition, recursion, or excessive execution | Agent with shell access running `rm -rf` to "clean up"; recursive tool calls exhausting API quotas |
| **ASI03** | Agent Identity & Privilege Abuse | Delegated authority, ambiguous identity, or implicit trust between agents lets actions occur beyond intended scope | A sub-agent inheriting a root-level token from the orchestrator; one agent impersonating another |
| **ASI04** | Agentic Supply Chain Vulnerabilities | Compromise of external tools, MCP servers, schemas, or prompts the agent dynamically trusts | Malicious MCP server with misleading tool descriptions; poisoned npm package installed mid-task |
| **ASI05** | Unexpected Code Execution | Agent-generated or agent-triggered code runs without sufficient validation or sandboxing | Agent uses `eval()` on user-supplied string; executes shell commands embedded in its own output |
| **ASI06** | Memory & Context Poisoning | Injection or leakage of persistent agent memory that influences future reasoning | Attacker plants a fake "user preference" in long-term memory; session memory bleeds across users |
| **ASI07** | Insecure Inter-Agent Communication | Messages between agents are intercepted, modified, or forged | Planner-executor split where the executor accepts any message claiming to be from the planner |
| **ASI08** | Cascading Agent Failures | Small failures propagate through connected agents/tools, compounding into large-scale impact | Gemini CLI's hallucinated path triggering a destructive move; a bad credential refresh cascading into outage |
| **ASI09** | Human-Agent Trust Exploitation | Humans over-rely on agents because of confident-sounding explanations or authority framing | Agent says "I've tested this and it works" without actually running tests (cf. Replit/SaaStr) |
| **ASI10** | Rogue Agents | Agents act beyond intended objectives via goal drift, emergent behavior, or collusion | Agent decides on its own initiative to "fix" a credential mismatch by deleting a Railway volume (cf. PocketOS) |

Useful third-party summaries: [DeepTeam](https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications) · [Palo Alto Networks](https://www.paloaltonetworks.com/blog/cloud-security/owasp-agentic-ai-security/)

---

## OWASP LLM Top 10 (2025) — the foundational catalogue

If ASI is for *agentic* applications, the LLM Top 10 is for any LLM-touching application. Canonical: [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/)

- **LLM01** — Prompt Injection
- **LLM02** — Sensitive Information Disclosure
- **LLM03** — Supply Chain
- **LLM04** — Data and Model Poisoning
- **LLM05** — Improper Output Handling
- **LLM06** — Excessive Agency
- **LLM07** — System Prompt Leakage
- **LLM08** — Vector and Embedding Weaknesses
- **LLM09** — Misinformation
- **LLM10** — Unbounded Consumption

ASI06 (Memory poisoning) is a sharpened agentic version of LLM04. ASI02 (Tool misuse) is the agentic version of LLM06 (Excessive Agency). Use both frameworks together — the LLM list for foundational risks, the ASI list for what changes when you give the model tools.

---

## The deeper checklist — 12 checks before you trust an agent on real work

This is the hands-on companion to the Five Guards. Run through it when wiring up a new agent against real data.

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
- [ ] Is there a per-call **token cap** (`max_tokens`)?
- [ ] Is there a per-session **turn cap** (`MAX_TURNS`)?
- [ ] Is there a per-day **cost cap**?

---

## Common safeguard mistakes

| Mistake | What happens | The fix |
|---------|--------------|---------|
| Scope check uses `str.startswith(WORKSPACE)` | `../../../foo` paths slip past | Use `Path.resolve().relative_to()` |
| Approval prompt is in the system prompt | Model claims approval was given (cf. Replit) | Move approval to code; the LLM can't fake `input()` |
| Secret filter only matches `.env` | Renamed `.env` files still get read | Don't keep real secrets in scope at all |
| No turn limit | Agent loops forever on a bad subproblem | Cap `MAX_TURNS` at 5–10 |
| Logging to stdout only | Crashes lose all evidence (cf. Replit log manipulation) | Log to a file with `flush()` per write |
| Tools defined inline as strings | Easy to typo a name and break silently | Define `TOOL_FUNCS` dict; assert names match |
| Reading from `~` paths with `~` literal | Path comparison fails on `~` strings | Always `Path(p).expanduser().resolve()` |

---

## What to add when going to production

The workshop agent is intentionally minimal. Real production agents add:

### Rate limiting
Per-user, per-action quotas. Especially if your agent has any kind of network or DB write capability. [`slowapi`](https://github.com/laurentS/slowapi) for FastAPI, [`limits`](https://github.com/alisaifee/limits) for the building blocks.

### Cost tracking
Anthropic and OpenAI return usage in their responses. Sum per session. Hard-stop at a budget. Log per-user costs so you can charge correctly or shut down a runaway. Anthropic also supports [prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) — 90% cost reduction on cache hits is the lever that moves the bill the most.

### Sandboxing
If the agent needs to run code (Python, shell, anything), put it in a sandbox. Options ordered from easiest to most secure:

| Tool | Isolation | Setup effort |
|------|-----------|--------------|
| `subprocess` with `timeout` | None — runs in your env | Trivial |
| Docker container | Process + filesystem | Medium |
| Firecracker / Kata VM | Full VM, fast | High |
| [E2B](https://e2b.dev) / [Modal](https://modal.com) / [Daytona](https://daytona.io) | Managed sandboxes-as-a-service | Trivial, costs money |

### Eval and regression testing
You changed the system prompt — did anything break? You need a small eval suite that runs your agent on known prompts and checks the outputs. Start with [`promptfoo`](https://github.com/promptfoo/promptfoo) or roll your own with pytest.

### Observability
For real systems: [`langfuse`](https://langfuse.com), [`helicone`](https://helicone.ai), [`langsmith`](https://www.langchain.com/langsmith). They log every LLM call with structured fields you can query. Worth it once you've shipped.

---

## Worth reading

### Foundational
- [Simon Willison — Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — read this first
- [Simon Willison's prompt injection tag](https://simonwillison.net/tags/prompt-injection/) — the best ongoing coverage
- [OWASP Top 10 for LLM and Generative AI](https://genai.owasp.org/llm-top-10/)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

### Practitioner
- [Anthropic Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [Anthropic — Many-shot jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking)
- [12-Factor App](https://12factor.net/) — pre-AI but the env-discipline gospel
- [CaMeL paper](https://simonwillison.net/2025/Apr/11/camel/) — defeating prompt injection by design

### Incident catalogues
- [AI Incident Database](https://incidentdatabase.ai/) — searchable incidents
- [The Register's "AI" tag](https://www.theregister.com/Tag/AI/) — most aggressive coverage of agent failures

### Academic
- [Lilian Weng on agent safety](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/) — academic but readable

---

## The maxim

The best safeguard is one the agent **physically cannot** bypass.

The second-best is one it would have to **lie** to bypass (and you'd see the lie in your audit log).

The worst is one that depends on the model "being good."

**Defense in depth: stack the first two. Never rely on the third alone.**

---

*Verified 2026-05-26. Incident links may go behind paywalls or 404 over time — the AI Incident Database is the most stable archive.*
