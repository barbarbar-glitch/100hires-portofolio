# Cold Outreach Pipeline for B2B SaaS - Research Repo

This repository contains a structured research dataset to support building a practical cold outreach playbook for B2B SaaS.

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

## Collection approach

- YouTube: `yt-dlp` to locate relevant videos + `youtube-transcript-api` to pull transcript text.
- LinkedIn: public mirror retrieval (`r.jina.ai`) and parsing of recent activity pages where available.
- Collection methods and constraints are documented in `research/other/method.md`.

## Quick insights snapshot

- Top repeated theme: generic personalization fails; relevance from account signals performs better.
- Multi-channel orchestration (email + LinkedIn + calls) appears consistently stronger than single-channel.
- Message quality and offer clarity are still bigger levers than volume.
- AI helps speed research/drafting but needs strict human review for accuracy and tone.

## Notes and limitations

- LinkedIn has anti-bot/privacy controls; in some cases only shared/liked activity is visible in public mirrors.
- YouTube transcripts were successfully collected for all 10 experts.