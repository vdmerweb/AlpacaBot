# WP-002 – Domain Model Questions

**Status:** Awaiting Chief Architect direction  
**Related work package:** `docs/architecture/cadence/active/WP-002_Domain_Model_Architecture_Baseline_v1.md`

## Questions

1. Should `Broker` remain a domain concept, or should it be treated only as an external boundary/integration concern?
2. Should `Asset` and `Instrument` remain separate concepts, or should one be the canonical term for a tradable thing in v1.0?
3. Is `Market` a first-class domain concept in v1.0, and what ownership or lifecycle does it have?
4. Should `Account` contain one or more `Portfolio` objects, or should an account and portfolio have a different relationship?
5. Is `OrderRequest` the intent submitted by a strategy/user and `Order` the accepted instruction, or should the distinction be modelled differently?
6. Is `Trade` the completed fill/result and `Execution` the process/lifecycle that produces it?
7. Should `Risk` and `RiskProfile` be separate concepts, with RiskProfile defining constraints and Risk evaluating state against them?
8. Should `Session` represent a user/application session, a trading session, or both as distinct concepts?
9. Should `Event` be a generic domain concept in the model, with concrete event types deferred to the Event Model workstream?
10. Are the ownership descriptions in the refined model sufficiently domain-level, or should ownership be left as a later component responsibility?
