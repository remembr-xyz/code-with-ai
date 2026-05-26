# Further reading

If the workshop hooked you, here's where to go next. Curated, not comprehensive.

## Daily reading

### [Learn Agentic AI](https://learnagentic.substack.com)
Yes, this is mine. Daily writing on what's actually working in AI coding right now. New tools, real techniques, no hype. Subscribe.

### [Simon Willison's Weblog](https://simonwillison.net)
The single best independent voice on this entire industry. Read every post. He coined "prompt injection," writes daily, and never wastes your time.

### [Hacker News](https://news.ycombinator.com/from?site=anthropic.com) (Anthropic + OpenAI tags)
Filter for the AI tooling discussions. The comments often contain the best critique.

### [Latent Space](https://www.latent.space)
Podcast + newsletter. Deep technical interviews with people actually building this stuff.

## Less frequent but worth subscribing

- **[Eugene Yan](https://eugeneyan.com)** — engineering rigor on ML systems. The "ML engineering" content is gold.
- **[Lilian Weng](https://lilianweng.github.io)** — deep, paper-grade posts on agent design, hallucination, safety.
- **[Chip Huyen](https://huyenchip.com/blog/)** — productionizing ML systems, occasional but excellent.
- **[Jason Liu](https://jxnl.co)** — structured outputs, RAG, the practical end of LLM engineering.
- **[Hamel Husain](https://hamel.dev/blog)** — evals, fine-tuning, real-world ML systems.

## Papers worth your time (readable, not academic torture)

- **["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)** — the original Transformer paper. Foundational; read once for the diagrams.
- **["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629)** — the loop you're using in `guarded_agent.py`. 8 pages, lucid.
- **["Reflexion: Language Agents with Verbal Reinforcement Learning"](https://arxiv.org/abs/2303.11366)** — how to make agents improve from their own mistakes.
- **["Toolformer"](https://arxiv.org/abs/2302.04761)** — how models learn to use tools. Background for MCP.
- **["Many-shot Jailbreaking"](https://www.anthropic.com/research/many-shot-jailbreaking)** — Anthropic's analysis of what breaks long-context models. Practical security.

## Books

- **["Designing Machine Learning Systems"](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)** — Chip Huyen. The textbook for shipping ML in production. AI engineering before "AI engineering" was a term.
- **["AI Engineering"](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)** — Chip Huyen again, newer, LLM-specific. The current best book on the subject.
- **["Hands-On Large Language Models"](https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/)** — Jay Alammar. Visual, intuitive, code-heavy. Great for the foundations.

## Communities

- **[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)** — best signal for local models, quantization, hardware questions.
- **[Anthropic Discord](https://www.anthropic.com/discord)** — Claude users, decent dev channels.
- **[Latent Space Discord](https://discord.gg/latent-space)** — the LS podcast community.
- **[Cursor forum](https://forum.cursor.com)** — workshop-relevant; bug reports and tips.

## Newsletters with high signal

- **[Import AI](https://importai.substack.com)** — Jack Clark (Anthropic policy). Weekly.
- **[The Batch](https://www.deeplearning.ai/the-batch/)** — Andrew Ng. Weekly digest.
- **[Last Week in AI](https://lastweekin.ai)** — broad weekly roundup.
- **[Ben's Bites](https://bensbites.beehiiv.com)** — daily, hype-heavy, useful as a tracker.

## YouTube channels worth subscribing to

- **[AI Explained](https://www.youtube.com/@aiexplained-official)** — measured, analytical, no hype.
- **[Yannic Kilcher](https://www.youtube.com/@YannicKilcher)** — paper deep-dives, dry humor.
- **[Sebastian Raschka](https://www.youtube.com/@SebastianRaschka)** — implementations from scratch, very clear.

## Things I'd skip

Twitter/X. Filter aggressively — the AI corner of X is 95% hype, 5% signal. Follow [@simonw](https://twitter.com/simonw), [@karpathy](https://twitter.com/karpathy), [@jeremyphoward](https://twitter.com/jeremyphoward), and a few specific people. Skip the rest.

LinkedIn AI content. Almost entirely slop. Treat it as a CRM, not a learning channel.

"Top 10 AI tools" listicles. They're all the same five tools you already know.

## A 30-day reading plan

If you want to seriously level up in a month:

**Week 1 — foundations.** Anthropic's interactive prompting tutorial + read 3 leaked system prompts.
**Week 2 — agents.** Read the ReAct paper + Lilian Weng's "LLM Powered Autonomous Agents" post.
**Week 3 — local models.** Install Ollama, try 4 different models on the same task, note differences.
**Week 4 — ship.** Pick one of your real problems and write a 100-line agent that solves it. Use what you wrote tonight as the base.

Good night and good shipping.
