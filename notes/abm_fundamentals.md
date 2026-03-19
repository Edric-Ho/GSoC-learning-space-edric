# Agent-Based Modeling (ABM) – Notes

These notes are based on the Mesa "Getting Started" tutorial, but rewritten in my own understanding.

The goal here is not just to remember the API, but to understand how ABM actually works conceptually.

---

## 1. What is an Agent-Based Model?

An agent-based model (ABM) is a simulation where:

- we define many individual entities (agents)
- each agent follows simple rules
- agents interact with each other and/or their environment
- global patterns emerge from these interactions

The key idea is:

> we don’t directly program the global outcome, it emerges.

---

## 2. Why ABM instead of traditional models?

Traditional models often:
- assume averages
- use equations to describe the whole system

ABM instead:
- models individuals explicitly
- allows heterogeneity (agents can be different)
- captures local interaction effects

So ABM is useful when:
- individual behavior matters
- interaction structure matters
- the system is complex or nonlinear

---

## 3. Core components in Mesa

Mesa organizes ABMs into a few key pieces.

---

### 3.1 Model

The **Model**:
- holds the entire simulation state
- initializes agents
- defines global parameters
- controls the simulation step

Key idea:

> the model is the environment + scheduler + data collector

---

### 3.2 Agent

An **Agent**:
- represents an individual entity
- has internal state (variables)
- has behavior (methods like `step()`)

Agents:
- act based on their own state
- may interact with neighbors

Important:

> behavior is local and decentralized

---

### 3.3 Space

Mesa provides different types of space.

Example:
- Grid (MultiGrid, SingleGrid)
- Network

Space defines:
- where agents are located
- who counts as a neighbor

This is important because:

> interaction is usually spatial or network-based

---

### 3.4 Scheduler (implicit in newer Mesa versions)

In many ABMs:
- agents act in some order

Mesa allows:
- sequential updates
- simultaneous updates (step + advance pattern)

Key idea:

> update rules affect results

For example:
- synchronous vs asynchronous updates can lead to different outcomes

---

### 3.5 DataCollector

Used to:
- track metrics over time
- store model-level and agent-level data

Example:
- average wealth
- inequality
- population statistics

Important:

> without data collection, you can’t analyze your model properly

---

## 4. How a typical Mesa model works

A typical simulation loop looks like:

1. initialize model
2. create agents
3. place agents in space
4. repeat:
    - agents compute behavior (`step`)
    - interactions happen
    - state updates (`advance`)
    - collect data

---

## 5. Step vs Advance (important detail)

Mesa often uses:

- `step()`: compute decisions
- `advance()`: apply updates

This avoids problems like:
- order bias
- one agent seeing updated state while others don’t

So:

> all agents act on the same “time snapshot”

---

## 6. Emergence (core concept)

The most important concept in ABM:

> simple local rules → complex global behavior

Examples:
- segregation (Schelling model)
- wealth inequality
- flocking behavior

You do not directly code:
- “create inequality”

Instead, you define:
- rules for interaction

and inequality may emerge.

---

## 7. What makes a “good” ABM

From what I understand so far:

### I. Clear local rules
- agents should have simple, understandable behavior

### II. Meaningful interaction
- agents must influence each other
- not just evolve independently

### III. Minimal but expressive design
- avoid unnecessary complexity
- focus on mechanism

### IV. Observable outcomes
- track metrics
- analyze results

---

## 8. Common mistakes (based on my own attempt)

### 8.1 No interaction
Agents evolve independently → not really ABM

### 8.2 Too centralized
Global ranking / control → breaks decentralization

### 8.3 Overcomplicated agents
Hard to interpret what causes outcomes

### 8.4 No data collection
Can’t evaluate results

---

## 9. What I learned from building my own model

The tutorial made more sense after I actually built something.

Key realizations:

### I. Interaction design matters more than I thought
Small changes in rules can drastically change outcomes

---

### II. Structure matters
Grid vs network vs global interaction leads to different behavior

---

### III. Emergence is sensitive
Unexpected results are common and useful

---

### IV. ABM is more about design than coding
The hardest part is not writing code — it’s choosing the rules

---

## 10. Connection to my project

In my inequality model:

- agents compete locally instead of globally
- outcomes depend on overlapping interactions
- inequality emerges from repeated competition

One key insight:

> how opportunities are structured matters as much as effort or randomness

---

## Final takeaway

ABM is not just simulation.

It is a way to think about systems:

- start from individuals
- define local rules
- observe global patterns

And most importantly:

> unexpected outcomes are part of the process, not a mistake
