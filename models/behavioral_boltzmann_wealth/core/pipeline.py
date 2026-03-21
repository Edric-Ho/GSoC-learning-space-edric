import math


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
            "risk_tolerance": agent.risk_tolerance,
        }

    def update_belief(self, agent, observation):
        # no separate belief model yet, just pass forward observed state
        return observation

    def evaluate(self, agent, belief):
        self_wealth = belief["self_wealth"]
        partner_wealth = belief["partner_wealth"]
        risk_tolerance = belief["risk_tolerance"]

        # If agent has no wealth, it cannot transfer
        if self_wealth <= 0:
            return {"p_transfer": 0.0}

        # Behavioral logic:
        # - richer agents are more willing to risk 1 unit
        # - poorer agents are more defensive
        # - relative advantage over partner slightly increases willingness
        wealth_pressure = self_wealth - 1
        relative_pressure = self_wealth - partner_wealth

        absolute_term = 1.0 * wealth_pressure
        relative_term = 0.3 * relative_pressure

        score = (absolute_term + relative_term) * risk_tolerance

        # Smooth probability
        p_transfer = 1 / (1 + math.exp(-score))

        return {"p_transfer": p_transfer}

    def decide(self, agent, evaluation):
        p_transfer = evaluation["p_transfer"]
        return 1 if agent.random.random() < p_transfer else 0

    def act(self, agent, decision):
        return decision
