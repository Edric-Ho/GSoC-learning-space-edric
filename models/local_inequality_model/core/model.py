# This model is built to isolate one question:
# how local competition, randomness, and cumulative advantage
# can generate inequality over time.
# I'm not trying to make it fully realistic.
# The point is to understand mechanism clearly.
from __future__ import annotations
from typing import List, Tuple
import mesa
import numpy as np
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from .agents import OpportunityAgent
from .metrics import gini, safe_correlation, softmax_sample, top_share


class LocalInequalityModel(mesa.Model):
    """Mesa model for local competition and emergent inequality.

    Each grid cell hosts one agent. In every step:
        1. agents compute a latent score,
        2. each cell center runs a local contest,
        3. winners gain success,
        4. fatigue updates,
        5. model-level metrics are collected.

    The whole setup is kept local on purpose so the inequality is produced
    by decentralized interaction rather than by any global controller.
    """

    def __init__(
        self,
        width: int = 20,
        height: int = 20,
        beta: float = 1.0,
        delta: float = 0.10,
        sigma: float = 0.50,
        lambda_fatigue: float = 0.00,
        effort_low: float = 0.80,
        effort_high: float = 1.20,
        radius: int = 1,
        fatigue_decay: float = 0.80,
        fatigue_gain: float = 0.05,
        win_recovery: float = 0.10,
        seed: int | None = None,
    ) -> None:
        # Basic setup: grid + agents.
        # I use a grid mainly because it naturally defines local neighborhoods,
        # which is important for keeping interactions decentralized.
        super().__init__(seed=seed)

        # Core structural parameters
        self.width = width
        self.height = height
        self.beta = beta
        self.delta = delta
        self.sigma = sigma
        self.lambda_fatigue = lambda_fatigue
        self.effort_low = effort_low
        self.effort_high = effort_high
        self.radius = radius

        # Fatigue parameters
        self.fatigue_decay = fatigue_decay
        self.fatigue_gain = fatigue_gain
        self.win_recovery = win_recovery

        # Separate NumPy RNG so runs are reproducible and batch experiments
        # stay easier to reason about.
        self.rng = np.random.default_rng(seed)

        # I use a MultiGrid because the neighborhood structure is explicit
        # and easy to reason about.
        self.grid = MultiGrid(width, height, torus=False)

        # Create one agent per cell with mild effort heterogeneity.
        for x in range(self.width):
            for y in range(self.height):
                effort = self.rng.uniform(self.effort_low, self.effort_high)
                agent = OpportunityAgent(self, effort=effort)
                self.grid.place_agent(agent, (x, y))

        # DataCollector is used to track inequality over time.
        # I specifically care about how fast concentration emerges,
        # not just the final state.
        self.datacollector = DataCollector(
            model_reporters={
                "Gini": self.compute_gini,
                "Top10Share": self.compute_top10_share,
                "MeanSuccess": self.compute_mean_success,
                "VarianceSuccess": self.compute_variance_success,
                "EffortSuccessCorrelation": self.compute_effort_success_correlation,
            },
            agent_reporters={
                "effort": "effort",
                "success": "success",
                "fatigue": "fatigue",
                "last_score": "last_score",
                "won_last_round": "won_last_round",
            },
        )

        self.datacollector.collect(self)

    # ------------------------------
    # Convenience accessors
    # ------------------------------
    def get_successes(self) -> List[int]:
        """Return the current success count for every agent."""
        return [agent.success for agent in self.agents]

    def get_efforts(self) -> List[float]:
        """Return the fixed effort level for every agent."""
        return [agent.effort for agent in self.agents]

    # ------------------------------
    # Model-level metrics
    # ------------------------------
    def compute_gini(self) -> float:
        """Primary inequality metric: Gini coefficient."""
        return gini(self.get_successes())

    def compute_top10_share(self) -> float:
        """Share of total success captured by the top 10% of agents."""
        return top_share(self.get_successes(), top_fraction=0.10)

    def compute_mean_success(self) -> float:
        """Average success across agents."""
        values = self.get_successes()
        return float(np.mean(values)) if values else 0.0

    def compute_variance_success(self) -> float:
        """Variance of success across agents."""
        values = self.get_successes()
        return float(np.var(values)) if values else 0.0

    def compute_effort_success_correlation(self) -> float:
        """Correlation between fixed effort and accumulated success."""
        return safe_correlation(self.get_efforts(), self.get_successes())

    # ------------------------------
    # Local contest helpers
    # ------------------------------
    def get_agents_in_neighborhood(self, pos: Tuple[int, int]) -> List[OpportunityAgent]:
        """Return all agents in the Moore neighborhood around ``pos``.

        The radius is configurable. Since we place one agent per cell, this
        returns a local set of neighboring competitors.
        """
        neighborhood_positions = self.grid.get_neighborhood(
            pos,
            moore=True,
            include_center=True,
            radius=self.radius,
        )
        local_agents: List[OpportunityAgent] = []
        for npos in neighborhood_positions:
            agents_here = self.grid.get_cell_list_contents([npos])
            for agent in agents_here:
                local_agents.append(agent)
        return local_agents

    def run_local_contests(self) -> None:
        """Resolve one local contest around every grid cell.
        I keep this local on purpose: the point is to let inequality emerge
        from overlapping neighborhood competition rather than from a global ranking.
        """
        winners_this_round = set()
        for x in range(self.width):
            for y in range(self.height):
                center = (x, y)
                local_agents = self.get_agents_in_neighborhood(center)
                if not local_agents:
                    continue
                # If an agent has already won once this round, it should not
                # be eligible to win again. This keeps the local structure but
                # removes the strongest within-step amplification effect.
                eligible_agents = [agent for agent in local_agents if agent not in winners_this_round]
                if not eligible_agents:
                    continue
                local_scores = [agent.last_score for agent in eligible_agents]
                winner_idx = softmax_sample(local_scores, self.rng)
                winner = eligible_agents[winner_idx]
                winner.pending_reward += 1
                winners_this_round.add(winner)

    # ------------------------------
    # Main simulation step
    # ------------------------------
    def step(self) -> None:
        # One full round:
        # agents score themselves, local contests resolve, then rewards apply.
        # Because neighborhoods overlap, agents can appear in multiple contests,
        # which is one reason concentration grows quickly in this baseline version.
        self.agents.do("step")
        self.run_local_contests()
        self.agents.do("advance")
        self.datacollector.collect(self)
