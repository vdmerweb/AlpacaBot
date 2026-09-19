# WP-003 – Broker Capability Model Lessons

**Related work package:** `docs/architecture/cadence/active/WP-003_Broker_Capability_Model.md`

## Discoveries

- The capability model is conceptually easier to keep stable when it describes business capability rather than vendor operations.
- The Domain Model needs to remain authoritative; capability names should map to domain terms without reintroducing implementation detail.
- Capabilities can be grouped cleanly by account, portfolio, order, market data, strategy, risk, and event/state change.
- The minimum v1.0 scope should remain intentionally narrow to avoid premature IBroker design.

## Traceability Clarification

The Broker Capability Model was initially labeled WP-004. The authoritative Phase 2 sequence identifies it as WP-003. This correction changes documentation identity only; the substantive model is unchanged. Historical WP-002 records remain preserved.

## Implication

This model is ready for Chief Architect review and should be used as the design basis for the next stage only after explicit approval.
