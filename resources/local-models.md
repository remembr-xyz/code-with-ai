# Local models

Running LLMs on your own laptop. Most of the speed/quality argument is decided by the model you pick; the runtimes are interchangeable.

## The two runtimes worth your time

### [Ollama](https://ollama.com)
One-command install, daemon-style, OpenAI-compatible HTTP API on `localhost:11434`. The smoothest path. Recommended for everyone starting out.

```bash
brew install ollama
ollama pull llama3.1:8b
ollama run llama3.1:8b "hello"
```

### [LM Studio](https://lmstudio.ai)
GUI for browsing, downloading, running models. Exposes the same OpenAI-compatible API on `localhost:1234`. Better if you want to compare quants and explore models visually. Heavier than Ollama.

## Other runtimes (skip unless you have a reason)

| Runtime | When |
|---------|------|
| [`llama.cpp`](https://github.com/ggerganov/llama.cpp) | The reference implementation. Both Ollama and LM Studio are wrappers. Use directly only if you need its flags. |
| [`vLLM`](https://github.com/vllm-project/vllm) | Server-side, GPU-heavy, high throughput. For multi-user workloads, not your laptop. |
| [`mlc-llm`](https://github.com/mlc-ai/mlc-llm) | Cross-platform (iOS, browser, etc.). For shipping local AI to end users. |
| [`llamafile`](https://github.com/Mozilla-Ocho/llamafile) | Single-file executable. Works without install. Curiosity-level. |

## Models worth running

Sizes assume 4-bit quantization (the default for Ollama). Add ~30% for fp16.

### Best small coding models
| Model | RAM needed | Best at | Pull |
|-------|------------|---------|------|
| `qwen2.5-coder:7b` | 5–6 GB | Code generation, refactoring | `ollama pull qwen2.5-coder:7b` |
| `deepseek-coder-v2:lite` | 9–10 GB | Long-context code, multi-file | `ollama pull deepseek-coder-v2:lite` |
| `qwen2.5-coder:1.5b` | 1–2 GB | Autocomplete, small machines | `ollama pull qwen2.5-coder:1.5b` |

### Best general-purpose small models
| Model | RAM needed | Best at | Pull |
|-------|------------|---------|------|
| `llama3.1:8b` | 6 GB | Chat, summarization, light code | `ollama pull llama3.1:8b` |
| `qwen2.5:7b` | 5 GB | Multilingual, math | `ollama pull qwen2.5:7b` |
| `gemma2:9b` | 7 GB | Reasoning, instruction following | `ollama pull gemma2:9b` |
| `phi3.5:3.8b` | 3 GB | Tiny machines, surprisingly good | `ollama pull phi3.5:3.8b` |

### When you have a GPU and want serious quality
| Model | RAM/VRAM | Note |
|-------|----------|------|
| `llama3.1:70b` | 40 GB+ | Approaching cloud quality for many tasks |
| `qwen2.5:72b` | 42 GB+ | Strong general model |
| `deepseek-r1:70b` | 42 GB+ | Reasoning model, slower but smarter |

## Where to find models

- **[Ollama library](https://ollama.com/library)** — official catalog
- **[Hugging Face](https://huggingface.co/models?sort=trending&search=gguf)** — every quant of every model, filter by `GGUF` for Ollama-compatible
- **[`TheBloke`](https://huggingface.co/TheBloke)** and **[`bartowski`](https://huggingface.co/bartowski)** — prolific quanters worth following

## How to plug a local model into your tooling

### Cursor
Settings → Models → Add Custom Model
- Base URL: `http://localhost:11434/v1`
- Model name: `llama3.1:8b` (whatever you pulled)
- API key: anything (it's ignored, just required)

### Continue.dev (VS Code)
In `~/.continue/config.json`:
```json
{
  "models": [{"title": "Local", "provider": "ollama", "model": "llama3.1:8b"}]
}
```

### Aider
```bash
aider --model ollama/llama3.1:8b
```

### Your Python code
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
resp = client.chat.completions.create(model="llama3.1:8b", messages=[...])
```

## What local models are NOT good at (yet)

Honesty check: as of mid-2026, local models in the 7B–13B range still trail cloud frontier models on:

- Long-context reasoning (50K+ tokens)
- Tool use with many tools (3+ tools, things get confused)
- Multi-step agentic tasks without strong scaffolding
- Code in less-common languages (Rust, Zig, Go in some cases)

They're great at:
- Short, well-scoped completions
- Summarization
- Classification
- Style transfer
- Anything where being offline/private matters more than the top 10% of quality

## Hardware notes

- **Apple Silicon (M1+):** unified memory means model size ≈ RAM needed. 16GB MacBook runs an 8B model comfortably with everything else open.
- **Linux/Windows with NVIDIA:** GPU VRAM is what matters. 8GB VRAM fits a 7B 4-bit model. 24GB VRAM (RTX 4090) fits 30B+.
- **CPU-only:** works for <7B models. Slower but real. Phi-3.5 3.8B runs surprisingly fast on a modern CPU.
- **RAM rule:** `model_size_GB × 1.2` is a safe floor. Buy more if you can.
