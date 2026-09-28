# Architecture

The repository is organized along three dimensions.

## A. Core lifecycle

Capability discovery → region/path fit → VPS correctness → control/data plane → minimal proxy → client integration → acceptance → freeze.

This is the shortest path to a working, explainable stack. Each stage has a PASS gate; a later stage must not be used to conceal a failed earlier one.

## B. Conditional capabilities

Implemented conditional branches are domain/DNS/TLS under the 3X-UI + Xray adapter, Cloudflare edge reasoning where applicable, protocol and preferred-edge experiments, shadow testing, benchmark methodology, special egress routing, subscription projection, and client governance. They are not mandatory milestones.

Safe automation is limited to documented safety and rollback principles; v0.1 has no general production automation framework. The only implemented control-plane adapter is 3X-UI + Xray. Other control planes may reuse the lifecycle and methodology, but their adapters are out of scope. `vps-baseline` checks correctness rather than tuning performance; only `proxy-transport-lab` may run isolated, single-variable, measurable, reversible experiments.

## C. Cross-cutting methodology

Every stage applies capability discovery, pollution auditing, evidence hierarchy, source-of-truth separation, one-variable changes, controls, shadow testing, ablation, progressive evidence, complexity budgets, secret handling, backup/rollback, fail-closed checks, platform honesty, explicit uncertainty, and freeze rules.

## Simplicity by ablation

For an optional component, compare the accepted baseline with the treatment and then remove the treatment. If removal preserves acceptance invariants, prefer the simpler architecture. Each CDN, DNS layer, route, script, egress, and automation adds ownership and failure surfaces.

The architecture therefore does not assume that users need Cloudflare, a domain, preferred IPs, multiple protocols, static egress, or a 24-hour soak.
