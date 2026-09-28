# Region testing

Use the same client, ISP, time window, sample counts, timeouts, and destination set for every candidate.

For measurements, use a real endpoint that the user owns, is authorized to test, or that the provider explicitly exposes for testing. In reports and fixtures, replace identifying addresses with role labels or RFC 5737 TEST-NET examples. Documentation addresses and real authorized test endpoints are different roles: never send performance or connectivity measurements to TEST-NET addresses such as `192.0.2.0/24`, `198.51.100.0/24`, or `203.0.113.0/24`.

Collect small samples first:

1. ICMP loss, median/average, tail, and successive-sample jitter.
2. TCP connect success and latency, with contamination caveats.
3. TLS handshake success and latency.
4. SSH command responsiveness, not banner reachability alone.
5. A short HTTP object with status separated from transport success.
6. UDP evidence only through a suitable protocol or endpoint.

No single metric is a region verdict. High ICMP loss may reflect rate limiting; successful TCP/TLS does not prove the application protocol; a Looking Glass is not the user's path.
