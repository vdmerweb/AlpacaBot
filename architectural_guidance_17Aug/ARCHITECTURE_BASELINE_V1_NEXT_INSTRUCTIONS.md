# Future Architecture Team Structure and Architect Onboarding Strategy

**Version:** 2.0  
**Status:** Proposed — to be activated progressively after Architecture Baseline v1.0 and v2.0

## 1. Purpose

The project is currently in startup phase and does not have funding for professional/paid versions of ChatGPT, GitHub Copilot, Microsoft Copilot, Grok or similar AI tooling.

Therefore, the architecture and team model must **not depend on paid AI products**.

The recommended strategy is:

- **Short term:** use available/free tooling and the current Product Owner + Chief Architect + Implementation Engineer team to complete Architecture Baseline v1.0 and v2.0.
- **Long term:** when funding and product scale justify it, progressively introduce managed AI tooling, additional architects and additional engineers.

---

## 2. Chief Architect Recommendation

### Complete Architecture Baseline v2.0 before changing the core team structure

I recommend that we **do not introduce the new architect and second Implementation Engineer immediately after v1.0**.

Preferred sequence:

```text
Architecture Baseline v1.0
          ↓
Initial implementation / learning
          ↓
Architecture Baseline v2.0
          ↓
Team and tooling review
          ↓
New team structure, if justified
```

This allows us to prove the architecture with real implementation experience before expanding the organisation.

Architecture v2.0 should be informed by:

- POC and implementation results
- Broker abstraction experience
- Domain-model findings
- Testing experience
- Integration experience
- Architecture reviews
- Technical debt
- Performance and maintainability observations
- Product Owner feedback
- Implementation Engineer feedback
- AI-assisted development experience

A new architect will therefore inherit a more mature product and architecture.

---

# 3. Startup Team — Stage 1

Retain:

**Product Owner → Chief Architect → Implementation Engineer**

### Product Owner
Owns business vision, priorities, scope and acceptance.

### Chief Architect
Owns architecture, architectural governance, architecture reviews and long-term technical direction.

### Implementation Engineer
Owns implementation, testing, refactoring and execution of approved Work Packages.

## AI tooling

Use suitable free/available tools, for example:

- ChatGPT Free
- GitHub Copilot Free, where available/eligible
- Microsoft Copilot Free, where available
- Grok Free, where available
- Other suitable free/local tools

The exact AI tool is less important than the governance model.

**The tool is not the source of truth. The repository is.**

---

# 4. Free-Tool Operating Model

### ChatGPT / Chief Architect

ChatGPT can assist with:

- Architecture review
- Domain modelling
- CADs
- ADRs
- ARRs
- Work Packages
- Design review
- Documentation
- Onboarding material

If context limitations occur, provide the relevant steering documents and current Work Package explicitly.

### Coding Assistant / Implementation Engineer

The engineer may use available free coding assistance.

Implementation remains governed by:

- Steering documents
- Approved Architecture Baseline
- Work Packages
- Coding standards
- Testing strategy
- Architecture reviews

**The coding assistant is not the architecture authority.**

---

# 5. Repository-First Architecture Knowledge

Because paid AI project/workspace features may not be available, the repository should be the portable architecture knowledge base.

Recommended structure:

```text
docs/
├── steering/
├── architecture/
├── decisions/
├── reviews/
├── work-packages/
└── onboarding/
```

Important documents include:

- `START_HERE.md`
- `PROJECT_CONTEXT.md`
- `PROJECT_VISION.md`
- `PROJECT_GLOSSARY.md`
- Approved Architecture Baseline
- Reference Architecture
- CAD index
- ADR index
- ARR index
- Roadmap
- Current Work Package
- AI Collaboration guidance
- Architect onboarding material

The project must remain understandable even if every AI tool disappears.

---

# 6. Architecture Baseline v1.0

The immediate priority remains:

