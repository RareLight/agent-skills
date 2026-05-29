---
name: documentation-and-adrs
description: Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase.
---

# Documentation and ADRs

## Core Guidelines
- **Document the "Why"**: Capture context, trade-offs, constraints, and rejected alternatives. Code represents *what* was built; documentation details *why*.
- **Omit Obvious Explanations**: Never write comments that restate what the code clearly says.
- **No Dead Code / TODOs**: Delete dead code (git retains history). Do not leave TODO comments for immediate requirements—write the code now.

## Architecture Decision Records (ADRs)
- **When to Write**: Choose of databases/ORMs, framework stacks, API formats, authentication schemas, or any choice expensive to reverse.
- **Structure**: Record sequentially in `docs/decisions/` containing: Title, Status (Proposed/Accepted/Superseded), Context, Decision, Alternatives Considered, Consequences.
- **Immutability**: Never edit or delete accepted ADRs. If a decision changes, submit a new ADR that explicitly references and supersedes the old one.

## Code & API Documentation
- **Type-Level Docs**: Annotate public components, interfaces, and API endpoints directly in-code using JSDoc/Docstrings with params, return signatures, and illustrative usage examples.
- **Project Index**: Maintain a clean `README.md` covering: Core Purpose, Quick Start (installation, environment template, dev triggers), Commands Table, and Architecture Map.

## Verification Checklist
- [ ] ADR is recorded and accepted for every significant architectural deviation.
- [ ] Public API signatures and types are documented inline.
- [ ] README covers local setup and execution commands accurately.
- [ ] Commented-out code and obsolete/speculative notes are fully expunged.
