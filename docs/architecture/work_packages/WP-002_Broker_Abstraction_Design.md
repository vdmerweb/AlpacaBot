# Chief Architect Recommendation – POC-002

## Objective
Establish the production broker abstraction before implementing additional Alpaca functionality.

## Rationale
Define the common architecture first and implement Alpaca as the first adapter. This avoids Alpaca-specific patterns spreading through the codebase.

## Recommended Sequence

```text
POC-001
    ↓
Broker Interface Design
    ↓
Broker Capability Model
    ↓
Alpaca Adapter Design
    ↓
POC-002 Implementation
```

## Work Package: WP-002 – Broker Abstraction Design

Deliverables:
- IBroker interface
- Broker capability model
- Domain models:
  - Account
  - Position
  - Order
  - Asset
  - Quote
- Exception hierarchy
- Package structure
- Adapter responsibilities

## Acceptance Criteria
- No Alpaca-specific logic in the domain layer.
- Interfaces remain broker-independent.
- Future brokers can be added with minimal change.
- Steering library updated where required.

## Chief Architect Recommendation
Approve WP-002 before implementing additional broker functionality.
