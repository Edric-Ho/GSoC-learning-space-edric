class DecisionPipeline:
    def run(self, agent, partner) -> int:
        observation = self.observe(agent, partner)
        belief = self.update_belief(agent, observation)
        evaluation = self.evaluate(agent, belief)
        decision = self.decide(agent, evaluation)
        return self.act(agent, decision)

    def observe(self, agent, partner):
        return {
            "self_wealth": agent.wealth,
            "partner_wealth": partner.wealth,
        }

    def update_belief(self, agent, observation):
        return observation

    def evaluate(self, agent, belief):
        return belief

    def decide(self, agent, evaluation):
        # Step 1 baseline: if the agent has wealth, it is willing to risk 1 unit
        return 1 if evaluation["self_wealth"] > 0 else 0

    def act(self, agent, decision):
        return decision
