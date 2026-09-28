# Route isolation

Required invariant:

```text
special inbound
→ dedicated route
→ special outbound

ordinary inbound
→ NOT special outbound
```

Verify across persistent state, generated/runtime route tables, and observed traffic. Positive checks prove the special path works; negative checks prove scope. Use a provider-supplied expected-exit fingerprint or protected comparison and report only match/mismatch.
