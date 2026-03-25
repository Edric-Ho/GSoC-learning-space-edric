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
            if not action.is_feasible(agent, observation):
                continue

            score = self.score_action(agent, observation, action)
            scored.append((action, score))

        return scored


class NeedsEvaluator(Evaluator):
    def score_actions(self, agent, observation, actions):
        scored = []

        for action in actions:
            if not action.is_feasible(agent, observation):
                continue

            score = self.score_action(agent, observation, action)
            scored.append((action, score))

        return scored

    def score_action(self, agent, observation, action) -> float:
        if action.name == "emergency_rest":
            return 100.0

        if action.name == "work":
            return 6.0 if observation.energy >= 5 else 2.0

        if action.name == "rest":
            deficit = observation.max_energy - observation.energy
            return float(deficit + 3 if observation.energy <= 2 else deficit)

        if action.name == "leisure":
            if 4 <= observation.energy <= 5:
                return 7.0
            return 1.0

        return 0.0
