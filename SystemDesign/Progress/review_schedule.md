---
type: review_schedule
updated: 2026-08-11
---

# Review Schedule Queue — System Design

Spaced repetition, compressed toward the front only when
`../../Progress/cycle.md` mode is `sprint` and an interval would land past
`target_end` (in that case: +1, +3, +7, +14, +21 days instead of the full
ladder). In `maintenance`/`dormant` mode use the full +1/+3/+7/+14/+30/+60/+90
ladder, same as DSA.

Same `[derive]`, `[leech]`, and graduation rules as
`../../DSA/Progress/review_schedule.md` apply here once entries exist — see
that file for the exact thresholds, not restated here to avoid drift between
the two copies.

## Graduated

_None yet._

## Upcoming Reviews

- Rate Limiter `[derive]` — due: 2026-08-12 — review #1 — [note](../questions/rate-limiter.md) — start with the "why", not the design: (1) why does per-customer-only fail AND global-only fail, (2) why is fail-open's standard rebuttal load-correlation, (3) why is the error bounded by bucket size. Then the unbuilt half: how do the Redis counters actually implement the floor + shared-pool policy?

_Format:_ `- Concept/Question Name — due: YYYY-MM-DD — review #N — [note](../concepts-or-questions/slug.md)`

## Completed Reviews Log

_None yet._
