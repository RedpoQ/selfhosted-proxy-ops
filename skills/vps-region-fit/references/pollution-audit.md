# Pollution audit

Before measuring, inspect TUN/TAP adapters, system proxy, proxy environment variables, SSH `ProxyCommand`, VPN/WireGuard, Tailscale, ZeroTier, corporate proxying, other proxy processes/listeners, DNS ownership, and default routes.

Classify:

- `NONE`: evidence supports a direct physical path.
- `PARTIAL`: a known overlay affects some probes; report which ones.
- `HIGH`: the tested path is materially different from the claimed path.
- `UNKNOWN`: visibility is insufficient.

A proxy may return a fast local TCP accept while the remote connection is slow or failed. Measure full protocol responsiveness or an independently direct path before calling it remote TCP latency.
