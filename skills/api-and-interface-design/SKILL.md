---
name: api-and-interface-design
description: Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or establishing boundaries between frontend and backend.
---

# API and Interface Design

## Core Design Principles
- **Hyrum's Law**: Every observable public behavior—undocumented quirks, error text, ordering, timing—becomes a de facto contract once users depend on it. Expose only what is intentional; conceal implementation details.
- **One-Version Rule**: Avoid forcing consumers to select between multiple concurrent versions of the same API. Design for continuous, backward-compatible extension rather than hard forks.
- **Contract First**: Define public interfaces and types (schemas, component prop shapes, interfaces) before starting implementation.
- **Consistent Error Semantics**: Adopt a single unified error response structure across the entire application (e.g., HTTP status code mapping with structured machine-readable error codes).

## REST & TypeScript Patterns
- **Noun-Based Resources**: Name endpoints using plural nouns and standard HTTP methods: `GET /api/tasks`, `POST /api/tasks`, `PATCH /api/tasks/:id` (for partial updates), `DELETE /api/tasks/:id` (idempotent).
- **Filtering & Pagination**: Always support pagination (`page`/`pageSize` query params) on list queries.
- **Validation Boundaries**: Enforce strict validation (e.g., using schema parsers like Zod/Pydantic) exclusively at the boundaries of untrusted inputs (user forms, API inputs, external service payloads). Internal modules should rely on established type contracts.
- **Separation of Input/Output**: Declare explicit, separate interfaces for caller inputs (`CreateTaskInput`) and system outputs (`Task` containing database generated fields).

## Verification Checklist
- [ ] Every API endpoint has strict, typed input and output validation schemas.
- [ ] List queries support standardized pagination.
- [ ] All errors return a consistent, structured format.
- [ ] New changes are backward-compatible (additive and optional).
- [ ] Third-party service payloads are treated as untrusted and validated at entry boundaries.
