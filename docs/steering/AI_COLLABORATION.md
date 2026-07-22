# AI Collaboration

## Purpose

Define how AI participates in AlpacaBot development and how it is governed.

## AI Roles

- ChatGPT: architecture, design reviews, documentation, and long-term direction.
- Implementation Engineer: implements approved designs, generates boilerplate, scaffolds modules, and writes tests. Current implementation: GitHub Copilot.
- Developer: final approval, product decisions, and integration.

## Rules of Engagement

- AI should not change core architecture without explicit approval.
- AI should follow `docs/steering/CONSTITUTION.md` and `docs/steering/ARCHITECTURE.md`.
- AI should operate within the current workstreams: Architecture Baseline v1.0 and Alpaca POC.
- AI should stop and ask for human approval when uncertain or when changes impact architecture.

## Workflow

1. Review `START_HERE.md` and the relevant steering documents.
2. Confirm the task fits the development lifecycle.
3. Generate or revise content.
4. Validate against the constitution and architecture.
5. Document the result and add tests.
