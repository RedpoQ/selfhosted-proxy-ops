---
name: proxy-client-governance
description: Reconcile client-local proxy settings, generated configuration, runtime state, DNS, TUN, rules, and observed traffic across platform adapters. This owns client-local routing; use special-egress-routing for server-side special outbound isolation. Windows is environment-specific reference material.
---

# Proxy client governance

## Purpose

Identify the actual owner of mode, TUN, DNS, rules, and node selection, then validate runtime traffic semantics.

## When to use

Use when the GUI and traffic disagree, client-local TUN/DNS/rules or group selection appear stale, or fail-closed structure must be checked. This Skill is primary for client-local ownership; prefer `special-egress-routing` for server-side special outbound isolation. Do not apply the Windows reference unchanged to other platforms.

## Preconditions

Known active profile/process, safe controller read access, platform adapter status, and offline rollback when the Agent depends on the client.

## Workflow

1. Use the relevant platform reference: [Windows](references/windows.md), [Linux](references/linux.md), [macOS](references/macos.md), or [OpenWrt](references/openwrt.md).
2. Trace application settings → extensions → generated config → runtime → observed traffic.
3. Record ownership of mode, TUN, DNS, and rules.
4. Verify route semantics with fresh runtime connections.
5. Prefer structural fail-closed proof: final match targets a proxy group, `DIRECT` is absent from it, and no direct fallback/nested bypass exists.

## Decision gates

Generated/runtime evidence outranks saved GUI state. Regional direct-routing examples are policy examples, not global defaults.

## Mutations

- **Allowed:** read-only by default; controlled client change only with preserved profile/node state, validation, and rollback.
- **Prohibited:** silent node switching, production sabotage, destructive fail-closed tests on one host, unverified macOS/OpenWrt automation, and exposing node material.

## STOP conditions

Agent depends on the proxy without offline rollback, active profile is unknown, service-mode ownership is inaccessible, or runtime cannot be distinguished from stale connections.

## Evidence requirements

Capture version, active source, generated values, runtime controller values, adapter/routes, and observed rule/chain. Keep application HTTP status separate.

## Output contract

```text
PLATFORM_STATUS=
MODE_SOURCE=
TUN_SOURCE=
DNS_SOURCE=
RULES_SOURCE=
RUNTIME_MATCH=
FAIL_CLOSED_STRUCTURE=
OFFLINE_ROLLBACK_REQUIRED=
```

## References

- [Windows](references/windows.md)
- [Linux](references/linux.md)
- [macOS](references/macos.md)
- [OpenWrt](references/openwrt.md)
