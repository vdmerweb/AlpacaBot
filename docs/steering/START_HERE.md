# Start Here

## Purpose

This is the entry point for every AI interaction with AlpacaBot.
It explains the project, the roles, and the documents that must be reviewed before making changes.

## What AlpacaBot is

- A modular algorithmic trading platform.
- Built for broker independence and secure execution.
- Designed to separate architecture from implementation.

## Who does what

- **Ben**: Product owner, final decision maker, and release approver.
- **ChatGPT**: Chief architect, reviewer, and documentation authority.
- **Implementation Engineer**: The role responsible for implementing approved designs and generating boilerplate. Current implementation: GitHub Copilot.
- **Future AI agents**: Specialists in testing, documentation, research, or monitoring.

## Current workstreams

- **Workstream A – Architecture Baseline v1.0**: Refine the steering library, review governance, and stabilise the architecture.
- **Workstream B – Alpaca Proof of Concept**: Validate Alpaca connectivity, paper trading, and implementation learnings as a separate POC.

## Required reading before any task

- `docs/steering/AI_CONTEXT.md`
- `docs/steering/CONSTITUTION.md`
- `docs/steering/ARCHITECTURE.md`
- `docs/steering/MODULE_RULES.md`
- `docs/steering/CODING_STANDARDS.md`
- `docs/steering/DECISION_FRAMEWORK.md`

## Development lifecycle

1. Idea
2. Requirements
3. Architecture
4. Specification
5. Implementation
6. Tests
7. Review
8. Documentation
9. Merge
10. Release

## When to stop and ask for approval

- Any change to architecture or core interfaces.
- Any new broker or platform integration.
- Any change that impacts security or secret handling.
- Any change that affects business logic.
- Any task that is unclear or not covered by the steering documents.
