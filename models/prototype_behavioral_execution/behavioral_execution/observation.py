from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    energy: int
    max_energy: int
    wealth: int


class ObservationModule(ABC):
    @abstractmethod
    def observe(self, agent) -> Observation:
        raise NotImplementedError


class NeedsObservation(ObservationModule):
    def observe(self, agent) -> Observation:
        return Observation(
            energy=agent.energy,
            max_energy=agent.max_energy,
            wealth=agent.wealth,
        )
