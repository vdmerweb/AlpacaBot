# Constitution

## Purpose

This constitution defines the core principles, governance rules, and collaboration standards for AlpacaBot.
It is the reference point for architecture, implementation, review, and AI-assisted development.

## Principles

- Broker independence: The system must separate core trading logic from broker-specific adapters.
- Interface-first design: Define contracts and interfaces before implementing concrete behavior.
- Dependency inversion: High-level modules should not depend on low-level implementation details.
- No business logic in UI: User interfaces and presentation layers may orchestrate but never contain core trading rules.
- Testability: Every module must be designed for automated testing and mockability.
- Security-first: Keep secrets outside source control, validate inputs, and handle credentials securely.
- Documentation as code: Architecture, decisions, and interfaces must be documented before implementation.
- Review discipline: Every change must be reviewed for compliance with the constitution.

## AI Collaboration Rules

- ChatGPT is the chief architect, reviewer, and documentation authority.
- GitHub Copilot is the implementation assistant and boilerplate generator.
- The developer is the product owner, final approver, and integrator.
- AI-generated code must be reviewed against this constitution before acceptance.
- Architecture decisions are documented in ADRs prior to major implementation.
- New modules are only added after a design document or module specification exists.

## Coding and Design Standards

- Use explicit interfaces and typed data models.
- Prefer composition over inheritance.
- Keep functions small and single-purpose.
- Use logging, not print statements.
- Handle errors explicitly and fail fast where appropriate.
- Keep configuration and secret management separate from business logic.

## Review Checklist

For every PR and major change, ask:

- Does this comply with the Constitution?
- Does it follow interface-first design?
- Is the behavior documented or specified?
- Are secrets protected and handled correctly?
- Are there tests for new behavior and edge cases?
- Has the change been reviewed for architecture alignment?
