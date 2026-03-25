from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Action(ABC):
    name: str = "action"

    def __init__(self) -> None:
        self.progress = 0

    @abstractmethod
    def is_feasible(self, agent: Any, observation: Any) -> bool:
        raise NotImplementedError

    def start(self, agent: Any) -> None:
        self.progress = 0

    @abstractmethod
    def step(self, agent: Any) -> None:
        raise NotImplementedError

    def abort(self, agent: Any) -> None:
        self.progress = 0

    def is_complete(self, agent: Any) -> bool:
        return True
