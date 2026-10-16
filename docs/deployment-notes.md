# Deployment notes: blue-green and canary as future extensions

The supplied demo guide illustrates progressive delivery patterns. These are **not required by the assessment brief**, which mandates a working local Docker MVP and CI. This project does not claim to deploy to Kubernetes or implement a production traffic switch.

## Blue-green concept
Run two application versions side by side (blue = current stable, green = candidate). Route normal traffic to blue while smoke-testing green. Promote by switching the service/router to green; rollback by switching back to blue.

## Canary concept
Expose a small proportion of traffic to a candidate version, monitor health/error rate/latency, then gradually increase traffic or roll back.

## Important database caveat
Both versions may temporarily use the same database. Schema changes must remain compatible with both versions during the overlap period; use expand-and-contract migrations. Never assume application rollback also reverses database changes.

## How this project could evolve
1. Add a container registry and immutable image tags.
2. Add a staging environment and automated smoke tests.
3. For Kubernetes, define Deployments/Services and use a progressive-delivery controller such as Argo Rollouts, or use a managed platform's traffic splitting.
4. Add health checks, metrics and explicit promotion/rollback gates.
5. Keep secrets out of Git and configure environment-specific values securely.

The referenced guide can be explored at the supplied GitHub URL: https://github.com/fajouri/blue-green-canary-example. Verify its exact implementation and prerequisites before adapting it; the core assessment application remains this social MVP.
