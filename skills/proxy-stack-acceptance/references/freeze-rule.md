# Freeze rule

Set:

```text
FREEZE=YES
NO_FURTHER_TUNING_WITHOUT_NEW_EVIDENCE=YES
```

only when core acceptance passes, no new failure evidence exists, and no explicit new requirement is pending.

Freeze prevents speculative optimization and ownership churn. It does not prohibit security work, incident response, required maintenance, or a new authorized feature. Those events reopen the relevant lifecycle stage with a fresh baseline.
