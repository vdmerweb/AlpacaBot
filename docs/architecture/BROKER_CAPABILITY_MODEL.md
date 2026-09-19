# Broker Capability Model

**Status:** Draft for Chief Architect review  
**Related work package:** WP-003 – Broker Capability Model
**Scope:** Business and architecture capability model only; broker-specific API details excluded

## Purpose

This document defines the business capabilities a broker must be able to provide for the AlpacaBot platform. It is intentionally independent of the Alpaca REST API, SDK, or implementation technology.

The model is a bridge between the Domain Model and the Broker Abstraction layer. It informs the future `IBroker` design without prematurely defining implementation code or API contracts.

## Principles

- Broker capabilities are platform concepts, not vendor concepts.
- Capabilities should remain stable even if the external broker changes.
- The platform should depend on capability contracts, not on a specific broker implementation.
- Capability definitions should map cleanly to the core domain concepts: Account, Portfolio, Position, Order, Market Data, Strategy, Risk, and Event.

## Capability Categories

### 1. Authentication and Access

**Capability:** Establish and maintain secure access to a broker.

**Functions:**
- authenticate identity and credentials
- establish session or access state
- maintain authorization health
- handle access failures and re-authentication conditions

**Domain alignment:** Broker, Account, Session

### 2. Account Management

**Capability:** Return and maintain account-level state.

**Functions:**
- retrieve account identity and status
- retrieve balances and account restrictions
- retrieve account metadata relevant to operating a portfolio

**Domain alignment:** Account, Portfolio

### 3. Portfolio and Position Management

**Capability:** Provide portfolio and position state needed for trading and risk evaluation.

**Functions:**
- retrieve current positions
- retrieve position history relevant to trading decisions
- calculate or expose portfolio-level totals
- surface holdings and exposure state

**Domain alignment:** Portfolio, Position, Risk

### 4. Order Lifecycle Management

**Capability:** Submit, track, modify, and cancel trading instructions.

**Functions:**
- submit new order instructions
- track order state transitions
- support cancellation or amendment where allowed
- expose order outcomes and latest status

**Domain alignment:** OrderRequest, Order, Execution, Trade

### 5. Market Data Access

**Capability:** Provide market observations needed to make trading decisions.

**Functions:**
- provide current quotes
- provide historical price windows
- provide price bars or aggregated intervals
- provide market state context

**Domain alignment:** Quote, Bar, Market Data, Market, Asset/Instrument

### 6. Asset and Instrument Catalog

**Capability:** Describe the financial instruments available to the platform.

**Functions:**
- enumerate tradable assets
- identify an instrument or asset from a normalized identifier
- provide relevant metadata needed for trading and analytics

**Domain alignment:** Asset/Instrument, Market, Watchlist

### 7. Watchlist and Monitoring Support

**Capability:** Maintain and observe a user- or strategy-selected set of instruments.

**Functions:**
- create and manage watchlists
- add/remove assets or instruments
- monitor selected market objects

**Domain alignment:** Watchlist, Market Data, Strategy

### 8. Strategy and Signal Support

**Capability:** Provide the operational environment for strategy-driven decisions.

**Functions:**
- provide relevant market and account data to strategy inputs
- return execution outcomes for strategy review
- expose signal and order lifecycle information

**Domain alignment:** Strategy, Signal, Execution

### 9. Risk and Guardrail Evaluation

**Capability:** Support the platform's business risk controls.

**Functions:**
- provide the data needed for risk evaluation
- allow check against limits and policies
- surface risk decisions or blocking conditions

**Domain alignment:** Risk Profile, Risk, OrderRequest, Portfolio

### 10. Event and Notification Support

**Capability:** Publish business state changes and notifications.

**Functions:**
- emit change events from the broker or abstraction boundary
- signal completion, rejection, or state transitions
- surface operational status and alerts

**Domain alignment:** Event, Notification, Execution, Trade

## Non-Functional Capability Expectations

The broker capability model should also account for non-functional concerns that influence the platform design, even where they are not domain concepts:

- reliability of access and response
- latency of market data and account state
- rate-limit constraints
- consistency of state across queries
- resilience of failed or partial responses
- traceability of external events and outcomes

These are architectural constraints, not the business domain itself, but they must be considered during broker abstraction design.

## Capability-to-Domain Mapping

| Capability | Core domain concepts |
|---|---|
| Authentication and access | Broker, Account, Session |
| Account management | Account, Portfolio |
| Portfolio and positions | Portfolio, Position, Risk |
| Order lifecycle | OrderRequest, Order, Execution, Trade |
| Market data | Market Data, Quote, Bar, Market |
| Asset catalog | Asset/Instrument, Market, Watchlist |
| Watchlist support | Watchlist, Strategy |
| Strategy support | Strategy, Signal |
| Risk support | Risk Profile, Risk |
| Event and notification | Event, Notification, Execution |

## Minimum v1.0 Capability Scope

For Architecture Baseline v1.0, the minimum capability scope is:

- authentication and access
- account retrieval
- portfolio and position retrieval
- order submission and status tracking
- market data access
- asset/instrument discovery
- event or status reporting

This scope is intentionally enough to support the initial broker abstraction and to validate the architecture, without yet defining implementation-specific runtime behavior.

## Out of Scope for v1.0

The following are not part of this document:

- Alpaca API method signatures
- Python class definitions
- REST endpoints or payload details
- SDK-specific behavior
- implementation or adapter logic
- ordering of runtime execution details beyond the conceptual capability model

## Traceability

Related documents:

- `docs/architecture/PHASE_2_ARCHITECTURE_BASELINE_v1.md`
- `docs/architecture/DOMAIN_MODEL.md`
- `docs/architecture/cad/CAD-001_Domain_Model_and_Broker_Abstraction_Directive.md`
- `docs/architecture/cadence/active/WP-003_Broker_Capability_Model.md`
- `docs/architecture/cadence/questions/WP-003_Broker_Capability_Model_Questions.md`
- `docs/architecture/cadence/learning/WP-003_Broker_Capability_Model_Lessons.md`

## Review Status

This document is a draft prepared for Chief Architect review under the active cadence. It is not a final approval and it does not authorize the next Phase 2 workstream.
