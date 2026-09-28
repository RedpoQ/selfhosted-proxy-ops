# DNS ownership

Detect ownership before repair:

- systemd-resolved: service state, `/etc/resolv.conf` target, link/global DNS scopes;
- NetworkManager: active connection DNS and resolver integration;
- netplan: renderer and declarative nameservers;
- resolvconf/openresolv: generated file ownership;
- static `/etc/resolv.conf`: only after excluding generators.

Validate both configuration and queries. A stub address is not a failure by itself. If a repair is authorized, change the smallest owner-controlled layer and prove persistence without replacing unrelated network configuration.
