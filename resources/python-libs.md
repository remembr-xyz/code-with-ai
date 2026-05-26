# Python libraries for building agents

The Python libraries worth knowing if you're going to ship your own agents. Ordered roughly by what you'll need first.

## The basics — SDK calls

### [`anthropic`](https://github.com/anthropics/anthropic-sdk-python)
Official Anthropic SDK. Used in `guarded_agent.py`. Clean API, native tool-use support, streaming, vision. Start here if you're calling Claude.

```bash
pip install anthropic
```

### [`openai`](https://github.com/openai/openai-python)
Official OpenAI SDK. Also works with Ollama and LM Studio (they expose an OpenAI-compatible API). The most widely supported pattern.

```bash
pip install openai
```

## Structured outputs

### [`pydantic-ai`](https://github.com/pydantic/pydantic-ai)
Pydantic team's take on agents. Type-safe, model-agnostic (Anthropic, OpenAI, Gemini, Groq, Ollama), built around the Pydantic types you already use. **Recommended next step after the SDKs** — it makes tool definitions and validation feel native to Python.

```bash
pip install pydantic-ai
```

### [`instructor`](https://github.com/jxnl/instructor)
Forces LLMs to return structured Pydantic objects. Bolts onto either SDK. Great for "I need this answer as JSON that I can validate."

```bash
pip install instructor
```

## Heavier frameworks

These are powerful and they have a real learning curve. Worth knowing they exist; don't reach for them on day one.

### [`langgraph`](https://github.com/langchain-ai/langgraph)
LangChain's graph-based agent framework. State machines for agents. Strong when you need branching, retries, human-in-the-loop, persistent state. Production-grade.

### [`llama-index`](https://github.com/run-llama/llama_index)
Retrieval-focused. Built for RAG pipelines. If your agent's job is "answer questions over a corpus," start here.

### [`crewai`](https://github.com/crewAIInc/crewAI)
Multi-agent orchestration. Multiple agents with roles, working in concert. Genuinely useful for some workloads, overkill for most.

### [`autogen`](https://github.com/microsoft/autogen)
Microsoft's multi-agent framework. Lots of features. Long-running conversations between agents.

## Supporting utilities

### [`tenacity`](https://github.com/jd/tenacity)
Retry decorators. API calls fail. Use this so your agent doesn't die on a transient 429.

### [`rich`](https://github.com/Textualize/rich)
Pretty terminal output. Makes your agent's tool calls and audit logs readable instead of a wall of text.

### [`typer`](https://github.com/tiangolo/typer)
Build CLI interfaces in 5 lines. Pair with your agent so it's not just `python script.py "prompt"`.

### [`python-dotenv`](https://github.com/theskumar/python-dotenv)
Load `.env` files. Standard, but **remember Lab 4 — keep real secrets outside the agent's scope** even with this.

## What we use in this workshop

`guarded_agent.py` uses just the `openai` SDK pointed at whichever provider you have a key for — OpenAI, Groq (free), or local Ollama. It's intentionally framework-free so you can read the entire program and understand the agent loop without abstraction layers. Once you've seen it from scratch you can pick up `pydantic-ai` and recognize what it's doing for you.

## A recommended reading order

If you're building agents seriously this year:

1. **Week 1:** the `anthropic` and `openai` SDK docs, end to end
2. **Week 2:** `pydantic-ai` quickstart + their cookbook
3. **Week 3:** read the LangGraph "agentic patterns" docs — you don't need to use LangGraph, but the patterns generalize
4. **Week 4:** build something real with no framework, just the SDK. You'll know what you need.
