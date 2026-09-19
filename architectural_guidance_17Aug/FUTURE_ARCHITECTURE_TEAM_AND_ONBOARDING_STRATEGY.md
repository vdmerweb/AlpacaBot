# Future Architecture Team Structure and Architect Onboarding Strategy

**Version:** 1.0  
**Status:** Proposed — activate after Architecture Baseline v1.0 approval

## 1. Purpose

Define how the project can evolve from a single Product Owner / Chief Architect / Implementation Engineer model into a scalable architecture organisation.

This is not activated yet. Architecture Baseline v1.0 must be completed and approved first.

## 2. Strategic Objective

Architecture knowledge must not depend on one person, one ChatGPT conversation, one Copilot session or one AI model.

The architecture must become an organisational asset.

## 3. Recommended Structure

### Group Architect
Owns enterprise architecture standards, cross-product architecture, shared platforms and portfolio-level governance.

### Portfolio/Product Architect
Owns product architecture, Architecture Baselines, CADs, ADRs, ARRs and technical evolution.

### Project/Domain Architect
Applies approved architecture to detailed component design and work packages.

### Implementation Engineers
Multiple engineers may implement against the same approved architecture.

## 4. AI Is a Tool, Not the Architect

Organisational and human authority should remain explicit.

AI should support architecture, not become the permanent owner of architectural authority.

The repository and approved architecture remain authoritative.

## 5. ChatGPT Recommendation

A future architect can use ChatGPT as their primary AI architecture assistant.

The recommended model is:

**Architect + ChatGPT + Architecture Knowledge Base**

not:

**Architect + historical ChatGPT conversation**

Current ChatGPT Projects are designed to keep files, instructions and chats together for long-running work, and Business/Enterprise workspaces support shared projects. This makes a dedicated project architecture workspace a suitable onboarding mechanism, subject to enterprise policy. citeturn0search0turn0search14

For enterprise use, ChatGPT Enterprise provides managed workspaces, administration, identity controls and governance capabilities. citeturn0search14

## 6. Architect Onboarding Package

Mandatory content should include:

- Project Context
- Project Vision
- Constitution
- Approved Architecture Baseline
- Reference Architecture
- Glossary
- CAD index
- ADR index
- ARR index
- Work Package process
- Roadmap
- Security
- Testing Strategy
- AI Collaboration rules

Useful additional content:

- Recent architecture reviews
- Current milestones
- Active work packages
- Learning Log
- Technical debt
- Open architecture questions

Rule for the new architect:

> Treat approved repository artefacts as authoritative. Do not reconstruct decisions from historical chat when an approved artefact exists.

## 7. Architect Onboarding Sequence

1. Understand the product.
2. Understand governance.
3. Understand the current architecture.
4. Review architectural history.
5. Produce a current-state assessment.
6. Have the outgoing architect review it.
7. Formally transfer architecture responsibility.

## 8. Handover Artefacts

Create:

`ARCHITECT_ONBOARDING.md`

and, for each transition:

`ARCHITECT_HANDOVER_<DATE>.md`

The handover should cover:

- Current baseline
- Architecture status
- Active CADs
- Active ADRs
- Recent ARRs
- Open decisions
- Known risks
- Current work packages
- Architectural debt
- Areas requiring attention
- Recommended next steps

## 9. Multiple Architects

Recommended hierarchy:

**Group Architect → Portfolio/Product Architect → Project/Domain Architect**

Disagreements should be resolved at the lowest appropriate level and escalated through the Decision Framework when necessary.

Important decisions should be recorded in ADRs where appropriate.

## 10. Second Implementation Engineer

Yes. A second Implementation Engineer can use GitHub Copilot.

Both engineers should operate against:

- The same repository
- The same steering library
- The same approved Architecture Baseline
- The same glossary
- The same coding standards
- The same testing strategy
- The same Work Package process

They must not develop independent architectural interpretations.

## 11. GitHub Copilot Recommendation

For organisational use, centrally managed Copilot Business or Enterprise is preferable to independent personal configurations.

GitHub currently provides Copilot Business and Enterprise with central policy and access controls; enterprise/organisation administrators can control features, models and agents. citeturn0search2turn0search4turn0search9

The exact plan should be selected after assessing organisational security, scale, identity and budget requirements.

## 12. Shared Engineering Context

The repository should be the shared source of truth.

Both Implementation Engineers may use Copilot independently, but both must operate within the same architecture.

Governance principle:

**Copilot may propose. Engineer validates. Architecture governs. Product Owner accepts.**

## 13. MCP Strategy

MCP should remain an enabling technology, not a mandatory architectural dependency.

Potential uses include:

- Project knowledge access
- Repository information
- Issue tracking
- Documentation
- Architecture queries
- Controlled engineering workflows

Current ChatGPT supports MCP-powered apps in Business/Enterprise/Edu environments under controlled settings. This should be treated as an optional future capability, not a prerequisite for the architecture team. citeturn0search20

## 14. Architecture Knowledge Hierarchy

The eventual organisational knowledge model should be:

```text
Enterprise Architecture Knowledge
        |
        +-- Group Architecture
        |
        +-- Portfolio Architecture
        |
        +-- Product Architecture
        |
        +-- Project Architecture
              |
              +-- Baseline
              +-- CADs
              +-- ADRs
              +-- ARRs
              +-- Work Packages
              +-- Learning Log
```

AI assistants consume this knowledge. They do not own it.

## 15. Architecture Continuity

If the current Chief Architect changes project, becomes Group Architect or leaves the project, the project must continue without architectural amnesia.

The new architect must be able to reconstruct the architecture from approved documents, decisions, reviews, baselines and repository history.

Objective:

**Architecture continuity without dependence on conversational memory.**

## 16. Transition to Architecture Baseline v2.0

Only after v1.0 is formally approved:

1. Appoint/confirm architects.
2. Onboard the new architect.
3. Appoint the second Implementation Engineer.
4. Establish common AI tooling.
5. Establish shared repository governance.
6. Review the current architecture with the new team.
7. Identify justified improvements.
8. Open Architecture Baseline v2.0 as controlled evolution.

Version 2.0 should not reopen every decision. Only justified architectural changes should enter v2.0.

## 17. Long-Term Principle

**People own architecture.**

**AI accelerates architecture.**

**Repositories preserve architecture.**

**Engineers implement architecture.**

**Governance controls change.**
