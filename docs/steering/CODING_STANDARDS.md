# Coding Standards

## Purpose

Define the coding conventions for AlpacaBot.

## Style

- Follow `black` formatting and PEP 8.
- Use `snake_case` for functions and variables.
- Use `PascalCase` for classes.
- Keep functions small and expressive.

## Typing

- Use type hints for public APIs.
- Prefer data classes or typed models for structured data.

## Error Handling

- Fail fast on invalid input.
- Use custom exceptions for domain errors.
- Log with context and avoid printing secrets.
