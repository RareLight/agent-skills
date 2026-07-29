---
name: source-driven-development
description: Verifies unfamiliar or version-sensitive implementation decisions against authoritative sources. Use for unstable APIs, security-sensitive integrations, or when local evidence is insufficient.
applies_when: Correctness depends on external API, standard, or dependency behavior that is uncertain or version-sensitive.
skip_when: Existing project code, tests, and stable local contracts provide sufficient evidence.
risk: medium
requires: [dependency-metadata, network-optional]
fallback: Identify the precise unverified assumption and avoid claiming source verification.
outputs: [version-evidence, source-notes-or-gap]
---

# Source-Driven Development

1. Identify the exact dependency or standard version from local metadata.
2. Consult authoritative version-appropriate sources when available and necessary.
3. Prefer existing project conventions unless they conflict with a verified requirement.
4. Record source links in the change summary, ADR, or user-facing handoff when they materially support a decision; do not add routine documentation URLs to code comments.
5. When sources are unavailable, use conservative local evidence and label the remaining uncertainty.

## Verification checklist

- [ ] The external dependency and version are identified when relevant.
- [ ] Source claims are accurate and scoped.
- [ ] Unavailable-source gaps are explicit.
