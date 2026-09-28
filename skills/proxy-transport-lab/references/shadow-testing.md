# Shadow testing

```text
production
→ unchanged

shadow
→ separate process
→ separate temporary config
→ localhost high port
→ TUN OFF
→ system proxy OFF
→ explicit test traffic only
```

Shadow is application-level isolation, not a second physical network. It can prove parsing, process startup, proxy handshakes, bounded traffic, and comparative behavior. It cannot fully prove TUN capture, system DNS hijack, OS routing, service-mode ownership, or production integration.

Before and after, inventory relevant processes, listeners, routes, proxy state, TUN adapters, and protected-file hashes. Terminate only the exact shadow process and verify its temporary files/listeners are gone.
