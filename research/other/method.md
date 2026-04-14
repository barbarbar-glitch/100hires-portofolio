# Collection Method

## Goal
Build a high-signal research set for a future B2B SaaS cold outreach playbook.

## Data sources
- LinkedIn recent activity pages (public mirror route via `r.jina.ai`).
- YouTube videos and transcripts (via `yt-dlp` + `youtube-transcript-api`).

## Process
1. Select 10 practitioners with consistent outbound/GTM execution content.
2. For each expert, collect:
   - 1 relevant YouTube transcript.
   - 2-3 recent LinkedIn activity items (prioritizing authored posts when available).
3. Save artifacts into:
   - `research/linkedin-posts/`
   - `research/youtube-transcripts/`
   - `research/other/*manifest.json`
4. Record expert rationale and source links in `research/sources.md`.

## Quality controls used
- Preference for experts with operator background (pipeline ownership, outbound leadership, SDR enablement, or GTM execution).
- Avoided generic motivational sources as primary data.
- Logged collection date in author files for traceability.

## Known limitations
- LinkedIn anti-bot/privacy controls can restrict full post visibility.
- Some mirrored activity streams include likes/shares mixed with authored posts.
- YouTube search may surface interviews/podcasts; relevance was filtered manually by title/topic.
