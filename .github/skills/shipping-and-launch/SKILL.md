---
name: shipping-and-launch
description: Prepares a production-affecting release with proportionate operational safeguards. Use for deployment, staged rollout, or launch readiness work.
applies_when: A change can affect production users, data, cost, or availability.
skip_when: The task does not include a production-affecting release.
risk: high
requires: [deployment-context]
fallback: Produce a release-readiness assessment and state unavailable operational checks.
outputs: [release-plan, rollback-plan, launch-evidence]
related_skills: []
---

# Shipping and Launch

1. Confirm release authority, changed risk, validation evidence, observability, and rollback/mitigation path.
2. Choose direct, staged, flagged, or canary rollout based on blast radius and available controls.
3. Monitor the metrics and signals that represent the change’s actual service objective; do not require irrelevant web, alerting, or feature-flag infrastructure.
4. Stop or roll back on defined adverse signals and record follow-up work.

## Verification checklist

- [ ] Release authority and rollback path are explicit.
- [ ] Operational checks match the actual risk and environment.
