---
type: progress
updated: 2026-08-11
---

# System Design Progress Tracker

Built organically — no pre-loaded curriculum. Concepts and questions are added only as
they're actually encountered and worked through.

## Current Position

- **Status**: started 2026-08-11 (day 33) — 1 question attempted, depth `partial`
- **Next**: Rate Limiter review #1 due 2026-08-12 (`[derive]`) — close the three
  open gaps in [rate-limiter.md](../questions/rate-limiter.md), above all the
  policy-vs-implementation disconnect. Then URL Shortener as case study 2.

## Case Study Sheet

Modeled on Alex Xu Vol 1+2 (read thoroughly ~2yr ago, corrected 2026-07-26
from earlier ~1.5yr estimate — treat as rusty prior exposure, verify at
interview speed, not a re-read task), ordered by real-interview frequency:

- [x] Rate Limiter — 2026-08-11, depth `partial` (3 gaps open)
- [ ] URL Shortener
- [ ] Chat System
- [ ] Notification System
- [ ] News Feed
- [ ] Web Crawler
- [ ] Key-Value Store
- [ ] Unique ID Generator
- [ ] Search Autocomplete
- [ ] Proximity Service (Nearby Friends)
- [ ] Google Maps
- [ ] Distributed Message Queue
- [ ] Metrics Monitoring System
- [ ] YouTube
- [ ] Google Drive
- [ ] Ad Click Event Aggregation
- [ ] Hotel Reservation System
- [ ] S3-like Object Storage
- [ ] Real-Time Gaming Leaderboard
- [ ] Payment System
- [ ] Digital Wallet
- [ ] Stock Exchange
- [ ] Ticket Booking System
- [ ] Distributed Email Service

## Concepts Covered

- [x] Rate Limiting Algorithms — [note](../concepts/rate-limiting-algorithms.md)
- [x] Shared Counter State Across N Instances — [note](../concepts/shared-counter-state.md)

_Format:_ `- [ ] Concept Name — [note](../concepts/concept-slug.md)`

## Questions Tackled

- [x] Rate Limiter — depth: partial — [note](../questions/rate-limiter.md) — 2026-08-11 17:47-18:27

_Format:_ `- [ ] Question Name — depth: shallow|full — [note](../questions/question-slug.md)`

## Notes for Next Session

- **2026-08-11 18:27** — Track opened after 33 days at zero. Rate Limiter run as
  cold draw, ~38 min, roughly real-loop pacing. Policy derivation was genuinely
  strong: the floor + shared-pool answer came out of four self-traced failure
  cases, not recall. Distributed-state reasoning (N x L breach, INCR race,
  fail-open load correlation) also solid.
- **The one thing to fix first**: the session produced a policy in its first
  half and an implementation in its second half that does not implement it. Open
  the review by connecting them, not by re-covering algorithms.
- **Cross-track signal confirmed**: mechanism cold, tradeoff/justification needs
  a second ask — 4 occurrences this session. This is the same pattern logged
  against DSA Greedy and is now confirmed as not DSA-specific. The working
  prescription transfers exactly: abstract question -> "I don't know";
  same question with concrete numbers -> correct derivation. Instantiate first.
- Alex Xu Vol 1 framing held up — this behaved like rusty prior exposure
  (pattern names recalled, underlying state not), not first exposure.
