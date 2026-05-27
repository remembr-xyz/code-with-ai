# Contributing

Thanks for reading. This repo is a living workshop kit — corrections, better examples, and new resources are welcome.

## What's most useful

### Corrections
- Broken or moved links (especially in [`starter/examples/`](starter/examples/) — those are dated and may go stale)
- Factual errors in [`resources/safeguards.md`](resources/safeguards.md) (incident details, OWASP wording)
- MCP server commands that no longer work as written

### Additions worth submitting
- **New real-world AGENTS.md examples** — must be in a public repo, verified to exist, with a one-paragraph annotation of *what's worth learning* from it (not just a summary)
- **New `.cursor/rules/*.mdc` patterns from production repos** — same bar
- **New documented agent incidents** with reputable sources (Fortune, Reuters, The Register, Tom's Hardware, AWS Security Bulletins, AI Incident Database). Postmortems welcome.
- **Translations** — particularly Section-6-Guardrails-style examples in non-English contexts

### What we'd rather not have
- Fictional/invented examples. The whole point of the gallery is grounded inspiration.
- "Promotional" entries (your own tool/SaaS without independent adoption evidence)
- Generic tips that aren't actionable
- Anything that lengthens a file past ~250 lines without splitting it

## How

```bash
gh repo fork remembr-xyz/code-with-ai --clone
cd code-with-ai
git checkout -b your-improvement
# make changes
git commit -m "Add: openai/codex AGENTS.md to gallery"
gh pr create
```

Open a PR. Small ones are easier to merge. If you're adding to the inspiration gallery, please include:
- The exact verified URL (with the path inside the repo, not just the repo root)
- File size at time of verification
- Date verified (e.g., "Verified 2026-05-26")

## Voice and style

Keep it terse and opinionated. The repo's voice is direct — short sentences, real examples, no marketing language. If your contribution reads like a brochure, it'll get edited.

## License

MIT. By contributing you agree your work is licensed the same way.

## Maintainer

[Kanishk Patel](https://x.com/above_almighty) · [Founsi AI](https://founsi.ai) · [Learn Agentic AI](https://learnagentic.substack.com)
