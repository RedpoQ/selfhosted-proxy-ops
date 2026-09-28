# TLS and ACME

Inspect certificate existence, readable metadata, SAN match, validity window, renewal mechanism, and deployment path. Do not read or copy private-key content.

Distinguish issuance from deployment: an ACME client or timer may renew one path while the service reads another. Verify the service's referenced certificate and the external TLS handshake. A valid certificate does not prove transport semantics or subscription correctness.