**Complete and formally approve Architecture Baseline v1.0.**

Do not expand the team simply because v1.0 is approved.

Use v1.0 to guide initial implementation and generate evidence.

---

# 7. Post-v1.0 Implementation

After v1.0 approval, implement architecture-validating capabilities such as:

- Broker abstraction
- Alpaca adapter
- Account service
- Portfolio service
- Order abstraction
- Market-data abstraction
- Initial strategy boundary
- Testing infrastructure

Use controlled Work Packages.

Each significant implementation should generate architectural feedback.

---

# 8. Architecture Baseline v2.0

v2.0 should be an **evidence-driven evolution**, not simply a larger documentation set.

Potential inputs:

- What worked
- What did not work
- Interface limitations
- Broker-specific issues
- Domain-model corrections
- Event-model corrections
- Testing challenges
- Performance issues
- Security findings
- Maintainability findings
- Engineering feedback
- Product Owner feedback

The Chief Architect determines which changes are justified.

---

# 9. Why v2.0 Before Team Expansion

### Lower startup cost
Avoid adding people before the architecture and product direction have matured.

### Better onboarding
A new architect inherits a proven architecture.

### Better role definition
By v2.0 we should know which architectural areas actually require additional ownership.

### Better hiring
Instead of simply deciding that another architect is needed, we can identify the actual responsibility requiring ownership.

### Better tooling investment
When funding becomes available, we can purchase tools based on demonstrated bottlenecks rather than buying everything upfront.

---

# 10. Startup Stage 2

The recommended structure through v2.0 remains:

**Product Owner + Chief Architect + Implementation Engineer**

Specialists can be brought in temporarily where a Work Package requires expertise, for example:

- Security
- Trading domain
- Python
- DevOps

These can initially be consultants or short-term contributors rather than permanent hires.

---

# 11. Trigger for a Second Implementation Engineer

Do not define this by calendar time.

Introduce another engineer when workload and complexity justify it, for example:

- Work Packages can be cleanly divided.
- Parallel development creates a bottleneck.
- Testing exceeds one engineer's practical capacity.
- Broker/integration and domain work need parallel development.
- Backlog size justifies parallel delivery.
- Code review becomes a constraint.
- Parallel engineering materially improves delivery.

---

# 12. Trigger for a New Architect

Introduce another architect when architectural scale justifies it, for example:

- Multiple products/projects share architectural concerns.
- Several major domains require simultaneous ownership.
- Architecture reviews become a bottleneck.
- Multiple engineering teams require architectural direction.
- Product and enterprise architecture need separation.
- The current Chief Architect becomes responsible for multiple products.

Possible future hierarchy:

```text
Group Architect
      │
      ├── Portfolio/Product Architect
      │        │
      │        └── Project/Domain Architect
      │
      └── Other Products
```

---

# 13. Long-Term Team Structure

When scale and funding justify it:

### Group Architect
Enterprise architecture, cross-product architecture, shared platforms and governance.

### Portfolio/Product Architect
Product architecture, baselines, CADs, ADRs, ARRs and architectural evolution.

### Project/Domain Architect
Detailed architecture, component design, Work Package architecture and engineering guidance.

### Implementation Engineers
Multiple engineers implementing against approved architecture.

---

# 14. Long-Term AI Tooling Strategy

Paid tooling should be introduced **progressively**, not all at once.

## Phase A — Startup / Free

Use available tools.

Principles:

- Repository-first
- Explicit prompts
- Controlled Work Packages
- Human validation
- Architecture documents as source of truth

## Phase B — Funded Team

When funding becomes available, prioritise the largest bottleneck.

A sensible order is:

1. Paid GitHub Copilot capability for engineering.
2. Paid ChatGPT capability/workspace for architects and Product Owners.
3. Microsoft Copilot if Microsoft 365 integration creates clear value.
4. Grok or other models only if they provide measurable value.

Do not buy multiple AI products simply because they exist.

