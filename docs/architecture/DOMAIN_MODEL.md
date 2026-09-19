# AlpacaBot Domain Model

**Status:** Draft for Chief Architect review  
**Related work package:** WP-002 – Domain Model: Architecture Baseline v1.0

This document is the central architectural reference for AlpacaBot's business vocabulary.
It describes concepts, responsibilities, relationships, lifecycle, and ownership without prescribing technology, interfaces, vendors, or implementation.

## Purpose and Boundaries

The domain model describes a broker-independent trading platform.
It does not define external operations, programming-language types, storage, transport mechanisms, or a specific broker.

The model distinguishes:

- business intent from external instructions
- market observations from domain decisions
- an execution process from its resulting trade
- risk constraints from risk evaluation

## Domain Concepts

### Broker

- **Purpose:** Represent an external financial service through which accounts, instruments, market information, and trading activity may be accessed.
- **Responsibilities:** Provide externally available trading and market capabilities; return outcomes and status relevant to the platform.
- **Relationships:** Associated with an Account, Asset/Instrument, Market Data, Order, and Execution.
- **Lifecycle:** Available, unavailable, connected for use, disconnected, or retired from the platform.
- **Ownership:** External to the platform; the platform owns the relationship and its normalized business meaning.

### Account

- **Purpose:** Represent the financial account in which trading activity and holdings are maintained.
- **Responsibilities:** Establish the scope for balances, portfolios, orders, positions, and account-level constraints.
- **Relationships:** Associated with a Broker and one or more Portfolios; contains Orders and Positions through portfolio activity.
- **Lifecycle:** Identified, active, restricted, suspended, or closed.
- **Ownership:** Owned by the account holder and administered through an external Broker.

### Portfolio

- **Purpose:** Represent a managed collection of holdings and cash within an Account.
- **Responsibilities:** Express allocation, valuation, performance, and exposure for its holdings.
- **Relationships:** Belongs to an Account; contains Positions; is observed by Strategies and Risk evaluation.
- **Lifecycle:** Defined, active, paused, or closed.
- **Ownership:** Owned by the Account; managed according to the platform's operating rules.

### Position

- **Purpose:** Represent the quantity and economic interest held in an Asset/Instrument within a Portfolio.
- **Responsibilities:** Track quantity, acquisition basis, valuation, and realized or unrealized change.
- **Relationships:** Belongs to a Portfolio and refers to an Asset/Instrument; changes as Trades settle.
- **Lifecycle:** Absent, opening, open, reducing, and closed.
- **Ownership:** Owned by the Portfolio; its state is derived from completed trading activity and current valuation.

### Asset and Instrument

- **Purpose:** Represent a tradable financial thing recognized by the platform.
- **Responsibilities:** Provide identity and descriptive attributes needed to distinguish what can be observed or traded.
- **Relationships:** May be listed or traded in a Market; referenced by Orders, Positions, Quotes, Bars, and Market Data.
- **Lifecycle:** Identified, tradable, restricted, suspended, expired, or retired.
- **Ownership:** Defined by the relevant market or external source; the platform maintains its canonical identity.

The terms `Asset` and `Instrument` are currently treated as a combined concept pending Chief Architect clarification. The distinction must not be assumed by later work until the question in the cadence record is resolved.

### Market

- **Purpose:** Represent the venue or market context in which an Asset/Instrument can be quoted or traded.
- **Responsibilities:** Define market identity, operating status, and trading calendar context.
- **Relationships:** Relates to Assets/Instruments, Quotes, Bars, Market Data, and Market Open/Closed events.
- **Lifecycle:** Defined, open, closed, halted, or retired.
- **Ownership:** External market context; the platform records the business-relevant view.

### OrderRequest

- **Purpose:** Represent an intention to buy or sell an Asset/Instrument under stated conditions.
- **Responsibilities:** Capture desired action, quantity, constraints, and originating purpose before an Order exists.
- **Relationships:** May be produced from a Signal, Strategy, user action, or approved portfolio activity; may result in an Order.
- **Lifecycle:** Proposed, risk-checked, approved, rejected, cancelled, or converted to an Order.
- **Ownership:** Owned by the originating strategy, user, or platform process until accepted for execution.

