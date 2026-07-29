# Routing Fixtures

| Request | Expected routing | Minimum evidence |
|---|---|---|
| Fix a typo in a README | Fast path | Readback or markdown check |
| Fix a localized bug | `debugging-and-error-recovery` + targeted test | Reproduction or focused test |
| Add a public endpoint | `api-and-interface-design` + proportional spec + tests | Contract and boundary tests |
| Change a database schema | `planning-and-task-breakdown` + `deprecation-and-migration` + compatibility review | Migration/rollback evidence |
| Modify a UI flow | `frontend-ui-engineering` + browser fallback | UI test or stated runtime gap |
| Diagnose a production incident | `debugging-and-error-recovery` + authority model | Reproduction, scope, mitigation |
| Work without shell/browser tools | Applicable skills with fallbacks | Static evidence and explicit gaps |
