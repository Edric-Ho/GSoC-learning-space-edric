from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Action(ABC):
    name: str = "action"

    @abstractmethod
    def is_feasible(self, agent: Any, observation: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def score(self, agent: Any, observation: Any) -> float:
        raise NotImplementedError

    def start(self, agent: Any) -> None:
        return None

    @abstractmethod
    def step(self, agent: Any) -> None:
        raise NotImplementedError

    def abort(self, agent: Any) -> None:
        return None

    def is_complete(self, agent: Any) -> bool:
        return True
