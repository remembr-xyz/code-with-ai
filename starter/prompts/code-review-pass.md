# Prompt: Code review pass

## Goal
Get a thorough self-review on a diff *before* you open the PR.

## Prompt

```
Review the current diff (what's staged or unstaged in git) as if you
were a senior engineer who didn't write it.

Cover, in this order:

1. CORRECTNESS — does it actually do what the task asked for?
2. EDGE CASES — what inputs would break it?
3. SECURITY — any inputs not validated, secrets logged, SQL/shell built
   by string concat, etc.?
4. PERFORMANCE — anything obviously O(n²) when it could be O(n)?
5. READABILITY — names, comments, structure
6. TESTS — are the new cases covered? Are there missing edge tests?

For each section, list issues as: [SEVERITY] short description.
Severity = blocker / important / nit.

Then summarize: ship it / fix the blockers first / rethink the approach.
```

## Why it works

- The senior-engineer framing produces sharper criticism than "review this"
- Six categories in fixed order = nothing gets skipped
- Severity labels separate "must fix" from "nice to fix" — actionable
- The summary line forces a verdict instead of a wishy-washy "looks pretty good"
