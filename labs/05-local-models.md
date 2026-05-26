# Lab 5 — Local models (bonus)

**Time:** 5–15 minutes
**Goal:** Point Cursor at a model running on your laptop. Turn WiFi off. Watch it still work.

> The most guarded agent in the world is the one that never sends data anywhere.

---

## Why bother

Three reasons to care about local models, even when cloud quality is still better:

1. **Privacy.** Your prompts, your files, your code — nothing leaves the machine. Mandatory for regulated work, comforting for everything else.
2. **Cost.** After the install, every call is free. Long-running agents become viable.
3. **Offline.** Coffee shop WiFi dies. The plane has none. Your agent doesn't care.

Quality is the trade-off. As of mid-2026, an 8B local model is roughly where GPT-3.5 was — solid for coding tasks, lossy for nuanced reasoning. Picks up quickly on tightly-scoped jobs.

---

## Step 1 — Install Ollama (~3 min)

Ollama runs models with an OpenAI-compatible HTTP server on `localhost:11434`. The smoothest path.

```bash
# macOS
brew install ollama
# or download from https://ollama.com

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download installer from https://ollama.com
```

Start it (macOS app auto-starts; on Linux: `ollama serve &`).

---

## Step 2 — Pull a model (~2 min)

For coding tasks, the best small model right now is `qwen2.5-coder:7b`. If you have less RAM, `qwen2.5-coder:1.5b` is still decent.

```bash
ollama pull qwen2.5-coder:7b      # ~5GB, needs 8GB free RAM
# or
ollama pull qwen2.5-coder:1.5b    # ~1GB, runs on anything
```

Confirm it works:

```bash
ollama run qwen2.5-coder:7b "Write a Python function that validates an email."
```

You should see code stream out in your terminal. If yes, you have a local LLM running.

---

## Step 3 — Point Cursor at it (~2 min)

This is the killer trick. Cursor supports OpenAI-compatible endpoints, and Ollama is one.

1. Open Cursor → Settings (`Cmd/Ctrl + ,`)
2. Go to **Models**
3. Scroll to **OpenAI API Key** section (or "Custom Model" / "OpenAI Compatible")
4. Add a custom model:
   - **Base URL:** `http://localhost:11434/v1`
   - **API key:** anything (`ollama` works — it's ignored, but Cursor requires a non-empty value)
   - **Model name:** `qwen2.5-coder:7b` (or whatever you pulled)
5. Select the new model from the model dropdown in the bottom-right

Some Cursor versions hide custom endpoints behind a toggle — search the settings for "OpenAI" if you can't find the field. The Cursor docs at [docs.cursor.com](https://docs.cursor.com) have the current location.

---

## Step 4 — The WiFi-off moment (~2 min)

This is the demo that sells it.

1. Turn off WiFi (or unplug ethernet)
2. In Cursor, ask: *"Read my AGENTS.md and summarize the guardrails section."*
3. Watch the model think and answer — entirely on your machine

Your filesystem MCP is local (Node process on your laptop). Your inference is local (Ollama on your laptop). Your editor is local. **Nothing leaves the machine.** This is the strongest possible scope.

Turn WiFi back on. Notice nothing changed.

---

## Step 5 — Live with it for a bit

Try the same prompts you've been using all night, but with the local model. Things you'll notice:

- **Speed** depends on your hardware. On Apple Silicon (M1+), an 8B model feels ~30 tokens/sec — comparable to cloud.
- **Quality** drops slightly. Local models are more literal. They follow instructions but don't fill gaps as gracefully.
- **Tool use** is rougher. Some local models don't follow function-calling formats as reliably. You may need to coach with examples.
- **Cost** is zero. Run prompts at 3 AM, no API meter.

When local quality stings, fall back to cloud for that task. When privacy matters, stay local. Most days you'll use a mix.

---

## Pick a better local model for coding

`qwen2.5-coder:7b` is the current sweet spot. Other options:

| Model | RAM | Best at | Pull |
|-------|-----|---------|------|
| `qwen2.5-coder:7b` | 6 GB | General coding. **Start here.** | `ollama pull qwen2.5-coder:7b` |
| `deepseek-coder-v2:lite` | 10 GB | Long-context code, multi-file | `ollama pull deepseek-coder-v2:lite` |
| `qwen2.5-coder:1.5b` | 2 GB | Tiny machines, autocomplete | `ollama pull qwen2.5-coder:1.5b` |
| `llama3.1:8b` | 6 GB | General chat, summaries | `ollama pull llama3.1:8b` |
| `phi3.5:3.8b` | 3 GB | CPU-only laptops | `ollama pull phi3.5:3.8b` |

RAM rule: model size × 1.2 = safe floor.

---

## Bonus — Run the Python agent locally too

If you went down the `guarded_agent.py` path in Lab 3, point it at Ollama by editing the top of the file:

```python
from openai import OpenAI

# Comment out the Anthropic client; use Ollama instead:
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5-coder:7b"
```

Run it with WiFi off. Same agent, same guardrails, zero network.

This is the full local stack: Cursor → local Ollama → local MCP filesystem → local audit log. A guarded agent that never phones home. Code reviewers and lawyers love this configuration.

---

## When you're done

You should have:
- Ollama installed and a model pulled
- Cursor configured to use the local model
- A successful WiFi-off session
- A sense of where local models stand vs. cloud

That's the night. Hit the [resources](../resources/) folder for what to read next, and find me after if you want to keep talking.
