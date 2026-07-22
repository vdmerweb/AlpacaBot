# Decision Framework

## Purpose

Provide a framework for making decisions and understanding what AI can decide.

## Decision Guidelines

- Architecture decisions: NO without human approval.
- Interface definitions: usually NO without review.
- Implementation details: YES when the design is approved.
- Bug fixes: YES if they do not alter architecture.
- Renames and refactoring: YES within boundaries.
- Security changes: NO without explicit approval.
- Business logic changes: NO without product owner approval.

## Approval Process

1. Identify the decision type.
2. Check the steering documents.
3. If uncertain, stop and ask for approval.
4. Document the decision or the requirement.

## Levels of Authority

- Business goals: Product Owner
- Architecture: Chief Architect + Product Owner
- Public interfaces: Chief Architect
- Internal implementation: Implementation Engineer
- Refactoring: Implementation Engineer (subject to review)
- Security changes: Product Owner + Chief Architect
- Third-party dependencies: Product Owner + Chief Architect
- Database schema changes: Chief Architect
- Runtime agent design: Chief Architect

## Architecture Baseline Readiness

A baseline is ready when:

- Steering documents are internally consistent.
- Cross-references between documents are complete.
- Architecture and module boundaries are agreed.
- Initial project structure is defined.
- Broker abstraction is specified.
- Configuration approach is agreed.
- Event model is defined.
- Coding standards are approved.
- AI collaboration model is documented.
- Product Owner formally approves the baseline.
