---
name: performance-optimization
description: Improves measured performance bottlenecks without regressing behavior. Use when performance is a requirement, a regression is observed, or profiling identifies a bottleneck.
applies_when: A measurable performance concern or budget exists.
skip_when: No performance objective, regression, or evidence of a bottleneck exists.
risk: medium
requires: [profiling-tools-optional]
fallback: Use available timing, query, bundle, or static evidence and state measurement limits.
outputs: [baseline, change, post-change-evidence]
---

# Performance Optimization

1. Define the user or system metric, workload, and baseline.
2. Identify the bottleneck with profiling or the strongest available evidence; do not optimize by stereotype.
3. Apply the smallest change that addresses it and preserve semantics.
4. Re-measure under comparable conditions and add a budget or regression guard when cost-effective.

## Verification checklist

- [ ] Baseline and post-change evidence are comparable.
- [ ] The chosen optimization addresses an identified bottleneck.
- [ ] Applicable project budgets, not universal web metrics, are respected.
