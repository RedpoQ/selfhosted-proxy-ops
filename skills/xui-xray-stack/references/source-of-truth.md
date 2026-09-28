# Source-of-truth model

```text
Persistent DB
    ↓
Template
    ↓
Control-plane generation
    ↓
Xray runtime
    ↓
Subscription projection
```

- **Persistent:** desired objects that survive restart.
- **Template:** shared runtime policy, API bootstrap, and routing/outbound material.
- **Generated:** files or API calls produced by the control plane.
- **Runtime:** in-memory handlers, processes, listeners, routes, and counters.
- **Projection:** client-facing links/YAML derived from persistent state.

Modern control planes may start Xray with a small API bootstrap and inject handlers dynamically. In that case the process command's config file is intentionally incomplete. Establish generation through API services, process ownership, listeners, and DB/template relationships before declaring drift.
