# Figma experiments — full app designs

> **TL;DR** Clone a Figma design, point the Figma MCP at it, watch a real model turn it into code. For the MCP setup itself, see [`../starter/examples/mcp/figma.md`](../starter/examples/mcp/figma.md) — two paths (Figma Desktop's Dev Mode MCP, or the Framelink npm package).

Free, complete application designs you can clone into your Figma account, then point Cursor's Figma MCP at and turn into real code.

These are **full applications**, not component libraries. The point is to feel what it's like to convert a real multi-screen design into a working codebase via MCP — and to compare what different models (Claude, GPT-5, local Ollama) produce from the same input.

## The experiment

1. Pick a design from the list below. Click "Get a copy" in Figma Community to clone it into your account.
2. Set up the Figma MCP in Cursor (see [`labs/02-mcp.md`](../labs/02-mcp.md) or appendix slide A7).
3. Pick **one frame** to start with — don't try the whole app at once.
4. Run this prompt in Cursor: *"Using the Figma tool, fetch frame [URL] and write a React + Tailwind component matching the layout exactly. Semantic HTML. Aria labels. Output the full file."*
5. Repeat with three models (Claude Sonnet 4.6 → GPT-5 → local Qwen 2.5 Coder via Ollama). Compare outputs.

The goal isn't perfection. The goal is **felt experience of how different models interpret the same design**.

## Starter (single-screen, ~5 minutes)

Best first conversion. One screen, clear structure, immediate satisfaction.

- **[Chatia — AI Chatbot Mobile App](https://www.figma.com/community/file/1444053668130495114/chatia-ai-chatbot-mobile-app-ui-ux-design-template-free-landing-page)** — clean mobile chatbot landing page. Single hero frame, ~6 components.
- **[SaaS Template by Flowbase.co](https://www.figma.com/community/file/877750883399287145/saas-template-by-flowbase-co)** — free SaaS landing page. Hero, features, pricing, footer.
- **[Customizable AI Chat Interface UI](https://www.figma.com/community/file/1373386017446585785/customizable-ai-chat-interface-ui-design-for-mobile-and-web-applications-free-download)** — both mobile and web chat surfaces; pick one screen.

## Intermediate (multi-screen app, ~15 minutes)

A small app with 3–6 screens. Real navigation, real state, real layouts.

- **[BrainBox AI Chatbot App — Full UI Kit](https://www.figma.com/community/file/1316069776447695879/brainbox-ai-chatbot-mobile-app-full-100-free-ui-kit)** — complete chatbot mobile app. Onboarding → chat → settings.
- **[Chat App — Free Template](https://www.figma.com/community/file/1213614322696245886/chat-app-free-template)** — multi-screen mobile chat app, end-to-end.
- **[3 Free AI Chatbot App UI Kits](https://www.figma.com/community/file/1393822153168458311/3-free-ai-chatbot-app-ui-kit)** — three full app designs in one file. Pick whichever appeals.
- **[AI Assistant Chat](https://www.figma.com/community/file/1459358248758159568/ai-assistant-chat)** — production-quality AI assistant interface.
- **[Fintech App — Onboarding + Dashboard](https://www.figma.com/community/file/1358062299850660607/fintech-app-onboarding-and-dashboard)** — onboarding flow + main dashboard. Banking-app feel.

## Ambitious (full SaaS dashboard, ~30 minutes)

Multi-section, multi-screen apps with charts, tables, sidebars, modals. Real productivity-app surface area.

- **[SaaS Dashboard UI Kit (Free)](https://www.figma.com/community/file/1633880935746848529/saas-dashboard-ui-kit)** — full production-ready SaaS dashboard. Auth, dashboard, settings, billing, all wired together.
- **[Glass SaaS Dashboard](https://www.figma.com/community/file/1633077830104049751/glass-saas-dashboard-free-figma-ui-kit-design-system)** — modern glassmorphism dashboard. Analytics, charts, admin panels.
- **[SaaS Dashboard UI Kit (Free, alt)](https://www.figma.com/community/file/1561384239599771178/saas-dashboard-ui-kit-free)** — clean responsive SaaS dashboard, light + dark mode.
- **[SAAS Dashboard](https://www.figma.com/community/file/1065510379888107603/saas-dashboard)** — popular community classic. Lots of screens.
- **[Fintech + CRM Web and Mobile Dashboards](https://www.figma.com/community/file/1224435883167876912/fintech-crm-web-and-mobile-app-dashboards)** — both web and mobile versions of the same app. Compare how the AI handles cross-platform.
- **[Fintech SaaS Dashboard](https://www.figma.com/community/file/1384108568079688147/fintech-saas-dashboard-design)** — investment/banking-style dashboard with charts.

## Find more by category

Figma Community has dedicated browse pages — bookmark these and filter by "Free":

- **[Dashboards](https://www.figma.com/community/website-templates/dashboards)** — every dashboard template, sortable.
- **[Mobile chat apps](https://www.figma.com/community/mobile-apps/chat)** — every chat-app template.
- **[Chatbot templates](https://www.figma.com/community/website-templates/chatbots)** — chat UI / AI assistant designs.
- **[Mobile finance apps](https://www.figma.com/community/mobile-apps/finance)** — fintech and banking apps.
- **[SaaS sites](https://www.figma.com/community/tag/saas/files)** — SaaS landing pages and product surfaces.
- **[Figma Templates Hub](https://www.figma.com/templates/dashboard-designs/)** — Figma's own curated template library.

## The "compare three models" exercise

Pick **one** frame. Don't change anything else. Run this prompt:

> *"Using the Figma tool, fetch frame [PASTE FIGMA URL].*
> *Write a single React component (Tailwind, no other dependencies) that matches the layout exactly.*
> *Use semantic HTML. Add aria labels where appropriate.*
> *Output the full file ready to drop into a Next.js project."*

Run it with each:

| Model | What to notice |
|-------|----------------|
| **Claude Sonnet 4.6** | Tends thorough and opinionated. Strong on accessibility. Often adds extra structural divs. |
| **GPT-5** | Cleaner structure, sometimes terser. Good at exact spacing. |
| **Local Qwen 2.5 Coder 7B (Ollama)** | More literal. May miss subtle tokens. Watch for hallucinated Tailwind classes. |

Score each output on:

- **Layout fidelity** — did it match the design 1:1?
- **Code quality** — clean, readable, idiomatic React?
- **Accessibility** — semantic HTML, aria labels, keyboard nav?
- **Design system match** — used the colors and spacing from Figma, or invented its own?
- **Hallucinations** — references to libraries/components that don't exist?

Most students leave thinking "Claude is best." Run this experiment with the same design and a 1–5 score per criterion. You'll have a real opinion grounded in actual diffs, not vibes.

## Workflow: Cursor + Figma MCP step by step

1. **Get a Figma personal access token** — Figma → Settings → Account → Personal access tokens → Generate (scope: "File content: read").
2. **Add the Figma MCP server to Cursor** — full snippet in appendix slide A7 of the workshop deck, or `mcp.json` example below.
3. **Clone a design** from the lists above into your Figma account.
4. **Grab the frame URL** — right-click any frame in Figma → Copy link.
5. **Paste into Cursor chat** with a conversion prompt.

```json
"figma": {
  "command": "npx",
  "args": ["-y", "figma-developer-mcp", "--stdio"],
  "env": { "FIGMA_API_KEY": "figd_..." }
}
```

## Beyond Figma — open-source alternatives

- **[Penpot](https://penpot.app)** — fully open-source design tool, web-based, imports Figma files. There's an emerging Penpot MCP at [github.com/penpot/penpot-mcp](https://github.com/penpot/penpot-mcp).
- **[Figma Dev Mode MCP](https://help.figma.com/hc/en-us/articles/32132100833559)** — Figma's first-party MCP server (2025). More polished but more setup; the community `figma-developer-mcp` we use in the workshop is faster to get started with.

## Share back

If you run the three-model experiment with one of these designs, **post the diffs**. Tag [@above_almighty](https://x.com/above_almighty) on X or open a PR adding `experiments/<design-name>.md` to this repo. The repo will collect a comparison archive over time.

Sources:
- [Figma Community — Dashboards](https://www.figma.com/community/website-templates/dashboards)
- [Figma Community — Chat apps](https://www.figma.com/community/mobile-apps/chat)
- [Figma Community — Chatbots](https://www.figma.com/community/website-templates/chatbots)
- [Figma Community — Finance apps](https://www.figma.com/community/mobile-apps/finance)
