---
name: ci-cd-and-automation
description: Designs reliable, secure automation for build, test, delivery, and operational checks. Use when creating or changing CI/CD workflows.
applies_when: The task changes automated validation, deployment, or release controls.
skip_when: No automation or delivery workflow is affected.
risk: high
requires: [ci-context]
fallback: Validate configuration statically and document unavailable CI execution.
outputs: [pipeline-change, quality-gates, rollback-notes]
related_skills: []
---

# CI/CD and Automation

1. Identify repository policy, risk, secrets boundaries, and the delivery target.
2. Automate the highest-value checks early; order and parallelize work based on dependency and cost.
3. Use caching, selective triggers, previews, flags, and rollback mechanisms when they serve the project’s delivery model.
4. Keep production secrets out of untrusted CI contexts and validate configuration before enabling it.

## Verification checklist

- [ ] Quality gates match project risk and supported tooling.
- [ ] Secrets and deployment authority are appropriately constrained.
- [ ] Rollback or mitigation is defined for production-affecting workflows.
