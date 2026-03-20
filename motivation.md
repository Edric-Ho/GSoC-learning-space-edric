# Motivation

## Who I am

My background is in mathematics, where problems are typically framed through clean, well-defined relationships between variables. However, through working with agent-based models in Mesa, I encountered a fundamentally different kind of problem:

> how do simple local rules give rise to complex, system-level behavior that is not explicitly encoded?

This shift from top-down formulation to bottom-up construction became the central motivation for this project.

I’m used to starting from an equation, defining assumptions clearly, and working toward something that is internally consistent and interpretable. But agent-based modeling requires operating on two levels simultaneously. On one level, I need to be precise about each agent: what it knows, what rules it follows, and how its state evolves. On another level, I need to understand how those local interactions combine into global patterns that were never directly specified.

This way of thinking was not natural for me at first. My instinct was to model outcomes directly, for example expressing inequality as a function of effort and randomness. Through implementation, I realized that this approach misses the mechanisms that actually produce those outcomes. Instead, I had to learn how to construct systems from the bottom up and observe how behavior emerges.

What makes this especially meaningful to me is that this perspective applies across domains. It can describe something concrete, such as how imbalance in roommate responsibilities emerges from repeated interactions, but also something abstract, such as how structure arises in systems composed of many interacting components. That connection is what motivates me to keep exploring this direction.

---

## Why Mesa

What makes Mesa valuable to me is not just that it supports agent-based modeling, but that it forces modeling decisions to be explicit.

When working with equations or more abstract models, it is easy to hide complexity inside a formula. In Mesa, that is much harder to do. I have to decide explicitly:

- what information an agent has access to
- when decisions are made
- how interactions are structured
- how state changes over time

These are not just implementation details; they directly determine the behavior of the system.

In my own work, I initially treated competition as a simple local process. But once I implemented it in Mesa, I realized that details such as overlapping neighborhoods and repeated interactions per timestep were not neutral choices. They fundamentally changed the outcome, producing much stronger inequality than expected.

Mesa, in this sense, acts as a form of constraint. It does not allow me to assume that a mechanism works. It forces me to specify it, and then confront the consequences of that specification.

Another aspect I find valuable is that Mesa keeps models close to code. This makes it possible to experiment quickly while still tracing outcomes back to specific design decisions. When a pattern appears, I can ask: *which part of the system produced this?* and follow it through the implementation.

Through this process, I began to notice that many of the challenges I encountered were not purely modeling issues, but were closely tied to how Mesa structures agent behavior. In particular, questions such as:

- how decision logic should be organized
- how evaluation should be triggered
- how internal state should be represented

are not explicitly addressed by the framework itself.

This observation directly connects to the behavioral framework project idea, which aims to understand how well Mesa supports different forms of agent behavior through implementation rather than assumption.

---

## What I want to learn

I want to understand agent-based modeling at a level where I can explain not just *what* a model does, but *why it behaves the way it does*.

In particular, I am interested in:

- how interaction structure (grid, network, global) shapes outcomes
- how scheduling and update rules affect system dynamics
- how small implementation details amplify over time
- how to design models that remain interpretable as they become more expressive

More recently, my focus has shifted toward structured behavior.

In early models, behavior was represented through simple scoring or threshold rules. These are easy to analyze, but they hide the internal decision process. I became interested in what changes when that process is made explicit, for example when agents balance competing internal pressures (such as recovery versus reward), or when decisions unfold across multiple stages instead of being computed in a single step.

This led me to explore behavioral modeling along three dimensions:

- interaction structure
- internal decision logic
- decision architecture

This perspective did not come from theory alone, but emerged directly from implementing multiple models and observing how different aspects of behavior influenced outcomes.

---

## Where I want to go

I do not just want to build models. I want to understand how modeling frameworks shape the kinds of models people are able to build.

Working through these models made it clear that small design decisions in a framework, such as how interactions are structured, how updates are scheduled, and how behavior is represented, can have large downstream effects on both usability and system behavior.

I want to reach a point where I can:

- identify friction points in Mesa through implementation
- distinguish between limitations of a model and limitations of the framework
- propose improvements grounded in actual modeling experience

In the context of the behavioral framework project, my goal is to contribute not by starting from a predefined abstraction, but by systematically evaluating how different behavioral patterns are currently expressed in Mesa.

The models I have implemented so far reflect this approach:

- Model 1: interaction-driven inequality (interaction structure)
- Model 2: needs-based agents (internal decision logic)
- Model 3: behavioral pipeline (decision architecture)

Together, they form a structured investigation into how Mesa supports behavioral modeling across multiple dimensions.

If selected for GSoC, I would continue this process by:

- extending to additional behavioral paradigms (such as BDI agents)
- comparing implementations with other platforms (NetLogo, GAMA, Agents.jl)
- deriving reusable framework components from observed modeling patterns

This approach aligns with the project’s emphasis on understanding through implementation rather than assuming solutions in advance.

This learning space is my way of making that process visible. Instead of presenting only final results, I am documenting how assumptions change, where models behave unexpectedly, and what that reveals about both the system and the framework.

Regardless of the outcome of the GSoC application, I plan to continue working with Mesa. This project has already changed how I think about systems, and contributing back, whether through models, documentation, or discussion, feels like a natural continuation rather than something tied to a single program.
