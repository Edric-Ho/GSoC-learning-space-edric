import math

class DecisionPipeline:
    def run(self, agent) -> None:
        observation = self.observe(agent)
        belief = self.update_belief(agent, observation)
        evaluation = self.evaluate(agent, belief)
        decision = self.decide(agent, evaluation)
        self.act(agent, decision)

    def observe(self, agent):
        return {
            "attendance_history": list(agent.model.attendance_history),
            "capacity": agent.model.capacity,
            "last_payoff": agent.last_payoff,
        }

    def update_belief(self, agent, observation):
        prediction = agent.strategy.predict(observation["attendance_history"])
        agent.predicted_attendance = prediction
        return {"predicted_attendance": prediction}

    def evaluate(self, agent, belief):
        predicted = belief["predicted_attendance"]
        capacity = agent.model.capacity
        go_value = capacity - predicted
        stay_value = 0
        return {"go_value": go_value, "stay_value": stay_value}

    def decide(self, agent, evaluation):
        diff = evaluation["go_value"] - evaluation["stay_value"]
        p_go = 1 / (1 + math.exp(-0.15 * diff))
        return "go" if agent.random.random() < p_go else "stay"

    def act(self, agent, decision):
        agent.intends_to_go = decision == "go"
