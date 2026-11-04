# Creator Outreach

**Find the fit. Develop the idea. Make a credible pitch.**

A portable AI skill for creators, artists and talent managers approaching brands for partnerships. Turn a creator profile into a researched shortlist, specific campaign ideas, tailored outreach and an organised pipeline.

Created by [Pascal Messi](https://github.com/pascalmessi-lab), inspired by managing an artist and content creator and preparing brand outreach in Manchester and across the UK.

## Try this

> I manage an artist who makes illustrated portraits and behind-the-scenes videos in Manchester. Use Creator Outreach to find five suitable UK brands for paid collaborations, explain each match, and draft pitches for the best three. Use only the metrics and profile links I supply. Prepare the outreach; do not send it.

The skill establishes the creator's actual work, goals and constraints, then uses available research tools or supplied materials to produce an outreach dossier and a CSV tracker. Facts, proposed ideas and actual actions stay distinct.

No followers? No media kit? Start with actual work and a clear collaboration idea. Metrics are optional, not an invitation to invent them.

## What you get

| Part | What it adds |
|---|---|
| Creator brief | One profile for an individual, or reusable profiles for a roster |
| Brand qualification | Explicit exclusions, supported fit reasons and visible unknowns |
| Partnership concepts | A specific creative deliverable for each recommended match |
| Pitches | Subject options, tailored emails and optional short DMs |
| Follow-ups and replies | Thread-aware next steps preserving the original goal |
| Outreach state | A CSV tracker distinguishing drafts, sends, replies and closed threads |

Browse the [fictional worked example](examples/manchester-artist/dossier.md) or start with the [creator brief](skills/creator-outreach/assets/creator-brief.md).

## Install in a skills-compatible agent

This repository follows the open [Agent Skills specification](https://agentskills.io/specification). Install the complete skill folder, including supporting files.

### Skills CLI

With Node.js and the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add pascalmessi-lab/creator-outreach --skill creator-outreach
```

Choose your agent when prompted. The CLI manages supported installation locations. Inspect third-party skills before installing them.

### Claude Code — manual

Copy `skills/creator-outreach/` into your project's `.claude/skills/` directory. The entry point should be `.claude/skills/creator-outreach/SKILL.md`. For personal installation, use the personal skill location documented by Claude Code.

Then invoke:

```text
/creator-outreach Draft brand partnership pitches using my attached creator brief.
```

See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

### Codex and other compatible agents

Use the Skills CLI or your host's documented import process. The portable entry point is `skills/creator-outreach/SKILL.md`; `agents/openai.yaml` supplies optional OpenAI interface metadata.

In a host supporting dollar-prefixed invocation:

```text
Use $creator-outreach to research brands and prepare pitches using my creator brief.
```

### Chat interfaces without native skill installation

Use the skill instructions and referenced files as project/reference material, and explicitly ask the assistant to apply them. This is a manual workflow, not native installation, and does not give the assistant new browsing, file or email capabilities. Import options vary by product, account and workspace; use your host's current instructions.

## Capabilities and dependencies

The core skill is Markdown, CSV and optional UI metadata. It requires no API key, paid outreach database, MCP server or Python runtime.

| Available tools | Behaviour |
|---|---|
| Browsing/search | Research public brands and business contact routes; record sources and dates |
| No browsing | Use supplied materials, label provenance and avoid freshness claims |
| File tools | Save a Markdown dossier and CSV tracker in your working location |
| No file tools | Return copyable content |
| Email/CRM tools | Use only when explicitly requested and supported by host policies |
| No email/CRM tools | Prepare drafts and manual next steps |

The skill does not unlock private analytics, prove email deliverability, send email by itself, schedule background follow-ups or guarantee partnerships. Those capabilities need actual tools, evidence and user instructions.

## A practical first run

1. Fill in the [creator brief](skills/creator-outreach/assets/creator-brief.md). Leave unknown metrics blank.
2. Give it to your assistant with your desired collaboration type and market.
3. Request a small shortlist and pitches. Add an existing tracker if you have one.
4. Check the fit, terms and links before sending. Request sending separately if supported.
5. Bring replies and the current tracker back for the next action.

Useful prompts:

- **Solo creator:** “Find three art-supply brands that fit this portfolio. I want paid content, not gifted collaborations.”
- **Talent manager:** “Match these four creators to the supplied brand list. Coordinate one approach per brand and flag existing conflicts.”
- **Draft only:** “Use the attached brand brief and creator profile to draft one email and one short DM. Don't invent metrics.”
- **Follow-up:** “Review this tracker and these replies. Which threads need a response? Draft the next messages without sending.”
- **Commercial reply:** “The brand offered gifting, but our goal was a paid video. Draft a polite reply preserving that goal.”

## Privacy and action boundaries

Public examples are fictional. Keep real analytics, rate cards, contact lists, replies and credentials in your own working files. The `.gitignore` excludes common output/private folders, but does not replace reviewing what you publish.

Research and drafting do not authorise sending. The skill respects recipient resolution, existing permissions, opt-outs and host action policies. It never needs your email password.

## Validation and limitations

Run the dependency-free repository checks:

```bash
python3 tools/validate_repository.py
```

These check structure, local Markdown links, the CSV contract and evaluation fixtures. They do not measure model quality. See [evaluation scenarios](evals/README.md) and [validation notes](evals/RESULTS.md) for evidence and remaining gaps.

Compatibility is a design target, not a claim of live testing across every AI product. Installation, browsing quality, link accessibility and model adherence vary. Evaluate the skill in your own host before using it with real outreach.

## Contribute

Useful contributions include anonymised failure cases, better qualification examples, installation fixes and documented evaluation runs. Open an issue with the host/model, reproducible prompt, expected behaviour and actual behaviour. Use fictional or redacted inputs; do not post private client information.

This is a focused outreach skill, not an autonomous email campaign service. Start with a few relevant prospects and improve it from real feedback.

MIT licensed. Use, adapt and redistribute it with the licence notice.
