---
name: ci-cd-and-automation
description: Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies.
---

# CI/CD and Automation

## Shift Left & Release Safely
- **Shift Left**: Enforce automated quality gates as early in the pipeline as possible. Move static analysis and type checks upstream of slow integration or E2E tests.
- **Continuous Integration**: Ensure no code merges without passing the strict order: Lint → Typecheck → Unit Tests → Build → Integration/E2E Tests → Security dependency audits.
- **Feature Flags**: Separate deployment from release. Deploy incomplete or high-risk features disabled behind toggle flags to support continuous, risk-free incremental delivery.
- **Deploy Previews & Rollbacks**: Trigger automated deploy previews for PR visual reviews. Maintain manual, immediate rollback triggers for rapid mitigation.

## Pipeline Optimization (Target <10m)
- **Dependency Caching**: Cache lock files and package dependencies within runner steps.
- **Parallelization**: Parallelize linting, typechecking, and testing phases.
- **Selective Triggers**: Use path-filtering to skip irrelevant workflows (e.g. skip E2E test runs for markdown-only changes).

## Environment and Secret Security
- **No Production Secrets in CI**: Never pass production secrets to CI environments. Store CI testing credentials strictly in repository actions secrets.
- **Example Environments**: Maintain a version-controlled, up-to-date `.env.example` template.

## Verification Checklist
- [ ] Quality gates (lint, typecheck, tests, build, dependency audit) are fully automated and block merges on failure.
- [ ] All pipelines trigger automatically on push and pull-request branches.
- [ ] Deployment workflows support a clear, instant rollback strategy.
- [ ] No hardcoded configuration credentials or secrets exist in pipeline configs.
- [ ] Total pipeline execution stays within acceptable optimized time limits (<10 minutes).
