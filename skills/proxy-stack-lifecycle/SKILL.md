---
name: proxy-stack-lifecycle
description: Discover a self-hosted proxy stack's current lifecycle stage, capability and safety constraints, next workflow, and blockers without changing systems. Use for new setups, ambiguous status, or orchestration; do not use for a narrow conceptual protocol question.
---

# Proxy stack lifecycle

## Purpose

Route work through the smallest safe lifecycle stage. Do not directly modify systems.

## When to use

Use when starting a deployment, resuming unknown work, deciding what to validate next, or reconciling multiple proxy tasks. Do not use for a self-contained conceptual question or when another Skill already owns a clearly bounded task.

## Preconditions

None. Treat missing information as `UNKNOWN`.

## Workflow

1. Read [capability matrix](../../docs/methodology/capability-matrix.md), [lifecycle](../../docs/lifecycle.md), and [rollback](../../docs/methodology/rollback.md) when disruption is possible.
2. Collect client OS/architecture/admin, network type, second client/network, current client/core, Agent proxy dependency, VPS/region, domain/Cloudflare, and control/data planes.
3. Classify `TEST_TOPOLOGY` as `SINGLE_HOST_SINGLE_NETWORK`, `SINGLE_HOST_MULTI_NETWORK`, `MULTI_HOST`, or `LAB`.
4. Identify the earliest incomplete lifecycle stage and any conditional capabilities actually required.
5. Select the next Skill and action class.

## Decision gates

- Unknown control-channel dependency blocks disruptive advice.
- A second same-LAN host does not establish an independent network.
- Optional branches must have an explicit requirement or measurable benefit.

## Mutations

- **Allowed:** none.
- **Prohibited:** configuration changes, installs, restarts, routing changes, node switching, purchases, and destructive tests.

## STOP conditions

Stop before recommending a disruptive operation when production ownership, authorization, rollback, or Agent connectivity is unknown.

## Evidence requirements

Label facts, inferences, unknowns, and environment-specific observations. Use the hierarchy in [evidence hierarchy](../../docs/methodology/evidence-hierarchy.md).

## Output contract

```text
TEST_TOPOLOGY=
CURRENT_STAGE=
BLOCKERS=
OPTIONAL_CAPABILITIES=
NEXT_SKILL=
NEXT_ACTION_CLASS=
OFFLINE_ROLLBACK_REQUIRED=
```

## References

- [Core lifecycle](../../docs/lifecycle.md)
- [Capability matrix](../../docs/methodology/capability-matrix.md)
- [Complexity budget](../../docs/methodology/complexity-budget.md)
