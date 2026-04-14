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
- Matthew Putnam
- Kris Rudeegraap

## What was collected

- `research/sources.md`: master source list with links, rationale, and collection notes
- `research/linkedin-posts/`: one file per author for recent LinkedIn activity capture
- `research/youtube-transcripts/`: one transcript per expert, collected via API tooling
- `research/other/`: machine-readable manifests for reproducibility

## Collection approach

- YouTube: `yt-dlp` to locate relevant videos + `youtube-transcript-api` to pull transcript text.
- LinkedIn: public mirror retrieval (`r.jina.ai`) and parsing of recent activity pages where available.

## Notes and limitations

- LinkedIn has anti-bot/privacy controls, so some profiles did not expose recent activity in the public mirror.
- YouTube transcripts were successfully collected for all 10 experts.