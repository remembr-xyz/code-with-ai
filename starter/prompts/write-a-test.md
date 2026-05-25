# Prompt: Write a test

## Goal
Get tests that actually exercise the function, not happy-path stubs.

## Prompt

```
Write tests for this function:

[PASTE: function signature + docstring, or path to file]

Cover these cases, in this order:
1. The happy path — typical valid input
2. Edge cases — empty input, None, zero, single element, max size
3. Error cases — invalid types, out-of-range values, malformed input
4. The boring case I always forget — [e.g., Unicode, leap years, timezones]

Constraints:
- One test per case. Name them test_<function>_<scenario>.
- Use pytest. No mocks unless I tell you which dependency to mock.
- If a case is impossible to test cleanly, say so — don't fake it.

Show me the tests, then run them and show the output.
```

## Why it works

- Forces structured coverage instead of "I wrote three tests, looks good"
- The fourth bullet is project-specific — fill in your domain's classic landmine
- Naming convention keeps the test suite navigable
- The "if impossible, say so" line prevents fake-passing tests
