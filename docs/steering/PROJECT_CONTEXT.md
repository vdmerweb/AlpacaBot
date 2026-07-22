# Project Context

## Purpose

Capture the current project state so AI assistants and humans understand where AlpacaBot is today.

## Current Status

- Current Release: `v0.1.0`
- Current Objective: Develop a broker-independent trading platform.
- Current Broker: Alpaca Paper Trading
- Current Phase: Foundation

## Progress

### Completed

- ✔ Git setup
- ✔ Python environment
- ✔ VS Code workspace
- ✔ Steering library

### In Progress

- Broker interface
- Configuration model
- Steering document refinement

### Next Milestone

- Market data module

## Known Issues

- Steering content needs review and alignment.
- Documentation structure is stabilising.
- Broker adapter design is pending.

## Current Priorities

- Align governance documents.
- Define stable roles and authority levels.
- Finalise architecture and runtime specification.
- Keep code implementation paused until the library is coherent.

## Learning Log

Record concise lessons from experiments and POCs here. Example entries:

```
POC-001 Lessons

- Alpaca authentication uses API key/secret pairs.
- The REST API returns a rich account object useful for mapping to a broker abstraction.
- Environment variables and `.env` files are a pragmatic configuration mechanism for developers.
- Network and authentication errors should be wrapped in domain-specific exceptions.
```

POC-001 Execution Notes

- The POC code ran successfully and authenticated to Alpaca Paper Trading.
- Account retrieval completed successfully.
- `Config.from_env()` supports both Alpaca-style and APCA-style environment variable names.
- The application correctly handled configuration, logging, and execution flow.
