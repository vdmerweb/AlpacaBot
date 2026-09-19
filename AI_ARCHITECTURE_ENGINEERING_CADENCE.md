# AI Architecture Engineering Cadence

**Status:** Established  
**Version:** 1.0  
**Effective date:** 2026-08-21

## Purpose

This document defines the controlled, resumable collaboration between the Chief Architect and Implementation Engineer.
It is an operating cadence, not a new approval layer. The repository remains the authoritative project memory.

## Roles

### Product Owner

The Product Owner owns business direction, priorities, scope, acceptance, and decisions requiring business authority.
The Product Owner is not required to participate in the technical implementation loop.

### Chief Architect

The Chief Architect owns:

- Architectural direction
- Work package sequencing
- Architecture quality gates
- Architectural review
- Technical and architectural decisions
- Instructions to the Implementation Engineer

### Implementation Engineer

The Implementation Engineer owns:

- Executing approved work packages
- Maintaining the repository
- Testing and validating changes
- Recording implementation results and learning
- Raising technical or architectural questions
- Keeping work resumable for the next session

## Operating Loop

1. The Chief Architect issues or updates a controlled work package.
2. The Implementation Engineer reads the steering context, current baseline, work package, and acceptance criteria.
3. The Implementation Engineer performs only the approved scope.
4. The Implementation Engineer validates the result with focused tests or checks.
5. The Implementation Engineer records outcomes, open questions, and architectural evidence.
6. The Chief Architect reviews the completed work.
7. The Chief Architect accepts the work, requests changes, or updates the architecture direction.
8. The next work package begins only after the review outcome is clear.

## Resumability Requirements

Every active work package must make the following discoverable:

- Current status
- Scope and explicit exclusions
- Related CAD, ADR, ARR, milestone, and baseline documents
- Work completed
- Validation performed
- Open technical or architectural questions
- Next action
- Review status

The Implementation Engineer must not rely on an unavailable chat session to recover context.

## Controlled Sequence

The agreed product and architecture sequence is:

```text
Architecture Baseline v1.0
        |
        v
Beta implementation using Alpaca Paper Trading
        |
        v
Product Owner demonstration
        |
        v
Implementation learning and evidence
        |
        v
Architecture Baseline v2.0
        |
        v
Formal sign-off
        |
        v
Team and tooling reassessment
```

The current controlled Phase 2 workstream is WP-003 Broker Capability Model. The next workstream must not begin until WP-003 receives explicit Chief Architect approval.

## Repository Structure

- `AI_ARCHITECTURE_ENGINEERING_CADENCE.md` — operating rules for the architect-to-engineer loop.
- `docs/architecture/cadence/README.md` — cadence records and navigation.
- `docs/architecture/cadence/active/` — the currently authorized work package and working status.
- `docs/architecture/cadence/completed/` — completed work-package execution records.
- `docs/architecture/cadence/questions/` — unresolved questions awaiting architectural direction.
- `docs/architecture/cadence/learning/` — implementation evidence and lessons that may inform Baseline v2.0.

Existing architecture records remain in their established folders under `docs/architecture/`.

## Current Gate

**Status:** Cadence established; WP-003 Broker Capability Model is ready for Chief Architect review.

**Historical traceability note:** Historical records referencing WP-002 remain preserved for traceability. The current authoritative sequence is WP-002 (Domain Model), WP-003 (Broker Capability Model), and WP-004 (IBroker Specification). The active gate is WP-003 Broker Capability Model review.

**Blocked until approved:** Starting WP-004 IBroker Specification.

**Permitted preparation:** Review of WP-003, responses to Chief Architect questions, and revisions within WP-003. No WP-004 architecture design should begin under this gate.

## Review Outcomes

The Chief Architect may conclude a work package with one of these outcomes:

- **Accepted** — work meets the package criteria.
- **Changes requested** — implementation returns to the same work package.
- **Architectural question raised** — work pauses pending a decision.
- **Superseded** — the package is replaced by a newer approved direction.

## Traceability

The normal traceability path is:

```text
CAD -> Work Package -> Implementation -> Validation -> ARR -> ADR where required -> Learning -> Next Work Package
```

ADR creation remains conditional. An ADR records an approved architectural decision; it is not a substitute for design discussion or implementation instructions.
