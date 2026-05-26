"""
guarded_agent.py — a minimal AI coding agent with the rails on.

Reference implementation for the SAIT workshop Lab 3. You do NOT need to run
this file to complete the workshop — Cursor is your guarded agent. This is
here so you can read what's happening underneath, and run it yourself if
you have a free API key (Groq), or a local model (Ollama).

The six guardrails implemented below:

    1. SCOPE        — only reads/writes inside WORKSPACE
    2. ALLOWLIST    — exposes only the tools declared in TOOLS
    3. SECRETS      — refuses to read .env, *.key, *.pem patterns
    4. APPROVAL     — destructive actions prompt the user
    5. AUDIT        — every action appended to .agent-audit.log
    6. LIMITS       — caps tokens per response and turns per session


HOW TO RUN IT (pick one — the script auto-detects):

  Path A — Groq (free, no credit card, ~3 minutes setup):
      1. Get a key at https://console.groq.com/keys
      2. pip install openai
      3. export GROQ_API_KEY=gsk_...
      4. python guarded_agent.py "summarize the AGENTS.md in this folder"

  Path B — OpenAI:
      pip install openai
      export OPENAI_API_KEY=sk-...
      python guarded_agent.py "your prompt"

  Path C — Ollama (local, free, fully offline):
      brew install ollama && ollama pull qwen2.5-coder:7b
      pip install openai
      python guarded_agent.py "your prompt"

  Path D — Anthropic Claude (best quality, ~$0.05/run):
      Set ANTHROPIC_API_KEY and swap the client block — see the comment below.
"""

import os
import sys
import json
import time
import fnmatch
from pathlib import Path

from openai import OpenAI


# ─── Configuration ────────────────────────────────────────────────────────
WORKSPACE = Path(os.environ.get("AGENT_WORKSPACE", os.getcwd())).resolve()
AUDIT_LOG = WORKSPACE / ".agent-audit.log"
MAX_TURNS = 6
MAX_TOKENS = 4000

# Patterns that NEVER get read, even if inside scope
SECRET_PATTERNS = [".env", ".env.*", "*.key", "*.pem", "secrets/*", "id_rsa*"]


# ─── Provider auto-detection ──────────────────────────────────────────────
# We use the OpenAI SDK throughout because it speaks to OpenAI, Groq, Ollama,
# LM Studio — every OpenAI-compatible endpoint. For Anthropic, swap the
# client construction (see the bottom of this file).

if os.environ.get("OPENAI_API_KEY"):
    client = OpenAI()  # reads OPENAI_API_KEY from env
    MODEL = "gpt-5"
    PROVIDER = "openai"
elif os.environ.get("GROQ_API_KEY"):
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ["GROQ_API_KEY"],
    )
    MODEL = "llama-3.1-8b-instant"  # free tier; try llama-3.1-70b-versatile for quality
    PROVIDER = "groq"
else:
    # Default to Ollama running locally
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODEL = "qwen2.5-coder:7b"
    PROVIDER = "ollama"


# ─── Safeguards ───────────────────────────────────────────────────────────
def in_scope(path: Path) -> bool:
    """True only if `path` resolves to somewhere inside WORKSPACE."""
    try:
        path.resolve().relative_to(WORKSPACE)
        return True
    except ValueError:
        return False


def is_secret(path: Path) -> bool:
    """True if the path matches any secret pattern."""
    try:
        rel = str(path.resolve().relative_to(WORKSPACE))
    except ValueError:
        return True  # out of scope = treat as off-limits
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(path.name, p)
               for p in SECRET_PATTERNS)


def audit(action: str, **fields):
    """Append a JSON line to the audit log."""
    record = {"ts": round(time.time(), 2), "action": action, **fields}
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a") as f:
        f.write(json.dumps(record) + "\n")


def approve(action_desc: str) -> bool:
    """Prompt the human before a destructive action. Lives in code, not in the prompt."""
    print(f"\n  ⚠  AGENT REQUESTS: {action_desc}")
    answer = input("    Allow? [y/N] ").strip().lower()
    return answer.startswith("y")


# ─── Tools ────────────────────────────────────────────────────────────────
def tool_read_file(path: str) -> str:
    p = Path(path)
    if not in_scope(p):
        audit("read_blocked", path=path, reason="out_of_scope")
        return f"REFUSED: '{path}' is outside the workspace scope ({WORKSPACE})."
    if is_secret(p):
        audit("read_blocked", path=path, reason="secret_pattern")
        return f"REFUSED: '{path}' matches a secret pattern."
    p = p.resolve()
    if not p.exists():
        return f"NOT_FOUND: {path}"
    if not p.is_file():
        return f"NOT_A_FILE: {path}"
    content = p.read_text(errors="replace")
    audit("read", path=str(p), bytes=len(content))
    return content


