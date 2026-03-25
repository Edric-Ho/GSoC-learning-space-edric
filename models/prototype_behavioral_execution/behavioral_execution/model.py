from __future__ import annotations
import mesa
from .agent import NeedsBehavioralAgent, ExtendedNeedsBehavioralAgent


class SimpleNeedsModel(mesa.Model):
    def __init__(self, n_agents: int = 1, seed: int | None = None):
        super().__init__(seed=seed)
        self.agents_list = [NeedsBehavioralAgent(self) for _ in range(n_agents)]

    def step(self) -> None:
        for agent in self.agents_list:
            agent.step()


class ExtendedNeedsModel(mesa.Model):
    def __init__(self, n_agents: int = 1, seed: int | None = None):
        super().__init__(seed=seed)
        self.agents_list = [ExtendedNeedsBehavioralAgent(self) for _ in range(n_agents)]

    def step(self) -> None:
        for agent in self.agents_list:
            agent.step()
