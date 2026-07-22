# Chief Architect Instruction to the Implementation Engineer
## Following Approval of WP-002

## Status

The recent architectural changes are **APPROVED**.

Please keep the current changes and proceed with **WP-002 – Domain Model and Broker Abstraction Foundation**.

---

# Primary Instruction

Your immediate objective is **not** to implement additional broker functionality.

Your objective is to establish the architectural foundation upon which all future implementations will be built.

Focus first on producing a high-quality, technology-agnostic business domain model.

---

# Work Sequence

Complete the following sequence without skipping steps:

1. Complete `DOMAIN_MODEL.md`
2. Submit for Chief Architect review
3. Incorporate review feedback
4. Obtain Product Owner approval
5. Produce `IBroker_Concept.md` (design document only)
6. Chief Architect review
7. Create `ADR-001 Broker Abstraction`
8. Begin implementation
9. Validate implementation
10. Close the work package

---

# Additional Guidelines

## Keep the Domain Business-Centric

The domain model should describe the business, not the implementation.

Avoid:
- Alpaca-specific terminology
- REST endpoints
- HTTP details
- Python classes
- Framework discussions

Describe concepts instead:
- Broker
- Portfolio
- Account
- Position
- Order
- Asset
- Quote
- Strategy
- Execution
- Risk
- Event
- Notification

## Delay Interface Design

Do not implement or finalise `IBroker` until the business concepts have been agreed.

The interface should emerge naturally from the approved domain model.

## Delay ADR Creation

Architecture Decision Records document approved decisions.

They should never be used as design discussion documents.

Design first.
Review.
Approve.
Record the decision.

## Preserve Architectural Independence

Every design decision should answer:

> "Would this still make sense if Alpaca were replaced by another broker?"

If the answer is "no", revisit the design.

## Maintain Traceability

Ensure each architectural artefact references related work packages, milestones, reviews and steering documents.

---

# Engineering Lifecycle

Product Owner
→ Architecture Baseline
→ Milestone
→ Work Package
→ Concept Design
→ Architecture Review
→ ADR
→ Implementation
→ Validation
→ Milestone Complete

---

# Final Observation from the Chief Architect

The project has reached an important transition point.

The governance model has been validated, the first milestone has been completed, and the engineering team is working effectively within clearly defined responsibilities.

From this point onward, architectural decisions will have long-term consequences.

Therefore, we should deliberately slow the pace of architectural work while increasing the depth and quality of design reviews.

A well-designed `DOMAIN_MODEL.md` and `IBroker_Concept.md` can become the foundation for every future broker integration, including Alpaca, Interactive Brokers, FNB, EasyEquities, or others.

Investing additional effort in these foundational documents now will reduce future redesign, minimise technical debt, and help ensure AlpacaBot remains modular, extensible, and maintainable for many years.
