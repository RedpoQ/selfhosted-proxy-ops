# Secret handling

Design public artifacts from synthetic inputs. Do not read a production secret merely to redact it later.

Forbidden content includes live addresses/domains, usernames, credentials, private keys, UUIDs, protocol authentication material, subscription identifiers, panel paths, controller/API secrets, provider credentials, and real exit addresses.

Use:

- `example.com` and its subdomains;
- `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`;
- `<REDACTED_IP>`, `<REDACTED_DOMAIN>`, and `<REDACTED_SECRET>`;
- abstract port roles such as `PANEL_PORT=<REDACTED>`.

Scan reports, fixtures, Git history, filenames, and patches. If provenance is uncertain, exclude the material and mark the evidence gap.
