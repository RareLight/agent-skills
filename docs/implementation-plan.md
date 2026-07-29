# Portable Skill-Pack Migration Plan

## Objective

Convert the pack from a harness-specific, lifecycle-mandatory prompt set into a portable, capability-aware set of risk-tiered workflows.

## Scope and success criteria

- Universal instructions contain no vendor, tool, path, or language dependency.
- Each skill has explicit activation, skip, capability, and fallback guidance.
- Small maintenance tasks have a documented fast path.
- Sensitive and external actions retain clear approval boundaries.
- Validation detects malformed metadata, broken skill references, and portable-content leakage.

## Implementation slices

1. Add portable core, routing model, adapters, and validation fixtures.
2. Replace the global prompt and meta-router.
3. Migrate lifecycle and domain skills to conditional, proportional rules.
4. Update personas, installation documentation, and repository index.
5. Run metadata, link, leakage, and fixture validation.

## Verification

Run `python3 scripts/validate-skills.py` and `python3 scripts/validate-routing-fixtures.py`. Review the fixture matrix in `docs/routing-fixtures.md` and run `python3 ./install --dry-run` before distribution.
