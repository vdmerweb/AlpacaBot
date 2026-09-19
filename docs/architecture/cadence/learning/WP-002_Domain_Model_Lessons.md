# WP-002 – Domain Model Lessons

**Related work package:** `docs/architecture/cadence/active/WP-002_Domain_Model_Architecture_Baseline_v1.md`

## Discoveries

- The original Domain Model was a useful starting glossary but did not satisfy the Phase 2 requirement for purpose, responsibilities, relationships, lifecycle, and ownership.
- Several terms require explicit boundaries before broker capabilities or interfaces can be designed: Asset/Instrument, OrderRequest/Order, Trade/Execution, and Risk/RiskProfile.
- A broker-independent model must describe business meaning and outcomes, not external service operations.
- The domain model should define the vocabulary; component ownership and interface contracts should be derived only after the vocabulary is reviewed.

## Implication

The Broker Capability Model and IBroker Specification must remain blocked until the Chief Architect reviews and approves the Domain Model.
