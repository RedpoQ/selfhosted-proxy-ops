# Evidence inventory

Maintain evidence by class and provenance instead of copying production exports into a repository.

| Class | Meaning | May enter a public Skill? |
|---|---|---|
| `VERIFIED` | Recollected from current runtime/system | Method and sanitized result only |
| `OBSERVED` | Partial evidence that does not prove the whole claim | Yes, with limitation |
| `ENV_SPECIFIC` | True only for a particular environment/window | Anonymous example, clearly labelled |
| `RECOLLECT_FAILED` | Safe current collection failed | Yes, as a gap; never invent a replacement |
| `SECRET` | Sensitive value or artifact | No; record only that it exists |

Synthetic example:

```text
DNS_HEALTH=VERIFIED
UDP_REACHABILITY=OBSERVED
REGION_RESULT=ENV_SPECIFIC
CONTROL_API=RECOLLECT_FAILED
SUBSCRIPTION_TOKEN=SECRET
```

For each entry record collection time, system layer, action class, contamination, supporting command or API category, and known limitations. A historical PASS does not establish current health.
