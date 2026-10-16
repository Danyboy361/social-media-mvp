# Methodology Selection — Lightweight Kanban

## Decision
Use Kanban with a prioritized backlog and a continuous flow through **Backlog → To Do → In Progress → Review / Testing → Done**.

## Why it fits
- The team may consist of one or two students, so a lightweight workflow avoids the overhead of formal Scrum roles and ceremonies.
- Requirements are intentionally incomplete. Kanban allows assumptions to be recorded and revised as the MVP is tested.
- The delivery window is short; the mandatory requirements can be prioritized ahead of optional features.
- Work can be reviewed continuously and linked to Git commits, pull requests and test evidence.

## Working agreements
1. Keep tasks small enough to complete in a focused work session.
2. Prioritize mandatory acceptance criteria before polish or extras.
3. Limit In Progress to two tasks for an individual (or three for a pair).
4. Each task has acceptance criteria and a definition of done.
5. A task is Done only when its acceptance criteria are checked, relevant tests pass, and documentation is updated.
6. Review the board at the start and end of each work session; note blockers and re-prioritize.

## Definition of Done
- Code is committed with a meaningful message.
- Acceptance criteria are met and automated tests pass.
- Docker/local run instructions remain accurate.
- Relevant documentation is updated.
- CI is green after pushing to GitHub.

## Review cadence
Use a brief planning/review session each work session, and a final end-to-end rehearsal before presentation. The actual board must be created and maintained in GitHub Projects/Trello by the student; the backlog starter is in `backlog.md`.
