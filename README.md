# Chirp — Social Media MVP

Chirp is a lightweight Twitter/X-style web MVP for the Software Engineering Workshop assessment. It supports account registration, login/logout, a public newest-first feed, authenticated post creation, persistent storage, Docker Compose and GitHub Actions CI.

## Features
- Register and sign in with Werkzeug password hashing (scrypt by default).
- Sign out and session-protected post creation.
- Feed shows author, content and UTC creation timestamp; newest first.
- Post length validation (1–280 characters); username validation and duplicate protection.
- SQLite data stored in a Docker named volume.
- Health endpoint at `/health`; automated tests and container build in CI.

## Run locally with Docker
Prerequisites: Docker Engine/Desktop with the Compose plugin.

```bash
cp .env.example .env
# Edit .env and replace APP_SECRET_KEY with a long random secret.
docker compose up --build
```

Open http://localhost:5000. Stop with `Ctrl+C`; use `docker compose down` to stop and remove containers. The named volume survives ordinary restarts and `docker compose down`. **Do not run `docker compose down -v` unless you intend to delete the database volume.**

The default key in Compose is for local demonstration only. Set a strong random `APP_SECRET_KEY` in `.env` before sharing or deploying. Never commit `.env`.

## Run tests without Docker
Python 3.12+ recommended.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\\Scripts\\Activate.ps1
pip install -r requirements-dev.txt
pytest -q
```

The test suite uses a temporary SQLite database and does not touch the persisted local database.

## Configuration

| Variable | Purpose | Example |
|---|---|---|
| `APP_SECRET_KEY` | Signs Flask sessions; replace before non-local use | long random value |
| `DATABASE_PATH` | SQLite file location | `/data/social.db` |
| `PORT` | Development server port | `5000` |

## Architecture
A small monolithic Flask application serves HTML templates and handles authentication and posts. SQLite is appropriate for a locally demonstrable MVP; the Docker named volume retains data across container replacement. See `docs/architecture.md` and `docs/adr-001-stack.md`.

## Project planning
The prioritized backlog is in `docs/backlog.md`; import or recreate these tasks in GitHub Projects/Trello and update statuses during development. A project board must be created in your own GitHub account; this starter cannot truthfully claim a board was created remotely.

## CI
`.github/workflows/ci.yml` runs on pushes and pull requests, installs dependencies, runs pytest, and builds a Docker image. After pushing this repository to GitHub, open **Actions** and verify the run succeeds; include a screenshot or link to the real run in your submission.

## Deployment strategy demo reference
The supplied blue-green/canary example is a deployment-strategy guide, not the application brief itself. The assessment's mandatory deliverable is a locally runnable Docker MVP and CI. Blue-green/canary deployment is an optional extension and is not configured by this starter. See `docs/deployment-notes.md` for how it could be added.

## Known limitations / next steps
- This is an educational MVP, not production-hardened: add CSRF protection, rate limiting, email verification, password reset, security headers, and stronger operational logging before public deployment.
- SQLite is intended for the single-instance local demo; consider PostgreSQL for multi-instance deployment.
- The feed shows the latest 100 posts; pagination, follows, likes, replies and moderation are out of scope.
- The current UI formats ISO timestamps as stored UTC values; locale-aware formatting can be added.

## Assessment evidence checklist
- [ ] Push source to your own GitHub repository.
- [ ] Create and maintain a GitHub Projects board; add backlog issues and link them to commits/PRs.
- [ ] Confirm CI succeeds on GitHub and capture evidence.
- [ ] Run `docker compose up --build` and demonstrate register → login → post → feed → logout.
- [ ] Explain the architecture, ADR and limitations in the presentation.
- [ ] Disclose AI assistance according to your institution's academic integrity policy.