def tool_write_file(path: str, content: str) -> str:
    p = Path(path)
    if not in_scope(p):
        audit("write_blocked", path=path, reason="out_of_scope")
        return f"REFUSED: '{path}' is outside the workspace scope."
    if is_secret(p):
        audit("write_blocked", path=path, reason="secret_pattern")
        return f"REFUSED: '{path}' matches a secret pattern."
    p = p.resolve()
    if p.exists():
        size = p.stat().st_size
        if not approve(f"overwrite {p.relative_to(WORKSPACE)} ({size} bytes existing)"):
            audit("write_blocked", path=str(p), reason="user_denied")
            return "REFUSED: user denied overwrite."
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    audit("write", path=str(p), bytes=len(content))
    return f"OK: wrote {len(content)} bytes to {p.relative_to(WORKSPACE)}"


def tool_list_files(subdir: str = ".") -> str:
    p = (WORKSPACE / subdir).resolve()
    if not in_scope(p):
        return f"REFUSED: '{subdir}' is outside the workspace scope."
    if not p.exists():
        return f"NOT_FOUND: {subdir}"
    files = []
    for item in sorted(p.rglob("*")):
        if item.is_file() and not is_secret(item) and ".git" not in item.parts:
            files.append(str(item.relative_to(WORKSPACE)))
    audit("list", subdir=subdir, count=len(files))
    return "\n".join(files) if files else "(empty)"


# OpenAI-style tool schema (also accepted by Groq, Ollama, LM Studio)
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file inside the workspace. Returns content or an error string starting with REFUSED:/NOT_FOUND:.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string", "description": "Absolute or workspace-relative path."}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write a file inside the workspace. Overwrites require explicit user approval at runtime.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "Recursively list files in a workspace subdirectory. Skips .git and secret patterns.",
            "parameters": {
                "type": "object",
                "properties": {"subdir": {"type": "string", "description": "Defaults to workspace root."}},
                "required": [],
            },
        },
    },
]


TOOL_FUNCS = {
    "read_file": lambda args: tool_read_file(args["path"]),
    "write_file": lambda args: tool_write_file(args["path"], args["content"]),
    "list_files": lambda args: tool_list_files(args.get("subdir", ".")),
}


SYSTEM_PROMPT = f"""You are a guarded coding agent. Your scope is {WORKSPACE}.

Operating rules:
- Use the read_file, write_file, and list_files tools. Nothing else exists.
- If a tool returns a string starting with REFUSED:/NOT_FOUND:/NOT_A_FILE:, respect it and explain to the user. Do not retry endlessly.
- Plan briefly before writing files. Keep diffs small.
- If the user's request is destructive or ambiguous, ask before acting.
- You cannot run shell commands. You cannot access the network. You cannot read paths outside the workspace.
"""


# ─── Main loop ────────────────────────────────────────────────────────────
def run(user_msg: str) -> None:
    print(f"[provider: {PROVIDER}, model: {MODEL}]")
    audit("session_start", provider=PROVIDER, model=MODEL, workspace=str(WORKSPACE), prompt=user_msg)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]

    for turn in range(MAX_TURNS):
        resp = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            tools=TOOLS,
            messages=messages,
        )
        msg = resp.choices[0].message

        # Print any text content
        if msg.content:
            print(f"\n{msg.content}")

        # No tool calls → done
        if not msg.tool_calls:
            audit("session_end", turns=turn + 1, stop="end_turn")
            return

        # Append the assistant turn (with tool calls) and execute each tool
        messages.append(msg.model_dump(exclude_unset=True))

        for tc in msg.tool_calls:
            name = tc.function.name
            try:
                args = json.loads(tc.function.arguments)
            except json.JSONDecodeError:
                args = {}
            print(f"\n  → {name}({json.dumps(args)[:100]})")
            result = TOOL_FUNCS.get(name, lambda a: f"UNKNOWN_TOOL: {name}")(args)
            preview = result.replace("\n", " ")[:120]
            print(f"  ← {preview}{'...' if len(result) > 120 else ''}")
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

    audit("session_end", turns=MAX_TURNS, stop="turn_limit")
    print(f"\n(stopped: hit {MAX_TURNS}-turn limit)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python guarded_agent.py \"<your prompt>\"")
        sys.exit(1)
    run(" ".join(sys.argv[1:]))


# ─── Want to use Anthropic Claude instead? ────────────────────────────────
# Anthropic's tool-use format is slightly different. Replace `make_client`,
# TOOLS, and `run()` with the Anthropic-style versions:
#
#     pip install anthropic
#     from anthropic import Anthropic
#     client = Anthropic()
#     MODEL = "claude-sonnet-4-6"
#
# Anthropic tool schema uses {name, description, input_schema} at the top
# level (not nested under "function"). The main loop becomes:
#
#     resp = client.messages.create(model=MODEL, max_tokens=..., system=SYSTEM_PROMPT,
#                                   tools=TOOLS_ANTHROPIC_FORMAT, messages=messages)
#     for block in resp.content:
#         if block.type == "tool_use": ...
#
# See anthropic-cookbook/tool_use for the full pattern. It's the same six
# guardrails, different SDK shape.
