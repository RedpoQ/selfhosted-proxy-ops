---
name: vps-baseline
description: Audit and, only when explicitly authorized, minimally repair Linux VPS correctness across OS, resources, routing, resolver ownership, time, services, listeners, and network counters. Use before proxy deployment; not for speculative performance tuning.
---

# VPS baseline

## Purpose

Prove Linux host correctness before control-plane or protocol work.

## When to use

Use for a new VPS, package/DNS failure, uncertain host health, or a pre-deployment baseline. Do not use to justify random sysctl, MTU, BBR, qdisc, or buffer changes.

## Preconditions

Verified target identity, permitted read access, and explicit authorization before any repair.

## Workflow

1. Read [Linux baseline](references/linux-baseline.md), [DNS ownership](references/dns-ownership.md), and [network counters](references/network-counters.md).
2. Collect OS, kernel, virtualization, CPU/RAM/disk/load/uptime, interfaces/routes, IPv4/IPv6, resolver, DNS, time, package-manager health, failed units, listeners, congestion control, qdisc, and counters.
3. Separate correctness failures from optimization candidates.
4. For an authorized repair: baseline → backup → owner-specific minimal repair → static check → apply → runtime check → external verification.

## Decision gates

Resolver ownership must be known before editing DNS. Nonzero counters require a rate and correlated failure before they justify tuning.

## Mutations

- **Allowed:** an explicit, minimal correctness repair with rollback.
- **Prohibited by default:** package upgrades, random sysctl/buffer/MTU changes, BBR/qdisc switching, firewall/SSH changes, and unrelated hardening.

## STOP conditions

Wrong host, unexpected services, incomplete backup, ambiguous resolver owner, loss of control path, or repair beyond authorization.

## Evidence requirements

Use current outputs; redact addresses and ports by role. Distinguish `PASS`, `WARN`, permission-limited, and not run.

## Output contract

```text
VPS_CORRECTNESS=
DNS_OWNER=
DNS_HEALTH=
DEFAULT_ROUTE_HEALTH=
TIME_SYNC=
FAILED_UNITS=
NETWORK_COUNTER_ANOMALY=
CORRECTNESS_REPAIR_REQUIRED=
TUNING_ACTION_REQUIRED=NOT_EVALUATED
```

## References

- [Linux baseline](references/linux-baseline.md)
- [DNS ownership](references/dns-ownership.md)
- [Network counters](references/network-counters.md)
