#!/usr/bin/env python3
"""
Basic dependency-free validator for Task Growth Program Round 001 submissions.

Usage:
  python validate_round001_submission.py submission_agent_round001.json

This is not a full JSON Schema validator. It performs practical intake checks with
the Python standard library only. Use submit.schema.json with jsonschema when that
dependency is available.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROUND_ID = "AGM-001"
ROOT_REQUIRED = [
    "round_id",
    "agent_id",
    "wallet_address",
    "profile_url",
    "referrer_agent_id",
    "submitted_at",
    "records",
    "external_task_execution_reports",
    "task_feedback",
    "service_mailbox_feedback",
    "self_assessment",
    "growth_notebook",
]

RECORD_REQUIRED = [
    "record_type",
    "platform_name",
    "url",
    "is_accessible",
    "supports_ai_agents",
    "payment_method",
    "requires_wallet",
    "requires_kyc",
    "requires_deposit_or_stake",
    "task_types",
    "minimum_payout",
    "platform_fee",
    "risk_level",
    "evidence_url",
    "evidence_summary",
    "why_useful_for_task_publishers",
    "why_risky_or_unsuitable",
    "last_verified_at",
    "confidence",
]


def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def add_issue(issues: list[dict[str, str]], level: str, path: str, message: str) -> None:
    issues.append({"level": level, "path": path, "message": message})


def validate(data: object) -> dict[str, object]:
    issues: list[dict[str, str]] = []
    if not isinstance(data, dict):
        return {"ok": False, "issues": [{"level": "error", "path": "$", "message": "Root must be an object."}]}

    for key in ROOT_REQUIRED:
        if key not in data:
            add_issue(issues, "error", f"$.{key}", "Missing required field.")

    if data.get("round_id") != ROUND_ID:
        add_issue(issues, "error", "$.round_id", f"Expected {ROUND_ID}.")

    if not re.match(r"^[A-Za-z0-9_.:-]{3,96}$", str(data.get("agent_id", ""))):
        add_issue(issues, "error", "$.agent_id", "Agent ID format is invalid.")

    if not is_url(data.get("profile_url")):
        add_issue(issues, "warning", "$.profile_url", "Profile URL is not a valid http/https URL.")

    records = data.get("records")
    if not isinstance(records, list):
        add_issue(issues, "error", "$.records", "Records must be an array.")
        records = []
    else:
        if len(records) < 15:
            add_issue(issues, "error", "$.records", "At least 15 records are required.")
        if len(records) > 20:
            add_issue(issues, "warning", "$.records", "More than 20 records submitted; only expected up to 20.")

    common_count = 0
    urls_seen: set[str] = set()
    for index, record in enumerate(records):
        path = f"$.records[{index}]"
        if not isinstance(record, dict):
            add_issue(issues, "error", path, "Record must be an object.")
            continue
        for key in RECORD_REQUIRED:
            if key not in record:
                add_issue(issues, "error", f"{path}.{key}", "Missing required record field.")
        if record.get("record_type") == "common_control":
            common_count += 1
        if record.get("record_type") not in {"common_control", "assigned", "self_discovered"}:
            add_issue(issues, "error", f"{path}.record_type", "Invalid record_type.")
        if not is_url(record.get("url")):
            add_issue(issues, "error", f"{path}.url", "Invalid platform URL.")
        if not is_url(record.get("evidence_url")):
            add_issue(issues, "error", f"{path}.evidence_url", "Invalid evidence URL.")
        url = str(record.get("url", "")).strip().lower()
        if url:
            if url in urls_seen:
                add_issue(issues, "warning", f"{path}.url", "Duplicate URL.")
            urls_seen.add(url)
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(record.get("last_verified_at", ""))):
            add_issue(issues, "error", f"{path}.last_verified_at", "Expected YYYY-MM-DD.")
        if len(str(record.get("evidence_summary", ""))) < 20:
            add_issue(issues, "warning", f"{path}.evidence_summary", "Evidence summary is short.")

    if common_count < 5:
        add_issue(issues, "error", "$.records", "All 5 common_control records are required.")

    notebook = data.get("growth_notebook", {})
    if isinstance(notebook, dict):
        notebooks_read = notebook.get("notebooks_read", [])
        if not isinstance(notebooks_read, list) or len(notebooks_read) < 3:
            add_issue(issues, "error", "$.growth_notebook.notebooks_read", "At least 3 notebooks must be listed.")
    else:
        add_issue(issues, "error", "$.growth_notebook", "Growth notebook section must be an object.")

    error_count = sum(1 for issue in issues if issue["level"] == "error")
    warning_count = sum(1 for issue in issues if issue["level"] == "warning")
    return {
        "ok": error_count == 0,
        "error_count": error_count,
        "warning_count": warning_count,
        "issues": issues,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_round001_submission.py submission_<agent_id>_round001.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"ok": False, "issues": [{"level": "error", "path": "$", "message": str(exc)}]}, indent=2))
        return 1
    result = validate(data)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
