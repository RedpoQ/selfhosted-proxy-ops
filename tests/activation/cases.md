# Activation cases

## 1. New VPS

- **Input:** “I just bought a VPS and want to set up a proxy.”
- **Expected skill:** `proxy-stack-lifecycle`
- **Expected behavior:** discover capability, topology, authorization, current stage, and blockers before selecting an implementation Skill.

## 2. Region comparison

- **Input:** “Tokyo or San Jose, which VPS path is better for my current ISP?”
- **Expected skill:** `vps-region-fit`
- **Expected behavior:** start with pollution audit and comparable current-path evidence; no purchase or geography-only verdict.

## 3. VPS DNS failure

- **Input:** “apt update fails on my new VPS and DNS looks broken.”
- **Expected skill:** `vps-baseline`
- **Expected behavior:** detect resolver owner and root cause before proposing an authorized minimal repair.

## 4. Control/runtime mismatch

- **Input:** “My 3X-UI subscription does not match the running Xray listeners.”
- **Expected skill:** `xui-xray-stack`
- **Expected behavior:** compare persistent, template, generated, runtime, and projection layers.

## 5. Safe protocol comparison

- **Input:** “Compare Hysteria2 and TUIC without breaking my current proxy.”
- **Expected skill:** `proxy-transport-lab`
- **Expected behavior:** isolated shadow path, bounded L0–L2 testing, production unchanged, cleanup proof.

## 6. Special egress

- **Input:** “Only AI traffic should use my static residential egress.”
- **Expected skill:** `special-egress-routing`
- **Expected behavior:** verify positive special routing and negative ordinary-route isolation without exposing the exit.

## 7. Client routing mismatch

- **Input:** “My Clash TUN is on but terminal traffic is bypassing the proxy.”
- **Expected skill:** `proxy-client-governance`
- **Expected behavior:** reconcile application, generated config, runtime routes/controller, and observed connection rules.

## 8. Stop tuning

- **Input:** “Everything works. Should I keep tuning?”
- **Expected skill:** `proxy-stack-acceptance`
- **Expected behavior:** refresh blocking acceptance evidence and freeze when no new failure or requirement exists.
