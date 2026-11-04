#!/usr/bin/env python3
"""Validate the distributable package using only Python's standard library."""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "creator-outreach"
ERRORS = []

def require(condition, message):
    if not condition:
        ERRORS.append(message)

def main():
    required = [
        "README.md", "LICENSE", ".gitignore", ".github/workflows/validate.yml",
        "skills/creator-outreach/SKILL.md",
        "skills/creator-outreach/agents/openai.yaml",
        "skills/creator-outreach/references/research-and-fit.md",
        "skills/creator-outreach/references/pitches-and-followups.md",
        "skills/creator-outreach/references/pipeline.md",
        "skills/creator-outreach/assets/creator-brief.md",
        "skills/creator-outreach/assets/outreach-dossier.md",
        "skills/creator-outreach/assets/outreach-tracker.csv",
        "examples/manchester-artist/brief.md",
        "examples/manchester-artist/dossier.md",
        "examples/manchester-artist/outreach-tracker.csv",
        "evals/scenarios.json", "evals/README.md", "evals/RESULTS.md",
    ]
    for path in required:
        require((ROOT / path).is_file(), f"Missing {path}")
    if ERRORS:
        return finish()

    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    require(bool(match), "Missing skill frontmatter")
    if match:
        # This package deliberately uses only flat, plain-string frontmatter.
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(":")
            require(bool(sep) and key in {"name", "description"}, "Unexpected frontmatter field")
            require(key not in fields, f"Duplicate frontmatter key: {key}")
            fields[key] = value.strip()
        require(fields.get("name") == SKILL.name, "Skill name and directory differ")
        require(0 < len(fields.get("description", "")) <= 1024, "Invalid description length")
    require(len(text.splitlines()) < 500, "Skill exceeds progressive-disclosure line budget")
    require("[TODO:" not in text, "Unfinished template")
    metadata = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
    require("$creator-outreach" in metadata, "Default prompt must name skill")

    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts or ".eval-runs" in md.parts:
            continue
        body = md.read_text(encoding="utf-8")
        for target in re.findall(r"!?(?:\[[^\]]*\])\(([^\s)]+)\)", body):
            url = urlsplit(target)
            if url.scheme or target.startswith("#"):
                continue
            local = (md.parent / unquote(url.path)).resolve()
            require(local.is_relative_to(ROOT.resolve()), f"Link leaves repository: {md.relative_to(ROOT)} -> {target}")
            require(local.exists(), f"Broken link: {md.relative_to(ROOT)} -> {target}")

    with (SKILL / "assets/outreach-tracker.csv").open(newline="", encoding="utf-8") as f:
        header = next(csv.reader(f))
    require(len(header) == len(set(header)), "Duplicate tracker fields")
    for field in ["creator_id", "campaign_id", "brand_domain", "status", "suppression_scope", "send_provenance", "message_id"]:
        require(field in header, f"Missing tracker field {field}")
    with (ROOT / "examples/manchester-artist/outreach-tracker.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    require(rows[0] == header, "Example and template tracker contracts differ")
    require(len(rows) == 3, "Expected two example prospects")
    for line, row in enumerate(rows[1:], 2):
        require(len(row) == len(header), f"CSV row {line} is misaligned")
        if len(row) != len(header):
            continue
        item = dict(zip(header, row))
        require(item["status"] == "draft", "Example falsely advances draft state")
        for field in ["initial_sent_at", "last_contact_at", "next_action_date", "message_id", "send_provenance"]:
            require(not item[field], f"Example fabricates {field}")
        require(item["brand_domain"].endswith(".example"), "Example contains non-fictional brand domain")

    scenarios = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
    require(len(scenarios) >= 6, "Insufficient scenario coverage")
    ids = [s.get("id") for s in scenarios]
    require(len(ids) == len(set(ids)), "Duplicate scenario IDs")
    for scenario in scenarios:
        require(bool(scenario.get("prompt")), "Empty scenario prompt")
        require(len(scenario.get("checks", [])) >= 3, f"Incomplete rubric: {scenario.get('id')}")
    for md in (ROOT / "examples").rglob("*.md"):
        require("fictional" in md.read_text(encoding="utf-8").lower(), f"Unlabelled fictional example: {md}")
    return finish()

def finish():
    if ERRORS:
        for error in ERRORS:
            print("FAIL:", error)
        return 1
    print("PASS: skill structure, local links, metadata, tracker contract and six evaluation fixtures")
    print("These checks do not measure model behaviour or commercial outcomes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
