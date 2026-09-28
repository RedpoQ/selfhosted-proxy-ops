# Subscription projection

A subscription is a client-facing projection, not the server runtime source of truth.

Validate:

1. endpoint role and authentication without publishing the URL;
2. HTTP status and content type;
3. non-empty content and node count;
4. parser compatibility;
5. protocol, transport, SNI/Host, address-strategy, and other semantics;
6. relationship to the intended persistent inbound;
7. client runtime after import.

HTTP 200 alone is insufficient. Cache, host expansion, and per-client projections can make node counts differ from inbound counts.
