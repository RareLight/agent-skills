---
name: test-driven-development
description: Uses focused tests to specify and verify behavior changes. Use for logic changes, bug fixes, and behavior whose regression risk is best captured by automated tests.
applies_when: A meaningful behavior can be reliably exercised by a test.
skip_when: The change is documentation, formatting, generated output, or a test would add less evidence than another reliable check.
risk: medium
requires: [test-runner]
fallback: Use the most reliable available verification and explain why an automated test was not added.
outputs: [behavioral-test-or-alternative-evidence]
related_skills: []
---

# Test-Driven Development

1. Identify the observable behavior and the narrowest test level that proves it.
2. For reproducible bugs, create a failing reproduction before the fix when practical.
3. Implement the minimal change, then run the focused test and relevant adjacent checks.
4. Use broader suites for integration boundaries, release gates, or elevated regression risk.
5. Test outcomes rather than internals; isolate state and mock external boundaries deliberately.

## Verification checklist

- [ ] Modified behavior has automated evidence or a documented alternative.
- [ ] Bug reproduction was added when practical and valuable.
- [ ] Test scope and execution evidence are reported accurately.
