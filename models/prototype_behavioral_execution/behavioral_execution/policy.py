from __future__ import annotations
from abc import ABC, abstractmethod


class DecisionPolicy(ABC):
    @abstractmethod
    def select(self, agent, scored_actions):
        raise NotImplementedError

    def should_interrupt(self, agent, current_action, scored_actions) -> bool:
        return False

    def should_interrupt_lazy(self, agent, observation) -> bool:
        return False


class GreedyPolicy(DecisionPolicy):
    def select(self, agent, scored_actions):
        if not scored_actions:
            return None
        return max(scored_actions, key=lambda x: x[1])[0]

    def should_interrupt(self, agent, current_action, scored_actions) -> bool:
        return current_action.name == "work" and agent.energy <= 1

    def should_interrupt_lazy(self, agent, observation) -> bool:
        """
        Lightweight trigger for deciding whether a full re-evaluation is needed.
        For this prototype:
        - if there is no current action, full evaluation will happen anyway
        - if the current action is 'work' and energy is critically low,
          reevaluation may be needed to interrupt it
        - otherwise, continue the current action without rescoring
        """
        if agent.current_action is None:
            return False

        return agent.current_action.name == "work" and observation.energy <= 1