---

# 15. Future AI Operating Model

```text
Human Product Owner
        │
        ├── Human Architecture Authority
        │          │
        │          └── AI Architecture Assistant
        │
        └── Engineering Authority
                   │
                   └── AI Coding Assistant
```

AI supports the roles.

AI does not replace the roles.

---

# 16. Future Architect and ChatGPT

When funding permits, a new architect can receive a managed ChatGPT environment appropriate to the organisation.

However, onboarding must not depend on a particular subscription.

The architect should be able to work from:

1. Repository
2. Architecture Baseline
3. Steering library
4. Architecture history
5. Structured onboarding document
6. Approved AI assistant

If the AI vendor/model changes, the architecture remains intact.

---

# 17. Multiple Engineers and GitHub Copilot

When funding permits, move toward centrally managed GitHub Copilot licensing appropriate to the organisation.

Both engineers should use:

- Same repository
- Same Architecture Baseline
- Same steering library
- Same coding standards
- Same testing strategy
- Same Work Package model

The second engineer must not receive an independent architectural interpretation from their coding assistant.

---

# 18. Architect Onboarding

When the first additional architect is appointed, create:

`ARCHITECT_ONBOARDING.md`

It should cover:

### Product
- Vision
- Business objectives
- Scope

### Architecture
- Current baseline
- Domain model
- Broker abstraction
- Components
- Interfaces
- Events
- Reference Architecture

### Governance
- CAD
- ADR
- ARR
- Work Package
- Decision Framework

### Current state
- Completed work
- Current work
- Open decisions
- Risks
- Technical debt
- Roadmap

### AI collaboration
- How the AI architecture assistant is used
- How coding assistants are used
- How prompts are controlled
- How AI output is reviewed

---

# 19. Architecture Continuity

Architecture must survive:

- Change of architect
- Change of Product Owner
- Change of engineer
- Change of AI model
- Change of AI vendor
- Loss of a ChatGPT conversation
- Loss of a Copilot session

Therefore the repository must remain the authoritative architecture memory.

---

# 20. Transition to the New Team

Recommended transition point:

**After Architecture Baseline v2.0, not v1.0.**

```text
v1.0 Baseline
     ↓
Initial Implementation
     ↓
Real-world Feedback
     ↓
v2.0 Baseline
     ↓
Formal v2.0 Sign-off
     ↓
Team / Tooling Review
     ↓
New Architect, if justified
     ↓
Second Engineer, if justified
     ↓
Funded AI Tooling, if justified
     ↓
Next Architecture Evolution
```

---

# 21. What Funding Should Change

Funding should unlock capability, not change the architecture.

The architecture should remain valid whether the team uses:

- Free ChatGPT
- Paid ChatGPT
- Free Copilot
- Paid Copilot
- Microsoft Copilot
- Grok
- Another AI model
- Local AI

The tools should make the existing workflow faster, more scalable or more secure.

---

# 22. Final Chief Architect Recommendation

**KEEP the current team structure through Architecture Baseline v2.0 unless a concrete workload or business requirement forces earlier expansion.**

Immediate priorities:

1. Finish Architecture Baseline v1.0.
2. Obtain formal v1.0 approval.
3. Implement enough real functionality to validate it.
4. Capture implementation evidence.
5. Refine the architecture.
6. Complete Architecture Baseline v2.0.
7. Obtain formal v2.0 sign-off.
8. Review team structure and tooling against actual scale and funding.
9. Introduce additional architects/engineers only where justified.
10. Upgrade AI tooling progressively as funding permits.

## Guiding Principle

> **Do not let the availability of AI tools determine the architecture or organisation. Let product complexity and business needs determine the organisation, and let funding determine how sophisticated the supporting tools become.**

## Startup Principle

**Build the architecture first.**

**Prove it with implementation.**

**Learn.**

**Refine to v2.0.**

**Then scale the team and tooling.**
