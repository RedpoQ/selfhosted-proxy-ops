# Domain architecture

Classify roles rather than requiring a fixed number of names:

- management: panel/API access;
- subscription: client projection delivery;
- proxy/SNI: transport hostname or TLS identity.

Roles may share or separate domains depending on TLS, exposure, transport, and policy. Separation can reduce ownership ambiguity but is not a purchase requirement.

No-domain branch: use direct-address-capable transports and an appropriate certificate/authentication model, document management exposure, and skip CDN-dependent branches. Never force domain acquisition merely to satisfy a template.
