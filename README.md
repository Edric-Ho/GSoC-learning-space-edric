# Mesa GSoC Learning Space
This is a template repository for GSoC candidates working on [Mesa](https://github.com/mesa/mesa). Fork it to create your personal learning space.

---

## Learning Focus

This learning space is structured around a specific question:

> At what point does agent behavior in Mesa become complex enough to require structured abstractions?

While building models, I observed a distinction between:

- interaction-driven systems, where simple agent rules are sufficient
- decision-driven systems, where agent logic becomes increasingly complex and difficult to structure

This repository explores that transition through progressively more complex models and reviews of existing Mesa examples.

In particular, I focus on:

- how agent behavior is currently implemented in Mesa
- where decision logic becomes difficult to manage
- what patterns emerge when behavior is made more explicit

Relevant notes and reviews:
- `reviews/behavioral_gaps_in_mesa_examples.md`

This aligns with the **Behavioral Framework** project idea, where the goal is to understand and improve how Mesa supports agent decision-making through implementation and experimentation.

---

## What is this?
Before contributing to Mesa, you need to understand Mesa — not just the API, but how agent-based models work and how Mesa's pieces fit together. This repo is your space to do that learning, visibly.

**The idea is simple: build models first, contribute second.**

This repo is also your chance to practice the open-source skills that make contributions successful: clear communication, clean git history, good documentation, collaboration, and code review. These matter as much as the code itself.

_Everything here is a suggestion, nothing is mandatory. It's a tool to help you structure your own learning process. Use as you see fit._

## Why build models?
Mesa is a library *for modellers*. If you want to improve it, you need to experience it the way its users do. That means building models — not just reading the source code or tutorials.

When you build models, you discover things you can't learn any other way:
- **Where Mesa helps and where it gets in the way.** You'll hit friction points, confusing APIs, missing features, unclear documentation. These are the real problems worth solving — and you found them because you needed something to work, not because you were looking for a PR to open.
- **How the pieces fit together.** Mesa has agents, models, spaces, data collection, visualization, event scheduling. Reading about them is different from wiring them together in a model that actually does something. Building gives you the architectural intuition that makes your contributions fit naturally into the framework.
- **What modellers care about.** The best Mesa contributions historically come from people who hit a real problem in their own work. They understand the context because they live in it. Building models puts you in that position.

Without this experience, it's very hard to make contributions that actually help Mesa's users. You might write code that compiles and passes tests but solves a problem nobody has, or solves it in a way that doesn't fit how modellers think. Building models first prevents that.

## How to use this repo
### 1. Fork this template
Click "Use this template" (or fork) to create your own copy under your GitHub account.

### 2. Fill in your motivation
Edit `motivation.md` — who you are, why Mesa, what you want to learn, where you want to go. Keep it honest and concise.

### 3. Build models
This is the core of the repo. Build Mesa models in the `models/` folder. Start simple, increase complexity. Each model should have its own folder with:
- The model code
- A `README.md` covering:
    - What the model does and why you chose it
    - What Mesa features it uses
    - What you learned building it
    - What was hard, what surprised you, what you'd do differently

**Focus on learning, not impressing.** A simple model with a thoughtful README is worth more than a complex model you can't explain.

### 4. Review and collaborate
This is where you practice the collaborative side of open source:
- **Review others' work**: Find another GSoC candidate's learning repo and open issues or PRs with feedback on their models. Be constructive and specific.
- **Work together**: Build a model with another candidate. Use branches, PRs, and code review — the same workflow you'd use on Mesa itself.
- **Document your reviews**: Keep notes in `reviews/` about models you reviewed and what you learned from reading someone else's code.

Collaboration is not required, but it's noticed and valued. If you and another candidate review each other's models, improve each other's code, or build something together using proper git workflow — that demonstrates exactly the skills Mesa needs.

### 5. Link to your Mesa PRs
When you open a PR on any Mesa repo, link to the relevant work in this learning space. This gives reviewers context for your understanding without having to extract it through the review process.

---

## Repo structure
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
├── reviews/
│   └── behavioral_gaps_in_mesa_examples.md
│
├── motivation.md
├── README.md
├── .gitignore
└── LICENSE
```
---

## What makes a good learning space?
- **Models that show progression.** Start with a basic model (Boltzmann Wealth, Schelling), then build something that stretches you — a model that uses discrete spaces, PropertyLayers, event scheduling, data collection, or visualization.
- **Honest READMEs.** "I got stuck on X and solved it by Y" is more useful than a polished summary. We want to see your thinking, not a press release.
- **Clean git practices.** Meaningful commit messages, branches for separate models, no giant "add everything" commits. This is practice for contributing to Mesa.
- **Engagement with others.** Reviewing someone else's model, suggesting improvements, or building together shows you understand that open source is collaborative.

## Suggested starting points
1. Go through Mesa's [introductory tutorials](https://mesa.readthedocs.io/latest/getting_started.html)
2. Study the [core examples](https://github.com/mesa/mesa/tree/main/mesa/examples) — don't just run them, read the code and understand the design choices
3. Build your own version of a classic ABM (Schelling, Sugarscape, flocking, etc.)
4. Then build something original — a model for a domain you're interested in
5. Read the [Mesa 3.5 release notes](https://github.com/mesa/mesa/releases) to understand recent changes and direction
6. Look at [open discussions](https://github.com/mesa/mesa/discussions) to understand what Mesa is working toward

## Resources
- [Mesa documentation](https://mesa.readthedocs.io/)
- [Mesa contributing guide](https://github.com/mesa/mesa/blob/main/CONTRIBUTING.md)
- [Mesa migration guide](https://mesa.readthedocs.io/latest/migration_guide.html)
- [Community examples](https://github.com/mesa/mesa-examples)
- [ABM concepts MOOC](https://ocw.tudelft.nl/course-lectures/agent-based-modeling/)
- [Practical Mesa MOOC](https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa)
- [Matrix chat](https://matrix.to/#/#project-mesa:matrix.org)
