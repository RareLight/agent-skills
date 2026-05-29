---
name: deprecation-and-migration
description: Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when deciding whether to maintain or sunset existing code.
---

# Deprecation and Migration

## Core Sunsetting Rules
- **Code is Liability**: Every active line of code incurs cost (maintenance, security, cognitive drift). Prioritize deletion of unused features, redundant API versions, and zombie code.
- **The Churn Rule**: If you own the infrastructure being deprecated, you are responsible for either migrating your users or providing fully backward-compatible shims. Never announce deprecation and expect clients to figure it out alone.
- **No Deprecation without Alternatives**: Do not sunset an active service without a production-ready, fully documented replacement that covers all critical client use cases.

## Sunset Decision Framework
1. **Uniqueness**: Does this system provide unique, un-replicated value? If yes, maintain it.
2. **Scope**: How many active consumers rely on it?
3. **Migration Cost**: Balance migration efforts against the 2-3 year ongoing cost of maintaining the legacy platform.
4. **Security & Obsolescence**: Does keeping the code introduce security risks or block major architectural upgrades?

## Migration Patterns
- **Strangler Pattern**: Route traffic incrementally from the old platform to the new platform (e.g. Canary 10% → 50% → 100%) and sunset the idle system.
- **Adapter Pattern**: Wrap the new implementation inside the old interface so client code requires zero modification during backend migration.
- **Feature Flag Migration**: Guard the execution paths behind feature flags, transitioning users incrementally based on ID properties or environments.

## Verification Checklist
- [ ] Replacement service is production-hardened and covers all target legacy use cases.
- [ ] Backward-compatible adapters or automated codemod migrations are provided.
- [ ] Production logs and metrics confirm zero traffic remains on the deprecated service.
- [ ] Legacy code, files, dependencies, tests, and configuration blocks are completely deleted.
