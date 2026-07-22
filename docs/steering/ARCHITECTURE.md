# Architecture

## Purpose

Document the static architecture of AlpacaBot and the relationships between core subsystems.

## Architecture Overview

- Presentation: REST, CLI, Dashboard
- Application: Strategy, Portfolio, Risk, Execution
- Broker Abstraction: adapters for Alpaca and future brokers
- Event Bus: runtime communication layer
- Persistence: state, logs, and history

## Design Principles

- Keep layer responsibilities clear.
- Use interfaces to isolate implementations.
- Prefer composition and dependency injection.
