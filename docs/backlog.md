# Prioritized Product Backlog

**Suggested board columns:** Backlog → To Do → In Progress → Review / Testing → Done  
**Initial statuses below are proposed, not evidence of a remotely updated board.** Import these as GitHub issues and maintain the real board.

| ID | Epic / story | Acceptance criteria | Priority | Initial status | Estimate |
|---|---|---|---|---|---|
| US-01 | As a visitor, I can create an account | Valid username/password accepted; duplicate/invalid input rejected | P0 | To Do | 3 |
| US-02 | As a user, I can log in and log out | Valid credentials create session; logout clears session | P0 | To Do | 3 |
| US-03 | As a visitor, I can read the timeline | Author, text and date visible; newest first; empty state | P0 | To Do | 3 |
| US-04 | As a signed-in user, I can publish a post | 1–280 characters accepted; invalid post rejected; post appears in feed | P0 | To Do | 3 |
| US-05 | As a user, my data persists | Users/posts survive container restart with named volume retained | P0 | To Do | 2 |
| US-06 | As a lecturer, I can run the app locally | Docker Compose builds and starts app at localhost:5000 | P0 | To Do | 3 |
| US-07 | As a developer, I get automated quality feedback | CI installs dependencies, tests and builds image on push/PR | P0 | To Do | 3 |
| US-08 | As a reviewer, I can understand the design | Requirements, architecture and ADR explain decisions/trade-offs | P1 | To Do | 2 |
| US-09 | As a user, I can use the app on mobile | Layout remains usable at narrow viewport widths | P1 | To Do | 2 |
| US-10 | As a presenter, I can demonstrate the MVP | 10-minute walkthrough rehearsed; real CI evidence captured | P1 | To Do | 2 |
| US-11 | As a maintainer, I can plan future progressive delivery | Document how blue-green/canary could be added; no production deployment claimed | P2 | Backlog | 2 |

## Suggested task breakdown
- Foundation: repo, requirements, assumptions, project board, architecture.
- Identity: registration validation, password hashing, login/logout, tests.
- Posts: create endpoint, ordered feed, timestamp display, tests.
- Delivery: Docker image/Compose volume, health endpoint, CI, README.
- Submission: board updates, CI screenshot/link, presentation rehearsal.

## Board setup instructions
1. Create a GitHub repository for this project.
2. Open **Projects → New project** and choose a board layout.
3. Create the five columns above.
4. Add each US-xx as an issue, copy its acceptance criteria, and set priority labels.
5. Move cards only when work actually changes status. Link PRs/commits and keep evidence.
