# WP-003 – Broker Capability Model Questions

**Status:** Questions captured for Chief Architect review  
**Related work package:** `docs/architecture/cadence/active/WP-003_Broker_Capability_Model.md`

## Questions

1. Should the capability model include optional premium capabilities beyond the minimum v1.0 scope, or should v1.0 remain intentionally narrow?
2. Should `Asset` and `Instrument` remain treated as one domain concept in all capability definitions, or should both terms be distinguished in the model?
3. Is `Risk` purely a platform evaluation concept, or should it include external broker-side risk checks as part of the capability model?
4. Should event publication be described as a broker capability in v1.0, or should event publication remain exclusively a platform concern?
5. Should non-functional concerns such as latency, rate limits, and reliability be treated as part of the capability model or left for the architecture review and reference architecture steps?
