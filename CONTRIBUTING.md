# Contributing

Contributions should improve a distinct operational decision, evidence gate, or platform adapter. Avoid duplicating general networking manuals.

For a new adapter or protocol, include:

- the tested environment and versions;
- the evidence level (`VERIFIED`, `OBSERVED`, `ENV_SPECIFIC`, or `RECOLLECT_FAILED`);
- exactly what was verified and what remains unverified;
- action-class and authorization boundaries;
- backup and rollback behavior;
- public-safe synthetic fixtures;
- activation and boundary cases where routing could be ambiguous.

Do not submit credentials, live subscription material, private infrastructure identifiers, or raw production exports. “Works for me” is not sufficient evidence. Separate transport success from application HTTP status and distinguish a client from an independent network.

Keep changes concise. If removing a proposed file would not remove a distinct capability, merge the content into an existing reference instead.
