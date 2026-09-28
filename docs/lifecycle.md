# Core lifecycle

Each stage uses: Goal, Preconditions, Capability requirements, Read-only baseline, Allowed actions, Evidence, PASS gate, STOP conditions, Rollback, Secrets, and Next stage.

## 0. Capability and safety discovery

- **Goal:** determine topology, dependencies, authorization, and evidence access.
- **Preconditions:** none.
- **Capabilities:** client/VPS access, admin state, second host/network, proxy dependency.
- **Baseline:** inventory only.
- **Allowed actions:** `READ_ONLY`.
- **Evidence:** capability matrix and contamination statement.
- **PASS:** topology and safe next action are known.
- **STOP:** control-channel dependency or ownership is unknown for a disruptive step.
- **Rollback:** not applicable.
- **Secrets:** record presence, never value.
- **Next:** region/path fit or the first known incomplete stage.

## 1. Region and path fit

- **Goal:** verify the real client-to-region path and VPS-to-destination path.
- **Preconditions:** clean or classified measurement path.
- **Capabilities:** bounded ICMP/TCP/TLS/SSH/HTTP; UDP only when safe.
- **Baseline:** pollution audit.
- **Allowed actions:** read-only probes; no purchase or migration.
- **Evidence:** loss, jitter, latency, reachability, provenance.
- **PASS:** path meets the user's stated needs with uncontaminated evidence.
- **STOP:** high/unknown contamination or incomparable regions.
- **Rollback:** remove only explicit temporary probes.
- **Secrets:** redact target identifiers.
- **Next:** VPS correctness.

## 2. VPS correctness

- **Goal:** establish OS, storage, route, resolver, time, service, and listener correctness.
- **Preconditions:** verified host identity.
- **Capabilities:** shell read access; admin only for otherwise invisible facts.
- **Baseline:** full read-only inventory.
- **Allowed actions:** explicit minimal correctness repair only.
- **Evidence:** current state plus post-repair verification when authorized.
- **PASS:** correctness blockers are absent.
- **STOP:** wrong host, ambiguous resolver owner, or missing rollback.
- **Rollback:** exact file/service restoration plan.
- **Secrets:** no raw configs.
- **Next:** control/data plane.

## 3. Control/data plane

- **Goal:** identify persistent, generated, runtime, and projection layers.
- **Preconditions:** VPS correctness PASS.
- **Capabilities:** control-plane read API/DB and runtime inspection.
- **Baseline:** source-of-truth graph.
- **Allowed actions:** bootstrap only under a production-change gate.
- **Evidence:** layer relationships, not one config file.
- **PASS:** control and data planes agree.
- **STOP:** incomplete backup or unverifiable generation path.
- **Rollback:** complete persistent objects and service recovery.
- **Secrets:** retain only protected, non-published backups.
- **Next:** minimal working proxy.

## 4. Minimal working proxy

- **Goal:** prove one transport end to end before optional complexity.
- **Preconditions:** control/data plane PASS.
- **Capabilities:** client parse and bounded observed-traffic probe.
- **Baseline:** existing runtime and listener state.
- **Allowed actions:** one primary transport change if authorized.
- **Evidence:** static parse, runtime, traffic.
- **PASS:** one minimal path works and can be rolled back.
- **STOP:** treatment changes multiple variables.
- **Rollback:** restore complete baseline.
- **Secrets:** no share links in reports.
- **Next:** client integration.

## 5. Client integration

- **Goal:** reconcile application ownership, generated config, runtime, DNS, TUN, and routing.
- **Preconditions:** minimal proxy PASS.
- **Capabilities:** platform adapter and runtime controller.
- **Baseline:** active profile and generated config.
- **Allowed actions:** controlled client mutation with preserved selection and rollback.
- **Evidence:** runtime and observed connections.
- **PASS:** intended traffic semantics are demonstrated.
- **STOP:** Agent/control path depends on the setting without offline rollback.
- **Rollback:** offline-capable restoration.
- **Secrets:** redact node material.
- **Next:** acceptance.

## 6. End-to-end acceptance

- **Goal:** classify functional readiness, security status, gaps, and rollback confidence.
- **Preconditions:** all required prior gates.
- **Capabilities:** acceptance matrix evidence.
- **Baseline:** fresh current state.
- **Allowed actions:** read-only verification by default.
- **Evidence:** server through observed traffic.
- **PASS:** blocking rows pass; gaps are classified.
- **STOP:** any blocking gap.
- **Rollback:** verified and usable.
- **Secrets:** report classifications only.
- **Next:** freeze.

## 7. Freeze

- **Goal:** prevent speculative tuning after acceptance.
- **PASS:** core acceptance passes, no new failure evidence, no explicit new requirement.
- **Output:** `FREEZE=YES` and `NO_FURTHER_TUNING_WITHOUT_NEW_EVIDENCE`.

Conditional branches attach to the relevant stage and do not become compulsory lifecycle steps.
