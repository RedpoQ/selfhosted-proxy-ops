# Complexity budget

Every optional component must earn its maintenance cost.

Adding a CDN, DNS layer, route, script, special egress, automation, protocol, or controller increases:

- failure surface;
- ownership ambiguity;
- credential exposure;
- rollback scope;
- maintenance and debugging cost.

State the measurable benefit and acceptance invariant before adding complexity. If the benefit is absent, unrepeatable, or disappears under ablation, do not keep the component. A component may still be justified for policy or resilience, but that requirement must be explicit.
