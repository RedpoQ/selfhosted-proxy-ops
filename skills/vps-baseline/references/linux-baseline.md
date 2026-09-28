# Linux baseline

Collect only what supports correctness decisions:

- OS, kernel, architecture, virtualization, uptime;
- CPU count/class, memory available, disk/inodes, load and pressure;
- interface state, MTU, IPv4/IPv6 and default routes;
- resolver ownership and DNS query;
- time synchronization;
- package-manager reachability without upgrading;
- failed units and expected service state;
- listener roles without publishing sensitive ports;
- congestion control and active/default qdisc.

Use bounded commands. Do not infer health from one low-load snapshot during an idle period, and do not equate unavailable privileged logs with the absence of errors.
