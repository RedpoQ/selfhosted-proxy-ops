# Evidence hierarchy

```text
Declared configuration
    ↓
Generated configuration
    ↓
Runtime state
    ↓
Observed traffic
```

Each later layer answers a question the earlier one cannot. A declared option shows intent; generated configuration shows composition; runtime shows what the process accepted; observed traffic shows actual routing and behavior.

When layers disagree, preserve the disagreement and investigate ownership. Do not rewrite a declared file merely to make it resemble runtime. Record time and contamination for observed traffic, and distinguish transport establishment from application response.
