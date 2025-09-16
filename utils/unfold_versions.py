#!/usr/bin/env python3
"""
unfold_versions.py

Reads a JSON file with vendors/os_name/os_versions and generates a ready-to-label dataset JSON.
Output: list of objects with the requested structure, but with vulnerability fields empty (null/[]).

Usage:
  python create_firewall_dataset.py --input vendors.json --output dataset.json

Input format (vendors.json):
[
  {
    "vendor": "Cisco",
    "os_name": "ASA",
    "os_versions": ["9.8(4)", "9.9.1"]
  },
  ...
]

Output (dataset.json):
[
  {
    "id": "<uuid4>",
    "vendor": "Cisco",
    "os_name": "ASA",
    "os_version": "9.8(4)",
    "normalized_version": "9.8.4",
    "ground_truth_vulnerable": null,
    "ground_truth_cves": [],
    "confidence_label": null
  },
  ...
]
"""

import argparse
import json
import re
import uuid
from typing import List


def normalize_version(version: str) -> str:
    """Normalize versions to a basic numeric form.

    Strategy: extract numeric groups in order and join with dots.
    Examples:
      "9.8(4)" -> "9.8.4"
      "v1.2.3" -> "1.2.3"
      "1_2_3" -> "1.2.3"
      "9.8.4a" -> "9.8.4"

    If no numeric groups are found, clean the string (remove 'v' prefix) and return a simple alphanumeric part.
    """
    if not version or not isinstance(version, str):
        return ""

    v = version.strip()
    v = re.sub(r"^v", "", v, flags=re.IGNORECASE)

    nums = re.findall(r"\d+", v)
    if nums:
        return ".".join(nums)

    simple = re.sub(r"[\s\(\)]+", "", v)
    return simple


def build_entry(vendor: str, os_name: str, os_version: str) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "vendor": vendor,
        "os_name": os_name,
        "os_version": os_version,
        "normalized_version": normalize_version(os_version),
        # Fields to be filled manually
        "ground_truth_vulnerable": None,
        "ground_truth_cves": [],
        "confidence_label": None,
    }


def load_mappings(path: str) -> List[dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("Input file format not recognized: must be a list or JSON object")


def main():
    parser = argparse.ArgumentParser(description="Generate base firewall dataset for manual labeling")
    parser.add_argument("--input", "-i", required=True, help="Input JSON with vendors/os_name/os_versions")
    parser.add_argument("--output", "-o", required=True, help="Output JSON with the generated dataset")
    parser.add_argument("--append", "-a", action="store_true", help="If output file exists, append instead of overwrite")
    args = parser.parse_args()

    mappings = load_mappings(args.input)

    entries = []
    for item in mappings:
        vendor = item.get("vendor") or item.get("Vendor") or ""
        os_name = item.get("os_name") or item.get("os") or item.get("osName") or ""
        versions = item.get("os_versions") or item.get("os_versions") or item.get("osVersions") or []
        if not isinstance(versions, list):
            if isinstance(versions, str):
                versions = [v.strip() for v in versions.split(",") if v.strip()]
            else:
                versions = []

        for v in versions:
            entries.append(build_entry(vendor, os_name, v))

    if args.append:
        try:
            with open(args.output, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if isinstance(existing, list):
                entries = existing + entries
        except FileNotFoundError:
            pass

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(entries)} records in {args.output}")


if __name__ == "__main__":
    main()
