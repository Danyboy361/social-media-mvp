# Requirements Specification

## 1. Purpose and scope
Build a locally runnable social media MVP where users register, authenticate, view all published posts and publish their own posts. The required scope follows the Software Engineering Workshop assessment brief.

## 2. Assumptions
- The application is a responsive web application rather than a mobile app.
- A username is the account identifier; email verification is not required by the brief and is omitted.
- Any visitor can read the public feed; only signed-in users can publish.
- Posts are plain text and limited to 280 characters.
- Times are stored as UTC ISO-8601 timestamps.
- SQLite with a Docker named volume is sufficient for a single-instance classroom demo.
- Feed pagination, follows, likes, replies, image uploads, moderation and password recovery are outside MVP scope.

## 3. Functional requirements
| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| FR-01 | Register account | Must | A valid unique username (3–30 letters/numbers/underscores) and password of at least 8 characters creates an account. Duplicate usernames are rejected with a clear message. |
| FR-02 | Secure credentials | Must | Passwords are stored only as salted password hashes; a database inspection never reveals the submitted password. |
| FR-03 | Log in | Must | A registered user can sign in with correct credentials; incorrect credentials show a generic error and do not authenticate. |
| FR-04 | Log out | Must | A signed-in user can log out; subsequent protected post requests require authentication. |
| FR-05 | Read feed | Must | The home page lists posts from all users, including author, content and creation timestamp, newest first. Empty state is shown when no posts exist. |
| FR-06 | Create post | Must | An authenticated user can publish non-empty text up to 280 characters; the new post appears at the top of the feed. |
| FR-07 | Validate post | Must | Empty/whitespace-only and >280-character posts are rejected with a user-visible message. |
| FR-08 | Persist data | Must | User and post records remain after container restart when the named volume is retained. |
| FR-09 | Health check | Should | `GET /health` returns HTTP 200 and `{"status":"ok"}` when the database is reachable. |

## 4. Non-functional requirements
| ID | Category | Requirement / test |
|---|---|---|
| NFR-01 | Security | Use industry-standard password hashing; never store plain-text passwords. |
| NFR-02 | Security | Post creation and logout require an authenticated session; session cookie is HttpOnly and SameSite=Lax. |
| NFR-03 | Usability | Responsive layout supports modern desktop and mobile viewport widths; form labels and validation messages are provided. |
| NFR-04 | Performance | For a classroom dataset, feed request should complete within 2 seconds on a typical laptop; latest 100 posts are indexed and queried. |
| NFR-05 | Reliability | Database records survive ordinary container replacement while the named volume is retained. |
| NFR-06 | Reproducibility | A fresh clone can start using documented `docker compose up --build` steps and port 5000. |
| NFR-07 | Maintainability | Source, templates, static assets, tests, documentation and CI workflow are separated into clear files/directories. |
| NFR-08 | Quality | CI installs dependencies, runs automated tests and builds the Docker image on push/PR. |

## 5. Traceability
- FR-01–FR-04: `app.py`, `templates/register.html`, `templates/login.html`, tests.
- FR-05–FR-07: `app.py`, `templates/index.html`, tests.
- FR-08: `compose.yaml` named volume and SQLite path.
- NFR-08: `.github/workflows/ci.yml`.

## 6. Out of scope
Social graph, likes, replies, direct messages, media uploads, search, notifications, email verification, account recovery, production hosting, Kubernetes deployment and blue-green/canary rollout.
