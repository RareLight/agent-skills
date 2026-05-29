---
name: shipping-and-launch
description: Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy.
---

# Shipping and Launch

## Pre-Launch Gates
Prior to pushing any release to production, ensure these gates are complete:
- **Code**: Passing tests, clean builds, zero temporary debugging code (`console.log`, `print`), and proper error capture.
- **Security**: No hardcoded secrets, clean dependency audits, input validated at routes, and wildcard CORS rules eliminated.
- **Performance**: Standard DB query indexes, assets compressed, response latencies under target SLAs, and performance budgets met.
- **Accessibility**: Focus trapped in modals, contrast ratios meeting WCAG 2.1 AA, and zero axe-core or Lighthouse warnings.
- **Infrastructure**: Production config variables set, CDNs active, and server health checks returning 200.

## Observability & Alerting
- **Structured Logs**: Enforce JSON/structured logging using queryable properties (`order_id`, `duration_ms`), not strings.
- **RED Method**: Monitor Rate (requests), Errors (status codes), and Duration (latency) on all active endpoints.
- **Actionable Alerts**: Restrict paging alerts strictly to critical, actionable incidents (error rate >5%, service down). Match alerts with runbooks.

## Rollout Strategy
- **Feature Flag Lifecycle**: Deploy with flag OFF → Enable for internal testing → Canary rollout (5% → 25% → 50% → 100%) → Clean up flag and dead code paths within 2 weeks.
- **Canary Decision**: Advance only if error rates, latencies, and client JS errors remain within baseline margins. Hold or roll back if metrics spike.
- **Rollback Plan**: Document the explicit rollback command (`git revert <commit>`, rollback database migration, or flag override) and average recovery time.

## Verification Checklist
- [ ] All pre-launch gates are met and verified.
- [ ] Rollback steps, triggers, and timing are documented.
- [ ] Observability logs, metrics, and alerting rules are configured.
- [ ] Feature flags are wired with clear expiration and cleanup targets.
- [ ] Deployment health check is 200 and production error rates remain stable.
