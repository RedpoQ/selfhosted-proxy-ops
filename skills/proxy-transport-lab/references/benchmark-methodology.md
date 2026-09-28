# Benchmark methodology

Use the same client, ISP, destination, request mix, timeout, sample schedule, and measurement implementation for control and treatment.

Report:

- attempts and success rate;
- longest consecutive failure streak;
- connect/handshake P50 and P95;
- TTFB P50 and P95;
- transfer bytes, duration, and throughput;
- HTTP status separately from transport error;
- cleanup and production-integrity checks.

Do not call a short object a sustained throughput test. Do not treat HTTP 403 after a successful TLS/proxy path as transport failure. Never publish credentials or target-specific secrets in raw logs.
