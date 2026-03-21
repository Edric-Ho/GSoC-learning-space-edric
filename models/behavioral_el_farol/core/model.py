from mesa import Model
from mesa.datacollection import DataCollector
from .agents import BehavioralElFarolAgent


class BehavioralElFarolModel(Model):
    def __init__(self, n_agents=100, capacity=60, seed=None):
        super().__init__(rng=seed)
        self.capacity = capacity
        self.attendance_history = []
        self.current_attendance = 0

        for _ in range(n_agents):
            BehavioralElFarolAgent(self)

        self.datacollector = DataCollector(
            model_reporters={
                "Attendance": lambda m: m.current_attendance,
                "Overcrowded": lambda m: int(m.current_attendance > m.capacity),
            }
        )

    def step(self):
        self.agents.do("step")
        attendees = [a for a in self.agents if a.intends_to_go]
        self.current_attendance = len(attendees)

        for agent in self.agents:
            agent.finalize_round(self.current_attendance)

        self.attendance_history.append(self.current_attendance)
        self.datacollector.collect(self)
