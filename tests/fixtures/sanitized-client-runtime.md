# Synthetic client runtime

`SYNTHETIC DATA — NOT A REAL CLIENT EXPORT`

```text
CLIENT_OS=Windows-like
PROXY_CLIENT=Clash-compatible client
CORE=Mihomo-compatible core
MODE=rule
TUN_ENABLE=true
DNS_ENABLE=true
DNS_ENHANCED_MODE=fake-ip
DNS_RESPECT_RULES=true
IPV6=false

LAN/private → DIRECT
regional example domains → DIRECT
MATCH → PROXY

PROXY_MEMBER_COUNT=3
DIRECT_IN_PROXY_GROUP=NO
RUNTIME_CONNECTION_SAMPLE=MATCH → PROXY → synthetic-node-a
```

The regional direct rule is an example policy, not a universal default.
