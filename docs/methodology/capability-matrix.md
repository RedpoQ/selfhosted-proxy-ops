# Capability matrix

Collect before proposing a workflow:

```text
CLIENT_OS=
CLIENT_ARCH=
ADMIN_AVAILABLE=
CURRENT_NETWORK_TYPE=
SECOND_CLIENT_AVAILABLE=
SECOND_NETWORK_AVAILABLE=
LONG_RUNNING_SECOND_HOST_AVAILABLE=
CURRENT_PROXY_CLIENT=
CURRENT_PROXY_CORE=
AGENT_DEPENDS_ON_PROXY=
VPS_AVAILABLE=
VPS_REGION=
DOMAIN_AVAILABLE=
CLOUDFLARE_IN_USE=
CONTROL_PLANE=
DATA_PLANE=
```

Use `UNKNOWN` rather than inference. A second client on the same LAN is not a second independent network. Admin availability is a capability, not permission. Access to a control plane does not authorize mutation.
