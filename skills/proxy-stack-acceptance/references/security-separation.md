# Security separation

Functional acceptance shows that intended traffic works. It does not establish host hardening, credential hygiene, management-plane restriction, firewall policy, patch posture, intrusion detection, or provider-account security.

Use only:

- `VERIFIED`: defined hardening requirements were currently checked;
- `PARTIAL`: some relevant controls were checked;
- `DEFERRED`: hardening was intentionally outside scope;
- `UNKNOWN`: evidence is insufficient.

Classify missing evidence as `BLOCKING_GAP` when it prevents the requested functional or rollback decision. Use `NON_BLOCKING_GAP` for an unrequested adapter or hardening item that does not invalidate the scoped readiness claim.
