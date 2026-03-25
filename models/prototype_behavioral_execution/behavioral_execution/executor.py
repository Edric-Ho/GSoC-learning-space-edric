from __future__ import annotations


class ActionExecutor:
    def execute(self, agent) -> None:
        if agent.current_action is None:
            return

        agent.current_action.step(agent)

        if agent.current_action.is_complete(agent):
            agent.last_action_event = f"{agent.current_action.name}(complete)"
            agent.current_action = None
