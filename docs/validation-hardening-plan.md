# Validation and Distribution Hardening Plan

## 1. Establish source and generated-artifact ownership

- [x] Treat `skills/` and `GLOBAL-PROMPT.md` as canonical sources.
- [x] Keep tracked Copilot outputs synchronized as generated artifacts until a future removal migration.
- [x] Add a drift check that compares canonical inputs with tracked generated outputs.
- [x] Document the synchronization command and run it before release.

## 2. Make skill validation schema-aware

- [x] Parse the constrained frontmatter format strictly.
- [x] Require non-empty scalar fields, valid skill names, risk values, and list-valued capability fields.
- [x] Require and validate explicit `related_skills` metadata.
- [x] Reject missing/empty skill directories and portable harness leakage.

## 3. Make routing fixtures executable data

- [x] Add a machine-readable routing manifest and fixtures.
- [x] Validate fixture schema, known task classes, required skills, and non-empty evidence.
- [x] Keep the Markdown fixture table as human-facing documentation generated from the same intent.

## 4. Harden distribution

- [x] Run validators before any installer write, including dry-runs.
- [x] Fail on invalid source or copy failure; do not claim partial success.
- [x] Stage directory and file replacements with a recoverable backup.
- [x] Add an installed-layout smoke test.

## 5. Isolate harness-specific hooks

- [x] Move Claude-specific hook guidance under a Claude adapter.
- [x] Make hook installation opt-in and resolve the meta-skill path explicitly.
- [x] Test the hook against both repository and installed layouts.

## 6. Update published guidance and verify

- [x] Update contribution and setup documentation to the portable routing model.
- [x] Synchronize tracked generated artifacts.
- [x] Run schema, routing, drift, installer, hook, and whitespace checks.
