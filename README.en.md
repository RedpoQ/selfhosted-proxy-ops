# selfhosted-proxy-ops

A staged, evidence-driven operational framework for building, testing, governing, and freezing self-hosted proxy stacks.

This project addresses a common operational problem: a proxy can appear correct in a panel or configuration file while its generated configuration, runtime state, client projection, or observed traffic says otherwise. The repository supplies eight composable Skills that make those layers explicit and keep production changes behind evidence and rollback gates.

It is not a turnkey installer, a provider recommendation, a performance-ranking claim, or a security-hardening substitute. It ships no MCP server, credentials, production scripts, or default infrastructure topology.

[简体中文](README.md)

## Core lifecycle

1. Capability and safety discovery
2. User network to VPS region/path fit
3. VPS correctness baseline
4. Control/data plane bootstrap
5. Minimal working proxy
6. Client integration
7. End-to-end acceptance
8. Freeze

Conditional capabilities branch from this lifecycle only when needed: domain/DNS/TLS under the implemented 3X-UI + Xray adapter, Cloudflare edge reasoning where applicable, protocol and preferred-edge experiments, shadow testing, benchmark methodology, special egress routing, subscription projection, and client governance.

Cross-cutting methodology includes baseline-before-mutation, capability discovery, pollution audits, evidence hierarchy, source-of-truth separation, one-variable experiments, controls, shadow testing, ablation, progressive evidence, complexity budgets, secret redaction, backup/rollback, fail-closed verification, explicit uncertainty, and freeze-after-acceptance.

See [architecture](docs/architecture.md), [lifecycle](docs/lifecycle.md), and the public-safe [evidence inventory](docs/evidence-inventory.md).

## Skills

| Skill | Responsibility |
|---|---|
| `proxy-stack-lifecycle` | Discover the current stage, constraints, blockers, and next workflow without mutating systems. |
| `vps-region-fit` | Measure contamination-aware user-to-region and VPS-to-destination path quality. |
| `vps-baseline` | Establish Linux VPS correctness before protocol work or tuning. |
| `xui-xray-stack` | Govern the implemented 3X-UI + Xray adapter and its source-of-truth layers. |
| `proxy-transport-lab` | Run isolated transport experiments, benchmarks, ablations, and progressive tests. |
| `special-egress-routing` | Prove both positive special routing and negative ordinary-route isolation. |
| `proxy-client-governance` | Reconcile application settings, generated config, runtime, and observed client traffic. |
| `proxy-stack-acceptance` | Decide readiness, security status, remaining gaps, rollback confidence, and freeze. |

## Support matrix

| Area | Status |
|---|---|
| Windows client governance | `ENV_SPECIFIC_REFERENCE` |
| Linux VPS baseline | `ENV_SPECIFIC_REFERENCE` |
| 3X-UI + Xray | `ENV_SPECIFIC_REFERENCE` |
| Shadow Mihomo pattern | `ENV_SPECIFIC_REFERENCE` |
| Linux client integration | `PARTIAL_REFERENCE` |
| macOS | `UNVERIFIED` |
| OpenWrt | `UNVERIFIED_OPTIONAL` |

`ENV_SPECIFIC_REFERENCE` means the workflow was derived from and checked against a real environment, but this repository does not claim universal platform validation. `PARTIAL_REFERENCE` has narrower evidence, while `UNVERIFIED` and `UNVERIFIED_OPTIONAL` must not be presented as production-tested adapters.

## Capability limits in v0.1

- **Safe automation:** v0.1 documents safety and rollback principles, but does not provide a general production automation framework.
- **Generic control planes:** v0.1 implements the 3X-UI + Xray adapter. Other control planes may reuse the methodology, but are not implemented adapters.
- **VPS tuning:** `vps-baseline` does not tune for performance. `proxy-transport-lab` permits only isolated, single-variable, measurable, reversible experiments.

## Safety and evidence model

The default action class is `READ_ONLY`. Other classes are `CONTROLLED_MUTATION`, `EXPERIMENTAL_SHADOW`, and `PRODUCTION_CHANGE`. Production changes require baseline, backup, a rollback path, one primary change, static validation, apply, runtime validation, and observed-traffic validation. If the control channel depends on the proxy being changed, offline rollback is required.

Evidence precedence is:

```text
Declared configuration
    ↓
Generated configuration
    ↓
Runtime state
    ↓
Observed traffic
```

Later evidence outranks earlier declarations. A value in a file does not prove runtime application. See [evidence hierarchy](docs/methodology/evidence-hierarchy.md).

## Secret handling

Never commit real addresses, domains, account names, private keys, UUIDs, protocol credentials, subscription URLs, tokens, panel paths, controller secrets, provider credentials, or exit addresses. Use documentation networks, `example.com`, synthetic fixtures, and `<REDACTED_...>` placeholders. Do not ingest a secret merely to produce a sanitized copy. See [secret handling](docs/methodology/secret-handling.md).

## Quick start

1. Start with `proxy-stack-lifecycle` and record the capability matrix and action class.
2. Follow the selected next Skill; load only the references required by that branch.
3. Keep facts, inferences, unknowns, and environment-specific observations separate.
4. Stop at any unmet backup, rollback, control-channel, or source-of-truth gate.
5. Finish with `proxy-stack-acceptance`; freeze a passing stack until new failure evidence or a new requirement appears.

## Status

`v0.1 release candidate` — public, knowledge-and-workflow first. Portable install smoke, model-activation evaluation, and broader cross-platform acceptance remain known validation gaps. The repository intentionally has no general production automation framework, CI/CD, telemetry, or package publication.

## License

MIT. See [LICENSE](LICENSE).
