# Acceptance matrix

Assess each row as `VERIFIED`, `OBSERVED`, `NOT_RECOLLECTED`, or `FAIL`:

| Area | Required evidence |
|---|---|
| SERVER_BASELINE | OS/resources/route/DNS/time/services/listeners |
| REGION_PATH | contamination-aware current path evidence |
| CONTROL_PLANE | persistent/generated/runtime relationship |
| TRANSPORT | bounded observed traffic |
| SERVER_ROUTING | intended and negative isolation |
| SUBSCRIPTION | status, content, parse, semantics |
| CLIENT_PARSE | active runtime contains intended nodes |
| TUN | runtime adapter/routes where required |
| DNS | ownership and observed resolution behavior |
| CLIENT_ROUTING | fresh connection rule/chain evidence |
| EXIT | protected expected-exit comparison |
| FAIL_CLOSED | structural verification by default |
| ROLLBACK | complete, usable, independent where needed |

Define which rows are blocking for the requested platform/topology before evaluating them.