### Order

- **Purpose:** Represent an accepted instruction to perform a trading action.
- **Responsibilities:** Maintain the instruction's identity, terms, status, and relationship to resulting execution activity.
- **Relationships:** May originate from an OrderRequest; refers to an Asset/Instrument; is processed through Execution and may produce Trades.
- **Lifecycle:** Created, submitted, accepted, partially filled, filled, rejected, cancelled, or expired.
- **Ownership:** Owned by the platform as a platform instruction while its external processing is handled through a Broker.

### Trade

- **Purpose:** Represent a completed or partially completed exchange of an Asset/Instrument resulting from an Order.
- **Responsibilities:** Record quantity, price, time, and economic result of a completed fill.
- **Relationships:** Results from an Order through Execution; changes a Position and Portfolio.
- **Lifecycle:** Reported, confirmed, corrected, or voided.
- **Ownership:** Owned by the platform's trading record; associated with the external Broker's execution evidence.

### Quote

- **Purpose:** Represent a point-in-time price observation for an Asset/Instrument.
- **Responsibilities:** Express available bid, ask, last price, size, and observation time where applicable.
- **Relationships:** Is a form of Market Data; relates to an Asset/Instrument and Market; may inform a Signal or Risk evaluation.
- **Lifecycle:** Observed, current, superseded, or expired.
- **Ownership:** Originates from a market data source; the platform owns the normalized observation.

### Bar

- **Purpose:** Represent aggregated market observations over a defined time interval.
- **Responsibilities:** Express open, high, low, close, volume, interval, and observation period where available.
- **Relationships:** Is a form of Market Data; relates to an Asset/Instrument and Market; may be consumed by Strategies.
- **Lifecycle:** Open, finalized, corrected, or expired.
- **Ownership:** Originates from a market data source; the platform owns the normalized record.

### Market Data

- **Purpose:** Represent observations about market conditions.
- **Responsibilities:** Provide current, historical, or streaming observations used by Strategies, Risk, and portfolio valuation.
- **Relationships:** Includes Quotes, Bars, and other observations; relates to Assets/Instruments and Markets.
- **Lifecycle:** Requested, received, validated, available, superseded, or expired.
- **Ownership:** Sourced externally and consumed by platform capabilities.

### Watchlist

- **Purpose:** Represent a selected collection of Assets/Instruments for observation.
- **Responsibilities:** Maintain membership and the intent to monitor selected instruments.
- **Relationships:** Contains Assets/Instruments; may be used by Strategies and Notifications.
- **Lifecycle:** Created, active, modified, archived, or deleted.
- **Ownership:** Owned by the user or platform process that defines it.

### Strategy

- **Purpose:** Represent a defined approach for interpreting information and generating trading decisions.
- **Responsibilities:** Observe relevant domain state, apply its rules, and produce Signals or OrderRequests.
- **Relationships:** Consumes Market Data, Portfolio state, and Risk outcomes; produces Signals and may produce OrderRequests.
- **Lifecycle:** Defined, enabled, paused, disabled, or retired.
- **Ownership:** Owned by the platform and governed by its creator and operating authority.

### Signal

- **Purpose:** Represent a strategy or analysis conclusion that an opportunity, condition, or action may exist.
- **Responsibilities:** State the observation, direction, confidence or strength, and validity period where applicable.
- **Relationships:** Produced by a Strategy or analysis process; may lead to an OrderRequest; may be evaluated by Risk.
- **Lifecycle:** Generated, valid, acted upon, expired, rejected, or withdrawn.
- **Ownership:** Owned by the producing Strategy or analysis process.

### Execution

- **Purpose:** Represent the process of carrying an Order through submission, progress, and completion.
- **Responsibilities:** Track processing state, outcomes, exceptions, and the relationship between an Order and its Trades.
- **Relationships:** Processes Orders; produces Trades; involves a Broker; changes Positions and Portfolio state.
- **Lifecycle:** Initiated, submitted, acknowledged, in progress, completed, failed, cancelled, or expired.
- **Ownership:** Owned by the platform process; depends on external Broker outcomes.

### Risk Profile

