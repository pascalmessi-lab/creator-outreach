# Validation notes

Date: 2026-11-04. Stage: early release for user feedback.

## Current revision

- Quick mode stays lightweight even for five requested brands; a tracker update does not force a full campaign dossier.
- Timing hooks are optional when unsupported. Follow-up cadence has one authoritative home in the pipeline reference.
- Added direct-brand, agency and platform routing, an illustrative deliverable menu, clarified usage permissions and linked official UK disclosure sources.
- Updated the README and supplied a second fictional example with a precise analytics proof point and launch deadline.

## Checks actually run

- The skill-creator package's original `quick_validate.py` passed the final skill folder's frontmatter and naming checks.
- `python3 tools/validate_repository.py` passed package structure, local links, metadata, the published example CSV and evaluation-fixture checks.
- Eight fresh-session behavioural scenarios were run against the revised skill. The author inspected the outputs against their written checks; all eight met those checks in these runs. Generated CSV blocks were also parsed for column alignment.
- Two paired draft tasks were run with and without project-specific skill instructions. A separate fresh agent rated blinded recipient-facing excerpts: one task tied at 9/10, with a preference for the skill's next-step asks; the launch task scored 10/10 with the skill versus 8/10 without.

Read the [full method, limitations and raw records](runs/early-release/README.md). The comparison used one generation per condition and one agent rater, not a human panel or an independently validated benchmark. It does not establish consistent improvement or commercial outcomes.

## What is still untested

- Native installation end to end in Claude Code, Codex, ChatGPT and other products; direct skill-path invocation is not an installation test.
- Live brand research and social-profile access.
- Real email/CRM connections, delivery, scheduling, replies or signed partnerships.
- Repeated-run reliability, human preference and a creator/manager user pilot.

The earlier development evidence is preserved in [the previous revision](https://github.com/pascalmessi-lab/creator-outreach/blob/2f4eb59026704f60732a26c51eb05b1789a35327/evals/RESULTS.md). The current runs supersede its pending six-scenario and paired-comparison items; they do not remove the remaining limits above.
