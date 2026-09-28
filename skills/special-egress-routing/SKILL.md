---
name: special-egress-routing
description: Validate or design server-side special/static/residential egress with a dedicated inbound-to-route-to-outbound invariant and negative isolation. This is the primary workflow for egress-policy intent; use xui-xray-stack only as 3X-UI/Xray implementation context.
---

# Special egress routing

## Purpose

Prove both the intended special path and the absence of unintended ordinary traffic on that path.

## When to use

Use when selected traffic must use a distinct special, static, residential, or provider outbound. This Skill owns the server-side egress-policy intent; `xui-xray-stack` may provide 3X-UI/Xray implementation context but is not primary. Prefer `proxy-client-governance` when the fault is client-local DNS, TUN, rules, or group selection. Do not use when ordinary default egress is sufficient.

## Preconditions

Known special traffic boundary, control-plane source of truth, protected provider credentials, baseline ordinary route, and rollback.

## Workflow

1. Read [route isolation](references/route-isolation.md).
2. Identify the special inbound, dedicated rule, and special outbound in persistent/template/generated/runtime layers.
3. Verify positive routing with an authorized, redacted exit-match probe.
4. Verify ordinary inbound does not match the special outbound.
5. Confirm existing ordinary transports and exits remain unchanged.

## Decision gates

Positive success without negative isolation is insufficient. A route declared in a template does not prove runtime or exit behavior.

## Mutations

- **Allowed:** read-only by default; one complete, scoped route/outbound change with explicit authorization and rollback.
- **Prohibited:** printing provider host/user/password/token/exit, broad catch-all routes, partial control-plane updates, or applying special egress to ordinary traffic.

## STOP conditions

Credential exposure, ambiguous inbound ownership, incomplete rollback, ordinary-route regression, or inability to verify exit without revealing it.

## Evidence requirements

Use fingerprints, equality checks, booleans, and role labels. Never print the actual exit address.

## Output contract

```text
SPECIAL_EGRESS_STRUCTURE=PASS|FAIL|UNKNOWN
ORDINARY_ROUTE_ISOLATION=PASS|FAIL|UNKNOWN
EXIT_MATCH_EXPECTED=VERIFIED|OBSERVED|NOT_RUN
SECRETS_EXPOSED=NO
```

## References

- [Route isolation](references/route-isolation.md)
