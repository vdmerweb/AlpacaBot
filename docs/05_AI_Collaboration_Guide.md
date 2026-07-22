# 04 AI Collaboration Guide

## Overview

This guide defines how AlpacaBot uses AI tools consistently and safely. It is the shared playbook for working with ChatGPT, GitHub Copilot, and the development team.

## Roles and Responsibilities

### ChatGPT

Use ChatGPT for:

- Architecture design and module boundaries
- Interface definitions and system decomposition
- Design reviews and refactoring strategy
- Testing strategy and validation plans
- Documentation drafts and review
- Risk analysis and security guidance
- Code review questions about correctness, style, and behavior
- High-level debugging and root-cause analysis

ChatGPT is the authoritative source for architecture and long-term design decisions.

### GitHub Copilot

Use Copilot for:

- Implementation of well-defined tasks
- Boilerplate code and repetitive patterns
- Method and class scaffolding once interfaces are clear
- Writing unit test stubs and fixtures
- Filling in code from explicit examples or designs

Copilot should not make architecture decisions or choose design patterns without human review.

### Developer

The developer is responsible for:

- Choosing which AI tool to use for each task
- Validating all AI-generated output
- Ensuring alignment with the project architecture
- Managing secrets, environments, and test data
- Merging code only when it satisfies the Definition of Done

## When to ask ChatGPT vs Copilot

### Ask ChatGPT when:

- You need to define or refine architecture
- You are specifying new module interfaces
- You need a design review or tradeoff analysis
- You need an ADR, roadmap, or documentation update
- You have a complex bug and need a root-cause diagnosis
- You want to define data contracts, security controls, or testing boundaries

### Ask Copilot when:

- You have a clear implementation task and interfaces are defined
- You need to generate boilerplate for models, API endpoints, or tests
- You are implementing behavior already specified in documentation
- You want to accelerate repetitive coding work

## Prompt Templates

### ChatGPT prompts

#### Architecture prompt

```
I am designing a modular algorithmic trading platform in Python. I need a broker-agnostic architecture with clear module boundaries for core trading, market data, portfolio management, order execution, risk, backtesting, and AI-assisted automation. Generate a high-level architecture diagram, the responsibilities of each module, and the interfaces between them.
```

#### Design review prompt

```
Review this design for a Python trading platform. Identify risks, architectural drift, coupling issues, missing interfaces, and improvements. The current structure includes a broker interface, Alpaca adapter, strategy modules, execution engine, persistence layer, and test suite.
```

#### Refactoring prompt

```
Refactor this module for better separation of concerns, clearer naming, and stronger typing. Keep behavior the same and preserve unit test expectations. Explain the changes and how they improve maintainability.
```

#### Debugging prompt

```
I have a failing test in a trading platform module. Here is the code and the test output. Help me identify the root cause and suggest a minimal fix while preserving existing design boundaries.
```

#### Testing prompt

```
I need a testing strategy for a Python trading platform. Define the types of tests needed (unit, integration, backtest, safety), common fixtures, and what metrics should be validated before release.
```

### Copilot prompts

#### Implementation prompt

```
Implement this Python function/class according to this interface and docstring. Keep the implementation simple, use standard library modules, type hints, and add a small unit test example.
```

#### Boilerplate prompt

```
Generate boilerplate for a new Python module with a Pydantic configuration model, logging setup, and placeholder methods for load, validate, and execute.
```

#### Test scaffolding prompt

```
Create unit test scaffolding for this module using pytest. Include fixtures for sample input data and tests for normal, edge, and error cases.
```

## Preventing Architectural Drift

- Start every new feature with a brief design note or ADR entry.
- Keep module interfaces stable; evolve with explicit review.
- Reject ad hoc changes that bypass adapters or layer boundaries.
- Prefer composition and dependency inversion over inheritance and global state.
- Use explicit data contracts and typed models between modules.
- Review AI output against architecture docs before accepting it.

## AI Coding Conventions

Both ChatGPT and Copilot should follow these conventions:

- Use Python 3.11+ syntax and type hints
- Respect repository naming conventions and module structure
- Keep functions short and focused
- Favor explicit error handling over silent exceptions
- Use logging instead of print statements
- Keep secrets in `.env` and never hardcode credentials
- Add or preserve docstrings for public classes and functions
- Write tests for new behavior before merging it

## Reviewing AI-generated Code

1. Confirm the design matches the current architecture documents.
2. Verify type hints, naming, and docstrings.
3. Check security boundaries and secret handling.
4. Run unit tests and integration checks.
5. Compare behavior against requirements and edge cases.
6. Update documentation if the code introduces new concepts or interfaces.

## Definition of Done

A module or feature is done when:

- It implements the agreed interface and behavior
- It passes all local tests for new and affected code
- It has at least one unit test for each path and a regression test for known edge cases
- It has documentation or design notes describing its responsibilities
- It has been reviewed for architecture alignment and style
- It does not include hardcoded secrets or production credentials
- It has clear commit messages and a concise PR description
