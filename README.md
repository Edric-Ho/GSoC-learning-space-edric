# Mesa GSoC Learning Space

This repository is Edric's learning space for Mesa, built in preparation for the GSoC Behavioral Framework project.

The goal here is to:

> build models, understand what breaks or feels awkward, and use that to figure out what Mesa is missing.

Instead of trying to design a framework upfront, I focused on implementing a few small models and observing what actually happens when behavior becomes more structured.

---

## What I’m exploring

While working through these models, I kept running into the same kinds of questions:

- how much of the outcome comes from interaction structure vs agent logic?
- how should decision-making actually be written inside an agent?
- at what point does `agent.step()` become hard to reason about?

After a few iterations, it started to feel like behavioral modeling in Mesa depends on three different things:

1. how agents interact
2. how agents decide
3. how that decision logic is organized in code

I wrote a more complete summary here:

👉 [notes/behavioral_framework_evaluation.md](notes/behavioral_framework_evaluation.md)

---

## Models

Each model is intentionally small. The goal is not realism, but to isolate specific issues.

### Model 1 — Interaction Structure
`models/model_1_interaction`

A local competition model where agents repeatedly compete with neighbors.

What surprised me here was how strongly inequality depended on structure. Even with identical agents, allowing overlapping interactions let some agents accumulate rewards much faster than others.

---

### Model 2 — Internal Decision Logic
`models/model_2_needs`

A simple needs-based model where agents choose between:

- working (gain reward, lose energy)
- resting (recover energy)

The interesting part was not the idea itself, but how sensitive the system was to how I defined “pressure” to work vs rest. Small changes in that function completely changed the long-term behavior.

---

### Model 3 — Decision Architecture
`models/model_3_pipeline`

This model keeps similar behavior to Model 2, but rewrites it as an explicit pipeline:

- observe → evaluate → decide → act

It doesn’t change the results much, but it makes the logic easier to follow. This made it clear that Mesa gives flexibility, but doesn’t really help structure decision logic once it grows.

---

## What I’ve learned so far

A few patterns showed up consistently:

- system behavior is often dominated by interaction design, not just agent rules
- internal decision logic is very sensitive to how it’s written
- even simple agents end up needing multi-step reasoning
- all of that currently lives inside `agent.step()`, which becomes harder to manage as models grow

So the problem isn’t just *when* agents are evaluated.

It’s also:

- how decisions are represented
- how behavior is structured
- how different pieces interact

---

## Why this matters for the project

The behavioral framework idea focuses on improving how Mesa supports agent behavior.

From what I’ve seen so far, this probably needs to be approached from multiple angles:

- interaction structure
- decision logic
- decision organization

not just scheduling or triggering evaluation.

I’m trying to get to that conclusion through implementation, rather than starting from a fixed design.

---

## Repository structure
```text
├── models/
│   ├── model_1_interaction/
│   │   ├── core/
│   │   ├── tests/
│   │   ├── run.py
│   │   ├── README.md
│   │   └── thinking_process.md
│   │
│   ├── model_2_needs/
│   │   ├── core/
│   │   ├── tests/
│   │   ├── run.py
│   │   ├── README.md
│   │   └── thinking_process.md
│   │
│   └── model_3_pipeline/
│       ├── core/
│       ├── tests/
│       ├── run.py
│       ├── README.md
│       └── thinking_process.md
│
├── notes/
│   ├── abm_fundamentals.md
│   └── behavioral_framework_evaluation.md
│
├── reviews/                 # notes from reviewing other candidates (planned)
│
├── motivation.md
├── README.md
├── .gitignore
└── LICENSE
```
---

## Next steps

Some directions I want to explore next:

- implementing a simple BDI-style agent
- comparing how similar models are written in NetLogo or GAMA
- experimenting with separating decision logic from `step()` in a reusable way

---

## Motivation

You can find my background and motivation here:

👉 [motivation.md](motivation.md)

---

## Notes

This repo is intentionally a work in progress.

I’m keeping models simple and documenting what actually happens while building them, rather than trying to present polished final results.
