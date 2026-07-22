# AI Context

## What AlpacaBot is

AlpacaBot is a modular algorithmic trading platform designed for broker independence, testability, and secure execution.

## Project vision

- Build a broker-agnostic platform.
- Keep business logic in services, not UIs.
- Separate architecture from implementation.
- Use AI as an assistant, not the authority.

## Architectural principles

- Interface-first design
- Dependency inversion
- Event-driven runtime flow
- Clear module boundaries
- Security and testability by default

## Roles

- **Ben**: product owner, business decision maker, final approver.
- **ChatGPT**: chief architect, reviewer, mentor, and design authority.
- **Implementation Engineer**: implementation role responsible for approved designs, currently fulfilled by GitHub Copilot.

## Where to find steering documents

- `docs/steering/PROJECT_VISION.md`
- `docs/steering/CONSTITUTION.md`
- `docs/steering/ARCHITECTURE.md`
- `docs/steering/AI_COLLABORATION.md`
- `docs/steering/DECISION_FRAMEWORK.md`

## Decision process

1. Agree on structure and content.
2. Produce Markdown in the repo.
3. Review and refine.
4. Commit to Git.

## What not to change without approval

- Core architecture documents and principles.
- Broker abstraction contracts.
- Runtime execution flows.
- AI collaboration rules.
- Security and secret-handling policies.
