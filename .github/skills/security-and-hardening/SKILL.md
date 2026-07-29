---
name: security-and-hardening
description: Identifies and mitigates security risks at trust boundaries. Use for untrusted input, authentication, authorization, sensitive data, external integrations, or security review.
applies_when: The change crosses a trust boundary or changes security posture.
skip_when: The change cannot affect a trust boundary and no security-relevant dependency or configuration changes.
risk: high
requires: [repository-read]
fallback: Perform static boundary review and state unavailable audit tools or environment gaps.
outputs: [threat-notes, mitigations, security-evidence]
related_skills: []
---

# Security and Hardening

1. Identify assets, trust boundaries, attackers, and the authorization level required by the portable core.
2. Validate untrusted input at boundaries; use parameterized queries, framework-safe output handling, least privilege, and safe secret handling.
3. Review authentication, authorization, PII, uploads, OAuth/CORS, and destructive operations as high-authority changes.
4. Add rate limits, secure session settings, headers, dependency review, and error sanitization where the system and threat model require them.
5. Do not log or commit secrets, trust client-side validation, expose sensitive diagnostics, or weaken controls without an approved compensating design.

## Verification checklist

- [ ] Affected trust boundaries and mitigations are identified.
- [ ] Sensitive or destructive scope had explicit authority.
- [ ] Available security checks were run or their absence is reported.
