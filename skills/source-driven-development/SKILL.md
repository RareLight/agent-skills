---
name: source-driven-development
description: Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters.
---

# Source-Driven Development

## Objective
- **Grounding**: Eliminate hallucinated APIs, outdated syntaxes, and legacy patterns. Always back framework-specific decisions with official, version-accurate documentation.

## The SDD Sequence
1. **Detect Stack**: Parse the exact lock and dependency files (`package.json`, `Cargo.toml`, `pyproject.toml`) to identify precise framework versions before coding.
2. **Fetch Documentation**: Retrieve specific, authoritative documentation sections (homepage docs, official blog changelogs, web standards on MDN). Reject StackOverflow, blog tutorials, or AI summaries.
3. **Implement**: Write code conforming precisely to the version's API signatures. Surfacing conflicts immediately if existing project code violates official best practices.
4. **Cite**: Document every framework pattern with a full, deep-linked URL to its official source in both code comments and conversation summaries.

## Implementation Rules
- The `sdd-cache` hook (`hooks/SDD-CACHE.md`) caches fetched documentation with HTTP revalidation — avoids redundant fetches without weakening freshness guarantees.
- If official documentation is unreachable, annotate logic with `UNVERIFIED: based on memory/training data, verify before production.`

## Verification Checklist
- [ ] Framework and library versions are verified from dependencies.
- [ ] Specific documentation pages are fetched and validated.
- [ ] Code avoids deprecated patterns or mismatched signatures.
- [ ] Implementations include deep-linked source URLs in comments.
