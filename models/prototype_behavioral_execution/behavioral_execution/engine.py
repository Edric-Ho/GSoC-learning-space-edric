from __future__ import annotations


class BehaviorEngine:
    def __init__(self, observation_module, evaluator, decision_policy, action_executor):
        self.observation_module = observation_module
        self.evaluator = evaluator
        self.decision_policy = decision_policy
        self.action_executor = action_executor

    def step(self, agent) -> None:
        observation = self.observation_module.observe(agent)

        scored_actions = None
        needs_evaluation = (
                agent.current_action is None
                or self.decision_policy.should_interrupt_lazy(agent, observation)
        )

        if needs_evaluation:
            scored_actions = self.evaluator.score_actions(
                agent, observation, agent.actions
            )

        if agent.current_action and scored_actions:
            if self.decision_policy.should_interrupt(
                    agent, agent.current_action, scored_actions
            ):
                interrupted = agent.current_action.name
                agent.current_action.abort(agent)
                agent.current_action = None
                agent.last_action_event = f"{interrupted}(interrupt)"
                return

        if agent.current_action is None and scored_actions:
            next_action = self.decision_policy.select(agent, scored_actions)
            if next_action is not None:
                next_action.start(agent)
                agent.current_action = next_action

        if agent.current_action is not None:
            self.action_executor.execute(agent)
