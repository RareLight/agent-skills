---
name: performance-optimization
description: Optimizes application performance. Use when performance requirements exist, when you suspect performance regressions, or when Core Web Vitals or load times need improvement. Use when profiling reveals bottlenecks that need fixing.
---

# Performance Optimization

## Core Workflow
1. **Measure**: Gather baseline metrics. Establish synthetic (Lighthouse, DevTools) and real-user benchmarks.
2. **Identify**: Isolate the actual bottleneck from profiling data (don't guess).
3. **Fix**: Address the specific root bottleneck using proven patterns.
4. **Verify**: Re-measure under identical conditions to prove improvement.
5. **Guard**: Integrate performance checks or size budgets into CI to prevent regressions.

## Core Web Vitals Targets
- **LCP** (Largest Contentful Paint): ≤ 2.5s
- **INP** (Interaction to Next Paint): ≤ 200ms
- **CLS** (Cumulative Layout Shift): ≤ 0.1

## Common Performance Patterns
- **Database Optimization**: Prevent N+1 queries by using JOINs or eager loading (`include` / `select_related`). Apply missing indexes to frequently queried fields. Paginate lists.
- **Frontend Assets**: Provide explicit `width`/`height` dimensions for images to avoid CLS. Compress and lazy-load below-the-fold media.
- **Bundle Optimization**: Use lazy loading (`React.lazy`, dynamic `import()`) for heavy components and routes. Verify bundle budgets in CI.
- **DOM & Threading**: Batch DOM writes inside `requestAnimationFrame`. Debounce expensive scroll/resize event handlers. Avoid blocking the async backend event loop with sync operations.
- **Caching Strategy**: Cache slow, static, or rarely modified calculations. Employ robust `Cache-Control` headers.

## Verification Checklist
- [ ] Profiling baseline is recorded and contrasted with post-fix timing (with specific numbers).
- [ ] The true bottleneck has been identified and corrected.
- [ ] No N+1 queries or un-paginated requests have been added.
- [ ] Core Web Vitals are within "Good" bounds.
- [ ] Existing functionality and test cases are fully preserved.
