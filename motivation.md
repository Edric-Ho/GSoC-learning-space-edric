# Motivation

## Who I am

My background is in mathematics, where most problems are framed in terms of clean relationships between variables. I’m used to starting from an equation, defining assumptions clearly, and working toward something that is internally consistent and interpretable.

At the same time, I tend to be interested in many different kinds of problems. Because of that, I care less about any single topic and more about finding a way of thinking that can connect different domains.

What I found through this project is that agent-based modeling forces exactly that kind of thinking. It requires me to operate on two levels at once. On one level, I have to be very precise about each agent: what it is, what it knows, what rule it follows, and how it changes over time. On another level, I have to think about the system as a whole: how those local interactions combine, what patterns emerge, and what behavior appears that I did not explicitly design.

That shift was not natural for me at first. My instinct was to model outcomes directly, for example, expressing inequality as a function of effort and randomness. But working through this made me realize that I tend to think in a top-down way by default, and that I needed to learn how to build systems from the bottom up instead.

What makes this especially meaningful to me is that this way of thinking applies across very different contexts. It can describe something small and personal, like how roommate chore distribution and conflict emerge from repeated interactions, but also something much more abstract, like how structure forms in mathematical systems built from many interacting components. That connection is what motivates me to keep exploring this direction.

---

## Why Mesa

What makes Mesa different for me is not just that it supports agent-based modeling, but that it makes certain design decisions unavoidable.

When working with equations or more abstract models, it’s easy to hide complexity inside a formula. In Mesa, that is much harder to do. You have to decide explicitly:

- what information an agent has access to
- when decisions are made
- how interactions are structured
- and how state changes over time

These are not just implementation details, they directly affect the behavior of the system.

In my own model, I initially treated the competition process as something simple and local. But once I implemented it in Mesa, I realized that details like overlapping neighborhoods and how often contests occur were not neutral choices. They fundamentally changed the outcome, producing much stronger inequality than I expected.

What Mesa brings, for me, is this kind of forced transparency. It doesn’t let me assume that a mechanism works, it makes me specify it, and then deal with the consequences.

Another thing I find valuable is that Mesa sits at a level where the model is still close to code. That makes it possible to experiment quickly, but also to trace behavior back to specific design choices. I can ask: *which part of the system caused this pattern?* and actually follow it through the implementation.

That combination, explicit structure, direct control over interaction, and the ability to connect code-level decisions to system-level outcomes, is what makes Mesa different from other ways of modeling I’ve used.

It’s not just a tool for simulation, but a way to test whether the mechanisms I think I understand actually produce the behavior I expect.

---

## What I want to learn

I want to understand agent-based modeling at a level where I can explain not just *what* a model does, but *why it behaves the way it does*.

In particular, I’m interested in:

- how interaction structure (grid, network, global) shapes outcomes
- how scheduling and update rules affect system dynamics
- how small implementation details (such as overlapping interactions) amplify over time
- how to design models that remain interpretable as they become more expressive

More recently, I’ve become interested in moving beyond simple rule-based agents toward more structured behavior.

In my current model, behavior is represented through a scoring function. It is simple and easy to analyze, but it hides the decision process. I want to explore what changes when that process is made explicit, for example, when agents balance competing internal states (such as fatigue versus reward), or when decisions unfold over multiple steps instead of being computed in a single formula.

What I’m trying to understand is the boundary between:
- models that are analytically clean
- and models that better capture how decisions are actually made

---

## Where I want to go

I don’t just want to build models, I want to understand how modeling tools shape the kinds of models people end up building.

Working on this project made it clear that small design decisions in the framework, how interactions are structured, how updates are scheduled, how behavior is represented, can have large downstream effects on both usability and outcomes.

I want to reach a point where I can:

- identify friction points in Mesa through actual modeling work
- distinguish between limitations of the model and limitations of the framework
- propose improvements that make it easier to build structured behavioral systems

In the context of the behavioral framework idea, what interests me most is not just implementing a specific theory, but understanding how well Mesa supports different ways of expressing behavior, and where that support starts to break down.

This learning space is my way of making that process visible. Instead of presenting only final results, I’m documenting how my assumptions changed, where the model behaved differently than expected, and what that revealed about both the system and the tools I’m using.

In the short term, my goal is to build models that expose these questions clearly. If I’m selected for GSoC, I want to continue in that direction, using implementation to test ideas, rather than starting from conclusions. Regardless of the outcome of the GSoC application, 
I plan to continue working with Mesa. Building this model has already changed how I think about systems, and I see it as a tool I would keep using and learning from. Contributing back to a project like this — whether through models, documentation, or discussion — feels like a natural next step rather than something tied to a single program.
