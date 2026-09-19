# WP-003 – Broker Capability Model

**Status:** ON HOLD — pending WP-002 Domain Model review and approval
**Owner:** Implementation Engineer  
**Started:** 2026-08-28

## Objective

Define the broker capability model for Architecture Baseline v1.0 in a broker-independent and business-centered way.

## Scope

- Describe the platform-level capabilities that a broker layer must provide.
- Map each capability to the business domain concepts already captured in `docs/architecture/DOMAIN_MODEL.md`.
- Keep the content technology-neutral and vendor-independent.
- Prepare the model for Chief Architect review before work moves to IBroker specification.

## Explicit Exclusions

- No IBroker specification or implementation.
- No API signature design.
- No Alpaca-specific method or payload detail.
- No implementation code.
- No next Phase 2 workstream.

## Governing References

- `AI_ARCHITECTURE_ENGINEERING_CADENCE.md`
- `docs/architecture/PHASE_2_ARCHITECTURE_BASELINE_v1.md`
- `docs/architecture/DOMAIN_MODEL.md`
- `docs/architecture/cad/CAD-001_Domain_Model_and_Broker_Abstraction_Directive.md`
- `docs/architecture/cadence/active/WP-002_Domain_Model_Architecture_Baseline_v1.md`
- `docs/architecture/work_packages/WP-002_Domain_Model_and_Broker_Abstraction_Foundation.md` (historical reference only)

## Work Completed

- Confirmed and preserved historical WP numbering context for traceability.
- Reviewed the current Domain Model and Phase 2 baseline.
- Defined the broker capability model in a broker-agnostic manner.
- Mapped capabilities to domain concepts.
- Recorded unresolved questions and lessons in the cadence folders.

## Validation

- Model is independent of Alpaca-specific implementation detail.
- Model aligns to the published Domain Model.
- Model remains a capability definition rather than an interface specification.
- Model is ready for Chief Architect review.
- The package identity now follows the authoritative Phase 2 sequence: WP-002 Domain Model, WP-003 Broker Capability Model.

## Output

- `docs/architecture/BROKER_CAPABILITY_MODEL.md`

## Questions and Learning

- `docs/architecture/cadence/questions/WP-003_Broker_Capability_Model_Questions.md`
- `docs/architecture/cadence/learning/WP-003_Broker_Capability_Model_Lessons.md`

## Traceability Clarification

The WP-003 identity correction is documentation and traceability clarification only. The substantive Broker Capability Model is unchanged. Historical WP-002 records remain preserved.

## Status to Return

**ON HOLD — WP-003 is not rejected; substantive architectural review is deferred until WP-002 receives explicit Chief Architect approval.**

No approval is inferred from silence. The Broker Capability Model must not be modified during this hold unless explicitly authorized. WP-004 remains blocked.
