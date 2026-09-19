# AlpacaBot – Project Context and Team Model

**Version:** 1.0  
**Status:** Current working context

## Project
AlpacaBot is a modular trading platform currently using Alpaca paper trading as its first broker integration.

Repository/home folder: `C:\Users\Ben\Documents\AlpacaBot`

Development environment: Windows, PowerShell, VS Code, Python, Git and GitHub Copilot.

The strategic objective is broader than Alpaca connectivity: create a modular, broker-independent trading platform that can evolve over time.

## Team Operating Model

### Product Owner — User
Owns vision, business objectives, priorities, scope and acceptance.

### Chief Architect — ChatGPT
Within the agreed team model, owns architecture, architectural governance, domain modelling, architecture directives, architecture reviews, architectural quality and long-term technical direction.

### Implementation Engineer — GitHub Copilot
Owns implementation, refactoring, testing, documentation updates, repository changes and execution of approved work packages.

Role names are intentionally independent of tools.

## Core Architecture

The platform is domain-first, broker-independent, modular, interface-driven, testable and extensible.

The intended dependency direction is:

`Trading Platform → Broker Abstraction → Broker Adapter → Alpaca`

Future brokers should be addable through adapters without redesigning the trading domain.

## Governance

The project uses:

- Steering Documents
- Chief Architecture Directives (CAD)
- Architecture Decision Records (ADR)
- Work Packages (WP)
- Architecture Review Records (ARR)
- Milestones
- Validation Matrix
- Learning Log
- Architecture Baseline

Lifecycle:

`Vision → Steering → CAD → Work Package → Implementation → ARR → ADR where required → Learning Log → Next Iteration`

## POC-001

POC-001 validated configuration, environment handling, Alpaca authentication/connectivity, account retrieval and basic separation of concerns.

Its key architectural lesson was that broker connectivity must sit behind a platform-owned abstraction rather than define the platform.

## Current Architecture Documentation

The steering library includes, among other artefacts:

- `START_HERE.md`
- `PROJECT_VISION.md`
- `CONSTITUTION.md`
- `DEVELOPMENT_PRINCIPLES.md`
- `ENGINEERING_PRINCIPLES.md`
- `ARCHITECTURE.md`
- `AGENT_ARCHITECTURE.md`
- `AI_COLLABORATION.md`
- `AI_CONTEXT.md`
- `MCP_STRATEGY.md`
- `MODULE_RULES.md`
- `CODING_STANDARDS.md`
- `TESTING_STRATEGY.md`
- `SECURITY.md`
- `ROADMAP.md`
- `DECISION_FRAMEWORK.md`
- `PROJECT_CONTEXT.md`
- `PROJECT_GLOSSARY.md`
- `PROMPT_LIBRARY.md`
- `WORK_PACKAGE_TEMPLATE.md`

## Architecture Reviews

ARR-003 and ARR-004 have been completed and integrated into the architecture documentation/indexes. ARR-005 captures the latest project progress/readiness assessment.

## Architecture Baseline v1.0

The team is deliberately not signing off yet. Controlled refinement iterations should continue until the Chief Architect considers the baseline sufficiently complete and coherent.

Phase 2 workstreams:

1. Domain Model
2. Broker Capability Model
3. IBroker Specification
4. Platform Interfaces
5. Component Architecture
6. Event Model
7. Naming Standards
8. Reference Architecture

## Current Working Principle

Governance expansion should now be limited. The focus should shift toward substantive architecture, with approximately 80% effort on architecture development and 20% on governance/documentation maintenance.

## Post-Baseline Direction

After formal approval, implementation can proceed through controlled Work Packages covering broker abstraction, Alpaca adapter, portfolio services, order services, market data, strategy, risk, events and automation.

## Future Team

After v1.0 approval, the intended structure is:

- Product Owner
- Group/Portfolio Architect
- Product/Project Architect(s)
- Implementation Engineer(s)
- AI assistants

Architecture knowledge must become an organisational asset rather than depending on one conversation, person or tool.

## AI Tooling Principle

AI tools are replaceable implementation technology.

The role is stable. A Chief Architect may use ChatGPT today and another approved reasoning environment later. An Implementation Engineer may use GitHub Copilot today and another coding tool later.

The steering library, approved architecture, decisions, glossary and project context remain authoritative.

## Long-Term Objective

Build a modular trading platform capable of supporting multiple brokers, strategies, portfolio management, risk management, market data, automation and future AI/agent capabilities without fundamental redesign.

## Current Decision

**KEEP. Continue refining Architecture Baseline v1.0. Do not formally sign off until explicitly approved by the Chief Architect and accepted by the Product Owner.**
