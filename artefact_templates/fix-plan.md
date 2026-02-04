
## 0. Meta

- Last updated: 2026-02-01T15:20:00Z
- Updated by: ralph-loop
- Source of truth: specs/*

## 1. High-priority items (do these first)

- [ ] BR-3 Magic link consume: implement single-use token semantics as per specs/features/magic_link_login.md.
- [ ] BR-2 Rate limiting: enforce per-email + per-IP limits with correct 429 behaviour.
- [ ] TESTING: Add unit tests for all BRs in magic_link_login spec (see Testing Strategy section).

## 2. Medium-priority items

- [ ] LOGGING: Add structured logs for token misuse (expired, already consumed).
- [ ] METRICS: Track number of requests and failures per endpoint.

## 3. Low-priority / Nice-to-have

- [ ] SECURITY: Consider revoking older tokens when a new one is issued (see Open Questions in spec).

## 4. Completed items (for traceability)

- [x] BR-1 Magic link request: issue tokens and send email with 15 min expiry.
  - Completed: 2026-02-01T14:00:00Z
  - Verified by: unit + integration tests in tests/auth/magic_link.test.ts
