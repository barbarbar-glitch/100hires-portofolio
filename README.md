# Cold Outreach Pipeline for B2B SaaS - Research Repo

This repository contains a structured research dataset to support building a practical cold outreach playbook for B2B SaaS.

## Business context

The target use case is outbound pipeline creation for B2B SaaS teams that need repeatable meeting generation without relying on generic cold email volume.

## Why these experts

I prioritized practitioners who actively run outbound motions (not just theorists), including founders, outbound trainers, and GTM operators who regularly share tactical examples.

Selected experts:
- Nick Abraham
- Will Allred
- Jason Bay
- Josh Braun
- Belal Batrawy
- Morgan J Ingram
- Alex Hormozi
- Vin Matano
- Kyle Coleman
- Kris Rudeegraap

## What was collected

- `research/sources.md`: master source list with links, rationale, and collection notes
- `research/linkedin-posts/`: one file per author for recent LinkedIn activity capture
- `research/youtube-transcripts/`: one transcript per expert, collected via API tooling
- `research/other/`: machine-readable manifests for reproducibility

## Repository architecture

| Folder | Purpose | Output quality |
| --- | --- | --- |
| `research/linkedin-posts/` | Per-author activity capture and tactical annotation | Mixed authored/shared/liked visibility due to platform limits |
| `research/youtube-transcripts/` | Long-form source transcripts for frameworks and messaging | High signal for tactics, examples, and process language |
| `research/other/` | Method docs, manifests, synthesis, and playbook artifacts | Implementation-ready planning materials |
| `research/sources.md` | Master source index and rationale | Reviewer-friendly traceability |

## Method

- YouTube: `yt-dlp` to locate relevant videos + `youtube-transcript-api` to pull transcript text.
- LinkedIn: public mirror retrieval (`r.jina.ai`) and parsing of recent activity pages where available.
- Collection methods and constraints are documented in `research/other/method.md`.

## API and tooling proof

- Created a local virtual environment and installed: `youtube-transcript-api`, `yt-dlp`.
- Used `yt-dlp` search to find relevant videos per expert and extract metadata.
- Used `youtube-transcript-api` to pull transcript text for each selected video ID.
- Used `r.jina.ai` fetch wrappers for LinkedIn public activity mirror pages.
- Generated and refreshed machine-readable manifests:
  - `research/other/linkedin_manifest.json`
  - `research/other/youtube_manifest.json`
- Verified manifest consistency against actual files in:
  - `research/linkedin-posts/`
  - `research/youtube-transcripts/`

## Deliverables

- `research/other/executive-brief.md` (decision-level summary)
- `research/other/playbook-v1.md` (actionable outbound operating model)
- `research/other/experiment-plan.md` (test design with measurable criteria)
- `research/other/evidence-map.md` (traceability from recommendations to sources)
- `research/other/playbook-outline.md` (supporting draft and examples)

## Outcome

- Built a 10-expert research corpus across LinkedIn + YouTube.
- Converted source material into an actionable outbound playbook structure.
- Added evidence mapping and experiment design so the work can move from research to execution.

## How to reproduce

1. Create environment: `python3 -m venv .venv`
2. Install deps: `./.venv/bin/python -m pip install youtube-transcript-api yt-dlp`
3. Run collection scripts (examples): `samples/create_session.py`, `scrape_linkedin.py`
4. Generate/refresh manifests in `research/other/` after updates.
5. Review outputs in `research/linkedin-posts/` and `research/youtube-transcripts/`.

## Quick insights snapshot

- Top repeated theme: generic personalization fails; relevance from account signals performs better.
- Multi-channel orchestration (email + LinkedIn + calls) appears consistently stronger than single-channel.
- Message quality and offer clarity are still bigger levers than volume.
- AI helps speed research/drafting but needs strict human review for accuracy and tone.

## Notes and limitations

- LinkedIn has anti-bot/privacy controls; in some cases only shared/liked activity is visible in public mirrors.
- YouTube transcripts were successfully collected for all 10 experts.
- A draft playbook structure based on this dataset is in `research/other/playbook-outline.md`.

## Next steps

- Run a 2-week pilot using the sequence and experiment plan.
- Track positive replies and meetings booked by segment.
- Iterate message variants weekly based on response quality, not only activity volume.