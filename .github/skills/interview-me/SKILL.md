---
name: interview-me
description: Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence about the underlying intent. Use when an ask is underspecified ("build me X" without "for whom" or "why now"), when the user explicitly invokes ("interview me", "grill me", "are we sure?", "stress-test my thinking"), or when you catch yourself silently filling in ambiguous requirements before any plan, spec, or code exists.
---

# Interview Me

## Objective & Posture
- **Target-Intent Extraction**: Clarify underspecified, conventional requests ("build a dashboard", "make it faster") before writing any code or plans.
- **Interactive Requirement**: Use ONLY in interactive sessions. For non-interactive contexts (CI, autonomous loops), flag missing requirements as blockers instead of guessing.

## The Interview Cycle
1. **Hypothesize & Score**: State your best guess of the user's intent in one sentence, with an explicit confidence score (0-100%). List the exact missing elements if confidence is <70%.
2. **One Question at a Time**: Never batch questions. Ask exactly one focused question per turn, attaching your explicit hypothesis/guess to give the user a target to react to.
3. **Probing Conventions**: Push past generic buzzwords ("modern", "scalable", "clean"). If the user signals standard best-practices, probe directly: *"If you didn't have to justify this, what would you actually want?"*
4. **Structured Restate**: Synthesize the confirmed intent using a standard, 6-line format: Outcome / User / Why Now / Success / Constraint / Out of scope.
5. **Strict Yes-Gate**: Obtain an explicit, unambiguous "Yes" before proceeding. Vague approvals ("sounds good", "whatever you think") are not valid yes-gates.

## Stop Condition
- Terminate the interview once you can confidently predict the user's reaction to the next three questions you would ask.

## Verification Checklist
- [ ] Initial hypothesis is stated alongside a confidence score and missing-detail list.
- [ ] Questions are sent strictly one-by-one with guesses attached.
- [ ] Final restatement covers explicit Out of Scope boundaries.
- [ ] The user gave an explicit, active "Yes" to the restatement.
- [ ] Confirmed intent is saved to `docs/intent/[topic].md` upon confirmation.
