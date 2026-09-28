# Adaptive testing

Levels:

- `L0`: static parse/config validation.
- `L1`: 3–5 smoke probes.
- `L2`: 20–50 samples or 5–15 minutes; default ceiling.
- `L3`: 30–60 minutes.
- `L4`: long soak.

Escalate beyond L2 only for intermittent failure, high variance, a candidate tie, or an explicit durability requirement. Stop early for deterministic failure, invalid control, security exposure, production drift, or resource risk. A request for “24 hours” is not evidence that L4 is necessary.
