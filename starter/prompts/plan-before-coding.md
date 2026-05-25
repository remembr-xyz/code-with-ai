# Prompt: Plan before coding

## Goal
Stop the AI from diving into code when the task isn't fully understood.

## Prompt

```
Before writing any code, give me your plan in this format:

1. WHAT you understand the task to be (in your words, one paragraph)
2. WHICH files you'll need to read first
3. WHICH files you expect to modify (with one line each on what changes)
4. WHAT could go wrong / what assumptions you're making
5. THE ORDER of operations

Wait for my confirmation before writing code.

Task: [PASTE TASK HERE]
```

## Why it works

- Surfaces misunderstandings *before* code is written, when fixes are free
- Forces the AI to identify reading dependencies (no skipping straight to writes)
- The "what could go wrong" line is gold — often catches edge cases you missed
- Trains the AI to ask, not assume, on any project where this is the default prompt
