from __future__ import annotations
from abc import ABC, abstractmethod


class Evaluator(ABC):
    @abstractmethod
    def score_actions(self, agent, observation, actions):
        raise NotImplementedError


class NeedsEvaluator(Evaluator):
    def score_actions(self, agent, observation, actions):
        scored = []
        for action in actions:
            if action.is_feasible(agent, observation):
                scored.append((action, action.score(agent, observation)))
        return scored
