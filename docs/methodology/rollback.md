# Rollback

A backup is useful only when it is complete, integrity-checked, readable by the recovery actor, and paired with a restore procedure.

Production mutation gate:

```text
baseline
→ complete backup
→ rollback path
→ one primary change
→ static validation
→ apply
→ runtime validation
→ observed traffic validation
```

Use commit-confirm style behavior for risky remote network changes: schedule or prepare rollback before applying, confirm only after the control path and service path pass, and let the rollback remain independent of the Agent session.

If the Agent or operator reaches the host through the proxy, route, firewall, DNS, or service being changed, set `OFFLINE_ROLLBACK_REQUIRED=YES`. Recovery must not depend on the modified path or on the Agent surviving.
