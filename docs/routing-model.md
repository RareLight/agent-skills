# Skill Routing Model

Choose skills by task conditions, not a mandatory lifecycle. A skill's frontmatter states its trigger, skip conditions, risk, required capabilities, and fallback.

## Routing order

1. Apply the portable core and repository rules.
2. Classify the requested change as maintenance, behavior change, public/irreversible change, incident, review, or release work.
3. Select the smallest set of skills whose conditions apply. Prefer the maintenance fast path for a localized, reversible change with clear acceptance criteria.
4. Escalate to discovery, specification, security, migration, or release workflows only when the task's risk signals require them.
5. Record the selected verification and any unavailable-capability gap in the final handoff.

## Fast path

For a typo, isolated documentation update, formatting change, or clear localized bug fix: inspect the target and nearby tests, make the scoped change, run the narrowest relevant check, and report the result. A full spec, plan, approval gate, or commit is not required unless project policy says otherwise.

## Delegation

Delegate an independent, bounded investigation when it has a clear output and no shared-write conflict. Use isolated workspaces for concurrent writers. A single specialist is valid when it reduces risk; fan out only when the investigations are genuinely independent.
