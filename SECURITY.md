# Security policy

This project describes operations on network infrastructure. Treat every copied runtime object as potentially sensitive.

Do not commit or attach:

- credentials, tokens, cookies, sessions, or controller secrets;
- private keys or protocol authentication material;
- subscription URLs, paths, or identifiers;
- real provider, static-proxy, or residential-egress credentials;
- production database/configuration exports;
- real public addresses, private hostnames, or panel paths.

Use synthetic fixtures and documentation networks. When reporting a vulnerability, reproduce it without real secrets. If redaction cannot be proven complete, describe the structure and impact instead of attaching the artifact.

Functional proxy acceptance does not imply host security hardening. Report functional readiness and security-hardening status separately.

Security reports should state the affected Skill or document, the tested version, evidence level, reproduction boundary, and whether any production mutation occurred.
