---
name: vps-region-fit
description: Evaluate a real user's network path to candidate VPS regions and intended destinations with contamination-aware evidence. Use for selecting or evaluating VPS regions and paths; use proxy-transport-lab to compare transports on an accepted path. Do not purchase or migrate servers.
---

# VPS region fit

## Purpose

Evaluate `User → VPS + VPS → Intended Destinations` under comparable conditions.

## When to use

Use before choosing or migrating a region, or when path quality is a plausible bottleneck. Prefer this Skill over `proxy-transport-lab` when the primary decision is which VPS region or network path to accept. Once a path is accepted, use `proxy-transport-lab` to compare available proxy transports. Do not use geography alone to recommend a region.

## Preconditions

Known real client/ISP, candidate endpoints, intended destinations, probe budget, and mutation boundary.

## Workflow

1. Run [pollution audit](references/pollution-audit.md).
2. If contamination is acceptable, follow [region testing](references/region-testing.md).
3. Measure bounded ICMP RTT/jitter/loss, TCP and TLS handshake, SSH responsiveness, short HTTP transfer, and UDP reachability only when evidence can be collected safely.
4. Compare evidence in this order: same real client/ISP and multiple regions; provider endpoint; Looking Glass; historical same-condition data; geography guess.
5. Keep client-to-VPS and VPS-to-destination conclusions separate.

## Decision gates

Do not treat a locally intercepted TCP connect as remote RTT. Do not rank incomparable windows as if controlled.

## Mutations

- **Allowed:** read-only, bounded probes.
- **Prohibited:** buying, migrating, changing DNS/routes/TUN/proxy state, large transfers by default, or provider changes.

## STOP conditions

Stop when contamination is `HIGH`/`UNKNOWN`, host identity is uncertain, probes would disrupt production, or candidates lack comparable evidence.

## Evidence requirements

Record time, client/ISP class, contamination, sample count, failures, and probe layer. Mark recommendations `ENV_SPECIFIC`.

## Output contract

```text
MEASUREMENT_CONTAMINATION=NONE|PARTIAL|HIGH|UNKNOWN
CLIENT_TO_VPS=
VPS_TO_DESTINATIONS=
UDP_REACHABILITY=VERIFIED|OBSERVED|UNVERIFIED
REGION_COMPARISON=
RECOMMENDATION_CONFIDENCE=
```

## References

- [Pollution audit](references/pollution-audit.md)
- [Region testing](references/region-testing.md)
