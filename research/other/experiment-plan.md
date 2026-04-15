# Outbound Experiment Plan (v1)

## Objective
Validate whether signal-based, persona-specific outreach increases positive replies and meetings compared to a baseline outbound sequence.

## Primary hypothesis
If outreach is triggered by account/persona signals and delivered through a 7-touch multi-channel sequence, then positive reply rate and meeting-booked rate will improve vs baseline.

## Test design
- **Duration:** 2 weeks initial pilot
- **Population:** 120 target accounts (split by tier/persona)
- **Groups:**
  - Control (baseline messaging/sequence): 60 accounts
  - Test (playbook-v1 messaging/sequence): 60 accounts

## Variables
- **Independent variables:**
  - Message opening strategy (generic vs signal-led)
  - CTA style (meeting ask vs async asset offer)
  - Sequence pacing (standard vs optimized follow-up timing)
- **Dependent variables:**
  - Positive reply rate
  - Meetings booked
  - Show rate
  - Meeting-to-opportunity conversion

## Success criteria
- +20% relative lift in positive reply rate (test vs control)
- +15% relative lift in meetings booked (test vs control)
- No decline in show rate

## Sample assumptions
- Assumes sufficient outreach volume to reach at least:
  - 30 contacts per persona track in each group
  - 3+ touches minimum delivered per contact

## Instrumentation
- Track all touches by account, persona, and sequence step.
- Label each reply as positive/neutral/negative.
- Log meeting outcomes and next-stage movement.

## Review cadence
- **Midpoint check (end of week 1):** detect broken variants; fix operational issues only.
- **Final review (end of week 2):** compare group-level outcomes and segment-level patterns.

## Stop/scale rules
- **Scale:** if primary success criteria are met and quality is stable.
- **Iterate:** if one metric improves but another regresses (e.g., replies up, shows down).
- **Stop:** if test underperforms on both positive replies and meetings after full run.

## Risks
- Uneven persona distribution can skew results.
- Data quality issues in LinkedIn visibility may affect signal precision.
- Rep execution variance may hide messaging effects.

## Next iteration
- Narrow to top-performing persona + trigger combinations.
- Add second test on subject line and first-line personalization depth.
- Incorporate weekly win/loss examples into message library.
