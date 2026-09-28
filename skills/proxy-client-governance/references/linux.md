# Linux client adapter

Status: **PARTIAL VALIDATION**.

Inspect systemd service/process ownership, NetworkManager versus systemd-resolved, `ip route`/policy rules, TUN devices, permissions, proxy environment variables, desktop system proxy, and the active core command/config.

Use a separate shadow core only in a permitted runtime directory with loopback listeners, TUN off, and explicit traffic. Do not infer the active profile from saved YAML. Linux distributions and desktop environments differ; keep untested service and DNS behavior explicit.
