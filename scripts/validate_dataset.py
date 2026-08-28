#!/usr/bin/env python3
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "demo" / "evaluation-dataset.jsonl"
count = 0
with path.open(encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if "query" not in row:
            raise ValueError(f"Line {i}: missing query")
        count += 1
print(f"OK: {count} rows validated.")
