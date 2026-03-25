from __future__ import annotations
import mesa
from .agent import NeedsBehavioralAgent, ExtendedNeedsBehavioralAgent


class SimpleNeedsModel(mesa.Model):
    def __init__(self, n_agents: int = 1, seed: int | None = None):
        super().__init__(seed=seed)

        for _ in range(n_agents):
            NeedsBehavioralAgent(self)

    def step(self) -> None:
        self.agents.shuffle_do("step")


class ExtendedNeedsModel(mesa.Model):
    def __init__(self, n_agents: int = 1, seed: int | None = None):
        super().__init__(seed=seed)

        for _ in range(n_agents):
            ExtendedNeedsBehavioralAgent(self)

    def step(self) -> None:
        self.agents.shuffle_do("step")
