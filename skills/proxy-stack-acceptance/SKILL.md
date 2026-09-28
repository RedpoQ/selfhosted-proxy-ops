---
name: proxy-stack-acceptance
description: Perform end-to-end proxy-stack acceptance, classify functional readiness separately from security hardening, identify blocking and non-blocking gaps, verify rollback, and freeze accepted systems until new evidence appears.
---

# Proxy stack acceptance

## Purpose

Turn current evidence into a bounded readiness and freeze decision.

## When to use

Use after implementation/integration, during release readiness, or when asked whether further tuning is justified. Do not use historical deployment success as current health without recollection.

## Preconditions

Known intended topology, current source-of-truth evidence, acceptance requirements, and rollback expectations.

## Workflow

1. Read [acceptance matrix](references/acceptance-matrix.md).
2. Evaluate server baseline, region path, control plane, transport, routing, subscription, client parse, TUN, DNS, client routing, exit, fail-closed, and rollback.
3. Classify missing evidence with [security separation](references/security-separation.md) as `BLOCKING_GAP` or `NON_BLOCKING_GAP`.
4. Apply the [freeze rule](references/freeze-rule.md).

## Decision gates

`FUNCTIONAL_READY != SECURITY_HARDENED`. A missing unrequested platform adapter need not block readiness for a validated platform. A blocking runtime or rollback gap does.

## Mutations

- **Allowed:** read-only verification by default.
- **Prohibited:** tuning to fill a report, destructive fail-closed testing, declaring security from functionality, and silently converting unknowns to PASS.

## STOP conditions

Current host/profile identity mismatch, stale evidence for a blocking row, unverified rollback, secret exposure, or new failure evidence.

## Evidence requirements

Use `VERIFIED`, `OBSERVED`, `NOT_RECOLLECTED`, or `FAIL` per row. Security status is only `VERIFIED`, `PARTIAL`, `DEFERRED`, or `UNKNOWN`.

## Output contract

```text
FUNCTIONAL_READY=
SECURITY_HARDENING_STATUS=VERIFIED|PARTIAL|DEFERRED|UNKNOWN
BLOCKING_GAPS=
NON_BLOCKING_GAPS=
ROLLBACK_READY=
FREEZE=YES|NO
NO_FURTHER_TUNING_WITHOUT_NEW_EVIDENCE=
```

## References

- [Acceptance matrix](references/acceptance-matrix.md)
- [Security separation](references/security-separation.md)
- [Freeze rule](references/freeze-rule.md)
