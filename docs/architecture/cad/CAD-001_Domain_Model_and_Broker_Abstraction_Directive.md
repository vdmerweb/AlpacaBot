# CAD-001 – Domain Model and Broker Abstraction Directive

## Status

APPROVED

## Scope

Provide authoritative instruction for WP-002: Domain Model and Broker Abstraction Foundation.

## Instruction

1. Finalise `docs/architecture/DOMAIN_MODEL.md` as the central architectural reference.
2. Keep the domain model business-centric and technology-agnostic.
3. Do not design or implement `IBroker` until the domain model has been reviewed and approved.
4. Do not create ADRs until the domain model and `IBroker_Concept.md` are approved.
5. Ensure every artefact references the related milestone, work package, and review record.
6. Use this directive as the approved architecture path for WP-002.

## References

- `docs/architecture/DOMAIN_MODEL.md`
- `docs/architecture/work_packages/WP-002_Domain_Model_and_Broker_Abstraction_Foundation.md`
- `docs/architecture/reviews/ARR-001_POC001_Architectural_Assessment.md`
- `docs/architecture/milestones/MILESTONE-002_Domain_Model_and_Broker_Abstraction_Foundation.md`
- `Chief_Architect_Instruction_WP002.md`

## Traceability

This directive establishes the approved architectural approach for WP-002 and should be referenced by:
- `WP-002_Domain_Model_and_Broker_Abstraction_Foundation.md`
- `ADR-001_Broker_Abstraction.md` (when created)
- `ARR-002` review record
