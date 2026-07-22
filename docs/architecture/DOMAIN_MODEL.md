# AlpacaBot Domain Model

This document is the central architectural reference for AlpacaBot.
It describes the core business concepts without implementation details.
All future ADRs should reference this model.

## Purpose

The domain model defines the key entities and relationships that represent AlpacaBot's problem space.
It should be used as the canonical source for architecture decisions, interface design, and work package definitions.

## Core Concepts

### Broker
A broker is the external service that provides market data, account information, order execution, and position management.

### Account
A trading account represents a customer's portfolio and balance information with a broker.

### Portfolio
A portfolio is a collection of positions, cash, and performance metrics for an account.

### Position
A position represents ownership of an asset in a portfolio, including quantity, cost basis, and current value.

### Order
An order is an instruction to a broker to buy or sell an asset according to specified parameters.

### Asset
An asset is a tradable instrument such as a stock, ETF, or other financial security.

### Quote
A quote is the current market price and aggregated bid/ask data for an asset.

### Market Data
Market data includes quotes, trade ticks, historical prices, and any feed used to inform decisions.

### Strategy
A strategy is the logic that decides when to create, modify, or cancel orders based on market and portfolio state.

### Signal
A signal is a decision output from a strategy or analysis process, indicating a trading opportunity or risk condition.

### Execution
Execution is the process of submitting orders to a broker and tracking their lifecycle until completion.

### Risk
Risk covers the business rules, limits, and checks that protect the portfolio from unacceptable exposure.

### Event
An event is a domain-occurring change or trigger, such as market updates, order fills, position changes, or alerts.

### Notification
A notification is a message delivered to users or systems about domain events, execution outcomes, or risk conditions.

## Relationship Overview

- A Broker exposes Account, Portfolio, Position, Order, Asset, Quote, and Market Data capabilities.
- An Account contains one or more Portfolios.
- A Portfolio contains Positions and maintains a view of cash and performance.
- Orders affect Positions and Portfolio state through Execution.
- Strategies observe Market Data, Portfolio state, and Risk rules to generate Signals.
- Events and Notifications carry domain state changes through the system.

## Architectural Role

This Domain Model is the foundation for:

- `ADR-001_Broker_Abstraction.md`
- `ADR-002_Trading_Domain.md`
- `ADR-003_Exception_Strategy.md`

It should remain implementation-agnostic and evolve only as the core business concepts change.