- **Purpose:** Represent constraints and permitted exposure rules applicable to a Portfolio, Strategy, or OrderRequest.
- **Responsibilities:** Define limits, thresholds, and conditions for acceptable activity.
- **Relationships:** Applies to Portfolio, Strategy, Signal, and OrderRequest; is used by Risk evaluation.
- **Lifecycle:** Draft, active, superseded, suspended, or retired.
- **Ownership:** Owned by the platform's risk authority or the authority assigned to the relevant Portfolio.

### Risk

- **Purpose:** Represent the evaluation of activity or state against applicable risk rules.
- **Responsibilities:** Identify exposure, breaches, warnings, and approval or rejection outcomes.
- **Relationships:** Evaluates Risk Profiles against Portfolio, Position, Signal, and OrderRequest state.
- **Lifecycle:** Requested, evaluating, approved, warned, rejected, escalated, or resolved.
- **Ownership:** Owned by the platform's risk process.

### Session

- **Purpose:** Represent a bounded period in which platform activity is coordinated and observed.
- **Responsibilities:** Establish context for a run of strategy, market, or operational activity.
- **Relationships:** Contains or contextualizes Signals, OrderRequests, Executions, Events, and Notifications.
- **Lifecycle:** Created, active, paused, ended, or expired.
- **Ownership:** Owned by the platform process that establishes the session.

### Event

- **Purpose:** Represent a meaningful occurrence or state change in the domain.
- **Responsibilities:** Communicate that something happened without prescribing how consumers respond.
- **Relationships:** May describe changes to Orders, Trades, Positions, Portfolios, Quotes, Markets, or Sessions; may trigger Notifications.
- **Lifecycle:** Created, published, consumed, acknowledged, archived, or expired.
- **Ownership:** Owned by the platform event source; consumers do not alter the original occurrence.

### Notification

- **Purpose:** Represent a message about a domain event, outcome, warning, or action requiring attention.
- **Responsibilities:** Deliver relevant information to a person or system through an appropriate channel.
- **Relationships:** May be generated from Events, Risk outcomes, Execution outcomes, or account conditions.
- **Lifecycle:** Created, queued, delivered, acknowledged, failed, or expired.
- **Ownership:** Owned by the platform notification process and addressed to its recipient.

## Relationship Overview

```text
Market -> Asset/Instrument -> Quote, Bar, and Market Data
Account -> Portfolio -> Position
Strategy -> Signal -> OrderRequest -> Order -> Execution -> Trade
Trade -> Position and Portfolio state
Risk Profile -> Risk evaluation -> Signal or OrderRequest outcome
Event -> Notification
Session contextualizes platform activity
Broker is an external boundary associated with Account, Market Data, and Execution
```

## Domain Invariants

- A Position refers to an Asset/Instrument and belongs to a Portfolio.
- A Trade is the result of completed execution activity; it is not the execution process itself.
- An OrderRequest expresses intent; an Order is an accepted instruction.
- A Quote and Bar are observations and must not be treated as trading decisions.
- A Signal does not itself constitute an Order or guarantee execution.
- Risk evaluation occurs before an OrderRequest becomes an accepted Order where applicable.
- Broker-specific terminology and behavior must not redefine platform business concepts.

## Architectural Role and Traceability

This Domain Model is the foundation for the Phase 2 Broker Capability Model, IBroker Specification, Platform Interfaces, Component Architecture, Event Model, Naming Standards, and Reference Architecture.

Related records:

- `AI_ARCHITECTURE_ENGINEERING_CADENCE.md`
- `docs/architecture/PHASE_2_ARCHITECTURE_BASELINE_v1.md`
- `docs/architecture/cad/CAD-001_Domain_Model_and_Broker_Abstraction_Directive.md`
- `docs/architecture/cadence/active/WP-002_Domain_Model_Architecture_Baseline_v1.md`
- `docs/architecture/cadence/questions/WP-002_Domain_Model_Questions.md`
- `docs/architecture/cadence/learning/WP-002_Domain_Model_Lessons.md`

This document is a draft pending Chief Architect review. It does not approve the Architecture Baseline, create an ADR, or authorize the next Phase 2 workstream.
