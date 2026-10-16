# ADR-001: Flask monolith with SQLite

- **Status:** Accepted for MVP
- **Date:** 2026-10-08

## Context
The assessment requires account registration, login/logout, a shared post feed, post creation, persistent data, a Docker-based local run and CI. Delivery time is limited and the solution must be easy for a lecturer to clone and run.

## Decision
Use Python 3.12, Flask, Jinja templates, Werkzeug password hashing, SQLite, Gunicorn and Docker Compose. Persist the database in a named Docker volume. Use pytest and GitHub Actions for automated verification.

## Alternatives considered
1. **Node.js/Express + PostgreSQL:** widely used and robust, but adds a separate database service and more configuration for a small local demo.
2. **Django + PostgreSQL:** provides batteries-included authentication and ORM, but has more framework structure than needed for this small MVP.
3. **Microservices:** separates identity and posts but adds service discovery, networking and deployment complexity without a clear MVP benefit.

## Consequences
### Positive
- One application container and one persistent volume are simple to start locally.
- Python/Flask code is small and easy to inspect.
- SQLite requires no separate database container.
- Password hashing and route protection can be tested directly.

### Negative / risks
- SQLite is a single-instance choice; horizontal scaling and concurrent writes are limited.
- The educational implementation needs additional production controls (CSRF, rate limiting, security headers, monitoring, secret management).
- A default development secret must never be used for a public deployment.

## Revisit when
The application needs multiple web replicas, substantial write concurrency, managed backups, or production security requirements. At that point, evaluate PostgreSQL, centralized sessions, migrations and a hardened deployment platform.
