# Tests

These tests are documentation-level routing and safety cases. They must not contact a real VPS, start a proxy, modify networking, or require credentials.

- `activation/cases.md` checks that representative requests select the intended Skill.
- `boundary/cases.md` checks exclusions, uncertainty, STOP conditions, and escalation boundaries.
- `fixtures/` contains synthetic, public-safe examples for static review.

Review tests semantically. Exact wording is not an acceptance criterion; correct routing, evidence requirements, and safety behavior are.

Run the dependency-free static repository checker from the repository root:

```text
python tests/check_repository.py
```

The checker is read-only and validates the manifest, eight Skill entrypoints and names, local Markdown links, required routing cases, obvious secret/private-key/UUID/local-user-path patterns, and non-documentation public IPv4 literals.
