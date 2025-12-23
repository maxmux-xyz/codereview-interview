# Head of Engineering Interview: System Design Exercise

## Company Context

We are building an **AI-powered PR review platform** that helps engineering teams ship secure, high-quality code. Our product integrates with customers' existing development toolchain to provide automated, context-aware code review.

---

## Product Overview

### How It Works

1. **Onboarding**: Customers sign up via our web application and connect three types of integrations:
   - **SCM Provider** (e.g., GitHub, GitLab) — source of pull requests
   - **Ticket Tracker** (e.g., Linear, Jira) — source of requirements and acceptance criteria
   - **Documentation App** (e.g., Notion, Confluence) — source of architecture decisions, security threat models, and design specs

2. **Automated Review**: For every PR opened in a connected repository, our system:
   - Analyzes the code changes
   - Cross-references against relevant tickets and documentation
   - Either **takes no action** (PR looks good) or **posts a constructive comment** highlighting issues

3. **Issue Categories**: Our analysis flags three types of problems:
   - **Security vulnerabilities** introduced by the change
   - **Requirement drift** — implementation doesn't align with the PRD or ticket acceptance criteria
   - **Standards violations** — code doesn't follow documented architecture patterns, best practices, or security threat model

### Additional Product Surface

Beyond inline PR comments, we're building a **web dashboard** where security researchers and engineering leads can:
- View a prioritized list of the most problematic PRs across their organization
- Drill into specific issues and their context
- Track trends over time

---

## Your Task

### Part 1: Data Model Design

Design the core data model for this system. We want to understand how you think about:

- **Entities**: What are the core objects in this system?
- **Relationships**: How do these entities relate to each other?
- **Attributes**: What key properties does each entity need?

Consider the full lifecycle: customer onboarding, integration setup, PR ingestion, analysis results, and the security researcher dashboard.

### Deliverable

Provide an entity-relationship diagram (ERD) or equivalent representation, along with a brief explanation of your key design decisions.

---

## Constraints & Considerations

As you design, keep the following in mind:

| Concern | Details |
|---------|---------|
| **Scale** | We're targeting hundreds to thousands of customers within the next year. Some customers will have dozens of repositories with high PR velocity. |
| **Multi-tenancy** | Customer data must be strictly isolated. We are SOC 2 compliant and cannot allow any cross-tenant data leakage. |
| **Auditability** | We need to track who did what and when, both for compliance and debugging. |
| **Extensibility** | We plan to add more integration types (e.g., Slack, additional SCM providers) in the future. |

---

## What We're Looking For

- Clear thinking about domain modeling
- Awareness of scale and isolation concerns
- Pragmatic trade-offs with reasoned justification
- Questions you'd want answered before finalizing the design

---

## Time Expectation

Please spend **30–45 minutes** on this exercise. We value clarity over completeness — it's fine to note areas you'd want to explore further rather than solving everything.

---

*Feel free to ask clarifying questions at any point.*
