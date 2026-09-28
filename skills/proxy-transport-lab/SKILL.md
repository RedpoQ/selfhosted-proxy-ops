---
name: proxy-transport-lab
description: Compare proxy transports and preferred-edge treatments on an accepted VPS path with isolated shadow tests, progressive benchmarks, controls, and ablation. Use for controlled performance experiments; not for region selection, stack architecture, or routine acceptance.
---

# Proxy transport laboratory

## Purpose

Produce comparable protocol evidence while keeping the production path unchanged until a bounded smoke is justified.

## When to use

Use for protocol candidates, intermittent behavior, benchmark design, preferred-edge experiments, or a narrowly scoped tuning hypothesis. Prefer `vps-region-fit` when selecting or evaluating the VPS region/path. Prefer `xui-xray-stack` when Cloudflare is an architecture or compatibility question; use this Skill when default versus preferred edge is the measured treatment. Do not benchmark merely because multiple protocols exist.

## Preconditions

A valid production baseline, available core, separate temporary config, localhost test ports, TUN/system proxy off for shadow, explicit targets, and cleanup capability.

## Workflow

1. Establish the [shadow model](references/shadow-testing.md).
2. Define control, treatment, metrics, pass/fail/stop gates, and contamination using [benchmark methodology](references/benchmark-methodology.md).
3. Run L0 static parse, L1 3–5 smoke requests, then L2 20–50 samples or 5–15 minutes by default.
4. Escalate with [adaptive testing](references/adaptive-testing.md) only for intermittent failure, high variance, or a tie.
5. Apply [ablation](references/ablation.md); prefer simpler state when removal causes no regression.
6. After shadow PASS, request authorization for a small production smoke; do not infer TUN/DNS/OS-route integration from shadow alone.

## Decision gates

HTTP status is separate from transport. A 403 after established transport is not automatically a transport failure. Never compare changed targets, windows, or clients as one-variable tests.

## Mutations

- **Allowed:** `EXPERIMENTAL_SHADOW` in isolated temporary state; production smoke only with explicit authorization.
- **Prohibited:** production node switching, TUN/system-proxy changes, unbounded load, destructive fail-closed, and retained experiments without acceptance benefit.

## STOP conditions

Invalid baseline, stale rollback source, contamination, production-path drift, cleanup failure, high resource cost, or an undeclared second variable.

## Evidence requirements

Record success rate, longest failure streak, connect, TTFB, throughput, HTTP status, duration, sample count, and error classes.

## Output contract

```text
SHADOW_ISOLATION=
TEST_LEVEL=L0|L1|L2|L3|L4
CONTROL_RESULT=
TREATMENT_RESULT=
ABLATION_RESULT=
PRODUCTION_SMOKE_REQUIRED=
CLEANUP_VERIFIED=
```

## References

- [Shadow testing](references/shadow-testing.md)
- [Benchmark methodology](references/benchmark-methodology.md)
- [Ablation](references/ablation.md)
- [Adaptive testing](references/adaptive-testing.md)
