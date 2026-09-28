---
name: xui-xray-stack
description: Inspect and govern the implemented 3X-UI plus Xray adapter across persistent data, generated state, runtime, domain/TLS architecture, listeners, and subscription projection. Use proxy-transport-lab when an edge is a performance treatment, and do not route non-3X-UI implementation requests here.
---

# 3X-UI and Xray stack

## Purpose

Maintain an evidence-backed source-of-truth model for the implemented adapter.

## When to use

Use when the primary problem is 3X-UI/Xray control-plane state, domain/TLS architecture, runtime generation, listeners, or subscription projection. Prefer `proxy-transport-lab` when Cloudflare or a preferred edge is being compared as a performance treatment. For special/static/residential egress intent, `special-egress-routing` is primary and this Skill supplies only implementation context.

Do not trigger this as an implementation workflow for a non-3X-UI control plane in v0.1. Use the general lifecycle and methodology, and mark the adapter unsupported.

## Preconditions

VPS correctness PASS, known authorization, and protected handling for any persistent database or credential-bearing object.

## Workflow

1. Read [source of truth](references/source-of-truth.md).
2. Inventory persistent DB, template, generation mechanism, Xray runtime, listeners, and subscription projection.
3. If domains exist, read [domain architecture](references/domain-architecture.md) and [TLS/ACME](references/tls-acme.md). Preserve the no-domain branch.
4. Read [Cloudflare edge](references/cloudflare-edge.md) only when an edge is present.
5. Validate subscriptions with [subscription projection](references/subscription-projection.md).

## Decision gates

A single `config.json`, HTTP 200, or panel record cannot prove the whole stack. Transport compatibility must precede edge configuration.

## Mutations

- **Allowed:** read-only by default; a complete-object controlled mutation only after baseline, backup, rollback, and explicit authorization.
- **Prohibited:** partial unknown-schema updates, direct DB edits, secret output, invented domains, forced domain purchase, and unsupported CDN assumptions.

## STOP conditions

Incomplete persistent backup, unclear generation path, stale client object, authentication ambiguity, or control-channel risk.

## Evidence requirements

Prove persistent, generated, runtime, and projection layers independently. Hash or classify sensitive objects instead of printing them.

## Output contract

```text
PERSISTENT_STATE=
TEMPLATE_STATE=
GENERATION_MECHANISM=
XRAY_RUNTIME=
SUBSCRIPTION_PROJECTION=
DOMAIN_BRANCH=DOMAIN|NO_DOMAIN
LAYER_CONSISTENCY=
```

## References

- [Source of truth](references/source-of-truth.md)
- [Domain architecture](references/domain-architecture.md)
- [TLS and ACME](references/tls-acme.md)
- [Cloudflare edge](references/cloudflare-edge.md)
- [Subscription projection](references/subscription-projection.md)
