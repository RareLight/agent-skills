---
name: idea-refine
description: Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-test assumptions before committing to a plan, or when you want to expand options before converging on one. Triggers on "ideate", "refine this idea", or "stress-test my plan".
---

# Idea Refine

## Execution Phases
This interactive skill processes a raw idea through three sequential phases:

### Phase 1: Understand & Expand (Divergent)
- **Reframing**: Restate the idea as a focused "How Might We" problem statement.
- **Sharpening**: Query the user for target audience, success criteria, and constraints.
- **Divergence**: Generate 5-8 distinct product variations using inversion, constraint removal, simplicity filters, or extreme scale lenses.

### Phase 2: Evaluate & Converge (Convergent)
- **Clustering**: Group variations into 2-3 distinct, competing directions.
- **Stress-Testing**: Evaluate directions against User Value (painkiller vs vitamin), Technical Feasibility, and Differentiation.
- **Uncovering Risk**: Explicitly outline hidden bets, fatal assumptions, and intentional omissions.

### Phase 3: Sharpen & Ship (Artifact)
Synthesize the session into a concise markdown document at `docs/ideas/[name].md` containing:
- **Problem Statement** (How Might We)
- **Recommended Direction** (Why and how)
- **Assumptions to Validate** (Test strategies)
- **MVP Scope** (Strict boundaries)
- **Not Doing** (Trade-offs made)

## Conversation Rules
- **Reject Yes-Machining**: Act as a rigorous design partner. Provoke, push back, and constructively challenge weak assumptions.
- **Constraint Integration**: If running inside an existing codebase, ground all ideas in the constraints of the active architecture.

## Verification Checklist
- [ ] Target user and clear success criteria are defined.
- [ ] Strategic assumptions are listed alongside concrete test validation plans.
- [ ] A strict "Not Doing" list forces MVP scope control.
- [ ] A final markdown one-pager is approved and saved to `docs/ideas/`.
