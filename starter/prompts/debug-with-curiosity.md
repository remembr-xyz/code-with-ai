# Prompt: Debug with curiosity

## Goal
Replace "find the bug" (which makes the AI guess) with structured investigation.

## Prompt

```
Something's wrong. Here's what I'm seeing:

[PASTE: error message, unexpected output, or symptom]

Steps I want you to take:

1. Form 2-3 hypotheses about what could cause this. Rank them by
   likelihood, briefly justifying each.
2. For the top hypothesis, tell me which files you'd read to confirm
   or rule it out — don't read them yet.
3. Wait for me to say "go" before reading anything or proposing a fix.

Do NOT immediately suggest a one-line patch. We're investigating first.
```

## Why it works

- The "form hypotheses first" pattern is how good engineers actually debug
- Ranking forces the AI to commit to a guess rather than vaguely list possibilities
- "Don't read them yet" is the killer line — it makes you the orchestrator, not the autocomplete victim
- You'll often find the bug yourself just from the AI's hypothesis list
