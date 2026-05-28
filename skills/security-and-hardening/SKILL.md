---
name: security-and-hardening
description: Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when building any feature that accepts untrusted data, manages user sessions, or interacts with third-party services.
---

# Security and Hardening

## Boundary Rules

### Always Do (No Exceptions)
- **Boundary Validation**: Validate all external inputs at system boundaries (forms, API routes) using schema parsers (e.g., Zod, Pydantic).
- **Parameterized Queries**: Parameterize all database inputs. Never use string concatenation or interpolation for query variables.
- **Output Encoding**: Escape output to prevent XSS (rely on framework auto-escaping; don't bypass it).
- **Encrypted Storage**: Hash passwords using slow, adaptive algorithms (bcrypt, argon2) with ≥12 salt rounds.
- **Session Protection**: Set cookies to `httpOnly`, `secure`, and `sameSite: lax/strict`.
- **API Security Headers**: Ensure standard security headers are set (CSP, HSTS, X-Frame-Options).

### Ask First (Human Approval Required)
- Modifying authentication or authorization logic.
- Handling or saving new categories of PII or payment data.
- Introducing new third-party integrations, OAuth flows, or CORS rules.
- Implementing file upload endpoints.

### Never Do
- **Never commit secrets**, tokens, keys, or passwords. Check `git diff` before committing.
- **Never log sensitive data** (PII, credentials, cards, tokens).
- **Never trust client validation** as a secure boundary.
- **Never use `eval()`** or un-sanitized dynamic DOM insertion (`innerHTML`).
- **Never expose stack traces** or detailed backend exceptions in API responses.

## Input & Boundary Hardening
- **File Upload Safety**: Explicitly restrict upload mime-types, enforce maximum file sizes, and sanitize file names.
- **Rate Limiting**: Apply API rate limiting, using stricter throttling rules for auth and reset endpoints.
- **Vulnerability Audit**: Check dependencies for high/critical vulnerabilities via `npm audit` (or language equivalent) prior to release.

## Verification Checklist
- [ ] No secrets or tokens are in source code or git history.
- [ ] Inputs are validated using schemas at boundary entry points.
- [ ] Query builders/ORMs use parameterized values exclusively.
- [ ] Dependencies have no known high/critical vulnerabilities.
- [ ] Auth endpoints are throttled and protected.
- [ ] Backend stack traces are fully caught, logged internally, and sanitized for users.
