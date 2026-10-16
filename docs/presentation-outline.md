# 10-minute presentation outline

1. **0:00–0:45 — Problem and assumptions:** explain the lightweight social MVP, audience and scope.
2. **0:45–1:45 — Requirements:** show FR/NFR IDs and mandatory acceptance criteria.
3. **1:45–2:30 — Methodology and board:** explain Kanban; show your real board and task status (create/update it before presenting).
4. **2:30–3:30 — Architecture and ADR:** monolith, Flask, SQLite volume, and trade-offs.
5. **3:30–6:30 — Live product demo:** register a user, log in, create a post, show author/date/newest-first feed, log out, show protected posting.
6. **6:30–7:30 — Persistence and Docker:** explain Compose and named volume; optionally restart the container and verify the post remains.
7. **7:30–8:30 — Testing and CI:** run `pytest -q`; show the actual successful GitHub Actions run.
8. **8:30–9:30 — Limitations and future work:** CSRF, rate limiting, PostgreSQL for scale, and optional progressive deployment.
9. **9:30–10:00 — Close:** summarize acceptance criteria met and key engineering decisions.

Do not claim that a remote board, GitHub repository or CI run exists until you have created it and captured real evidence.
