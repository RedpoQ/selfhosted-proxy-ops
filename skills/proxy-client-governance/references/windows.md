# Windows adapter

Status: **ENV_SPECIFIC_REFERENCE**.

The workflow was derived from and checked against a real environment, but this repository does not claim universal Windows platform validation.

Inspect system proxy, TUN/service mode, active physical and virtual adapters, DNS/fake-IP, generated config, runtime controller, route conflicts, VPN adapters, and WinINET versus WinHTTP behavior. Do not hard-code local ports.

One validated ownership pattern is:

```text
GUI/application → mode, IPv6, TUN
DNS override   → DNS, fake-IP, respect-rules
Global Merge  → empty when unnecessary
Global Script → no-op when unnecessary
Profile Script → profile-specific routing
```

This is an example, not a required Clash layout. A regional routing example may send LAN/private and selected local-region domains/IPs direct, with `MATCH → PROXY`; it is not a worldwide default.

For shadow processes, use an independent executable/config, loopback ports, TUN off, system proxy off, and explicit traffic. Service-mode safe-path restrictions must not be bypassed by guessing runtime paths.
