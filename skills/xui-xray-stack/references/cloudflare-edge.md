# Cloudflare and edge compatibility

First determine whether the transport is compatible with an HTTP reverse proxy/CDN. Ordinary CDN proxying does not transparently carry every TCP/UDP proxy protocol.

Separate DNS proxy status, edge TLS, origin TLS, HTTP/WebSocket/H2 behavior, and the actual proxy protocol. Pair a proxy-path result with fresh direct TCP/TLS controls where possible. Preferred IPs are an optional experiment and can drift over time; they are not a default optimization.
