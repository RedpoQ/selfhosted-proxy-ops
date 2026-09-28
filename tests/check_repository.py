#!/usr/bin/env python3
"""Read-only static validation for the portable skills repository."""

from __future__ import annotations

import ipaddress
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_SKILL_COUNT = 8
TEST_NETS = tuple(
    ipaddress.ip_network(value)
    for value in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")
)


def repository_files() -> list[Path]:
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def markdown_links(path: Path, text: str) -> list[Path]:
    targets: list[Path] = []
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = raw.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        targets.append((path.parent / unquote(target)).resolve())
    return targets


def frontmatter_name(path: Path, text: str) -> str | None:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return None
    name = re.search(r"(?m)^name:\s*([^#\n]+?)\s*$", match.group(1))
    return name.group(1).strip(" '\"") if name else None


def main() -> int:
    errors: list[str] = []
    files = repository_files()

    try:
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        if "skills" in manifest:
            errors.append("plugin.json retains legacy 'skills' field")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"plugin.json parse failed: {exc}")

    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if len(skill_dirs) != EXPECTED_SKILL_COUNT:
        errors.append(f"expected {EXPECTED_SKILL_COUNT} skill directories, found {len(skill_dirs)}")

    names: list[str] = []
    for directory in skill_dirs:
        entrypoint = directory / "SKILL.md"
        if not entrypoint.is_file():
            errors.append(f"missing {entrypoint.relative_to(ROOT)}")
            continue
        text = entrypoint.read_text(encoding="utf-8")
        name = frontmatter_name(entrypoint, text)
        if name != directory.name:
            errors.append(f"frontmatter name mismatch: {directory.name!r} != {name!r}")
        if name:
            names.append(name)
    if len(names) != len(set(names)):
        errors.append("skill frontmatter names are not unique")

    for path in files:
        data = path.read_bytes()
        relative = path.relative_to(ROOT)
        if not data:
            errors.append(f"empty file: {relative}")
            continue
        if b"\x00" in data:
            errors.append(f"binary/null content: {relative}")
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 file: {relative}")
            continue

        if path.suffix.lower() == ".md":
            for target in markdown_links(path, text):
                if not target.exists():
                    errors.append(f"broken link in {relative}: {target}")

        private_key_marker = "-----" + r"BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"
        if re.search(private_key_marker, text):
            errors.append(f"private-key marker: {relative}")
        if re.search(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", text):
            errors.append(f"UUID pattern: {relative}")
        if re.search(r"(?i)\b[A-Z]:\\Users\\(?!<|example\b|user\b)[^\\\s]+", text):
            errors.append(f"local Windows user path: {relative}")

        for key, value in re.findall(
            r"(?im)\b(password|passwd|token|secret|private[_-]?key|uuid)\s*[:=]\s*([^\s,;]+)",
            text,
        ):
            normalized = value.strip("'\"`<>[]{}()").upper()
            if normalized not in {"", "SECRET", "REDACTED", "REDACTED_SECRET", "EXAMPLE", "NONE", "UNKNOWN"}:
                errors.append(f"suspicious {key} assignment in {relative}")

        for literal in re.findall(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])", text):
            try:
                address = ipaddress.ip_address(literal)
            except ValueError:
                continue
            allowed = (
                address.is_private
                or address.is_loopback
                or address.is_link_local
                or any(address in network for network in TEST_NETS)
            )
            if not allowed:
                errors.append(f"non-documentation public IPv4 {literal} in {relative}")

    activation = (ROOT / "tests" / "activation" / "cases.md").read_text(encoding="utf-8")
    boundary = (ROOT / "tests" / "boundary" / "cases.md").read_text(encoding="utf-8")
    activation_count = len(re.findall(r"(?m)^##\s+\d+\.", activation))
    boundary_count = len(re.findall(r"(?m)^##\s+\d+\.", boundary))
    if activation_count != 8:
        errors.append(f"expected 8 activation cases, found {activation_count}")
    required_cases = (
        "Cloudflare architecture decision",
        "Cloudflare edge experiment",
        "Region purchase decision",
        "Transport comparison on accepted VPS",
        "Special egress in 3X-UI",
        "Client-local rule mismatch",
        "Server special-route leak",
        "Unsupported control-plane adapter",
        "Linux desktop DNS and TUN",
        "Unverified OpenWrt automation",
    )
    for heading in required_cases:
        if heading not in boundary:
            errors.append(f"missing boundary case: {heading}")

    if errors:
        print("STATIC_REPOSITORY_CHECK=FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("STATIC_REPOSITORY_CHECK=PASS")
    print(f"SKILL_COUNT={len(skill_dirs)}")
    print(f"ACTIVATION_CASE_COUNT={activation_count}")
    print(f"BOUNDARY_CASE_COUNT={boundary_count}")
    print(f"FILE_COUNT={len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
