# Each agent is intentionally simple:
# a fixed effort level, an evolving success count, and a few temporary states.
# I want most of the interesting behavior to come from local interaction,
# not from making the agents themselves too complicated.
from __future__ import annotations
import mesa


class OpportunityAgent(mesa.Agent):
    """Agent that competes for local opportunities.
    each round the agent gets a score based on effort, past success,
    fatigue, and a random shock. That score is then used in local contests.
    """

    def __init__(self, model: "LocalInequalityModel", effort: float) -> None:
        # Effort is fixed at initialization.
        # I'm treating it as a baseline characteristic rather than something that evolves.
        super().__init__(model)
        self.effort = float(effort)
        self.success = 0
        self.fatigue = 0.0
        self.last_score = 0.0
        self.pending_reward = 0
        self.won_last_round = False

    def compute_score(self) -> float:
        # This is the key function that determines competition outcomes.
        # It combines:
        # - effort (baseline)
        # - success (path dependence)
        # - randomness (noise / luck)
        # The weights control how "deterministic" vs "random" the system feels.
        epsilon = self.model.rng.normal(loc=0.0, scale=self.model.sigma)
        score = (
            self.model.beta * self.effort
            + self.model.delta * self.success
            - self.model.lambda_fatigue * self.fatigue
            + epsilon
        )
        return float(score)

    def step(self) -> None:
        """Compute this round's score and reset temporary state."""
        self.last_score = self.compute_score()
        self.pending_reward = 0
        self.won_last_round = False

    def advance(self) -> None:
        # Fatigue is a small friction term.
        # It builds with effort and eases a bit after winning.
        if self.pending_reward > 0:
            self.success += self.pending_reward
            self.won_last_round = True

        self.fatigue = (
            self.model.fatigue_decay * self.fatigue
            + self.model.fatigue_gain * self.effort
            - self.model.win_recovery * self.pending_reward
        )
        self.fatigue = max(0.0, self.fatigue)
