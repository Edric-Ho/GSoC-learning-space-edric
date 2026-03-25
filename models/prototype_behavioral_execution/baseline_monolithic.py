class MonolithicNeedsAgent:
    def __init__(self):
        self.energy = 6
        self.max_energy = 10
        self.wealth = 0

        self.current_task = None
        self.task_progress = 0
        self.last_event = "none"

    def step(self):
        # interruption logic
        if self.current_task == "work" and self.energy <= 1:
            self.current_task = None
            self.task_progress = 0
            self.last_event = "work(interrupt)"
            return

        # continue ongoing work task
        if self.current_task == "work":
            self.task_progress += 1

            # work consumes energy every step
            self.energy = max(0, self.energy - 2)

            if self.task_progress < 3:
                self.last_event = "work(continue)"
            else:
                self.wealth += 3
                self.current_task = None
                self.last_event = "work(complete)"
            return

        # emergency rest if energy critically low
        if self.energy <= 1:
            self.energy = min(self.max_energy, self.energy + 4)
            self.task_progress = 1
            self.last_event = "emergency_rest(complete)"
            return

        # normal rest if energy is not high enough
        if self.energy < 5:
            self.energy = min(self.max_energy, self.energy + 2)
            self.task_progress = 1
            self.last_event = "rest(complete)"
            return

        # start working if energy is high enough
        self.current_task = "work"
        self.task_progress = 0
        self.last_event = "work(start)"

        # first step of work happens immediately
        self.task_progress += 1
        self.energy = max(0, self.energy - 2)

        if self.task_progress < 3:
            self.last_event = "work(continue)"
        else:
            self.wealth += 3
            self.current_task = None
            self.last_event = "work(complete)"


def main() -> None:
    agent = MonolithicNeedsAgent()
    print("Monolithic baseline trace")
    print("-" * 70)

    for tick in range(10):
        agent.step()
        print(
            f"tick={tick:02d} | "
            f"event={agent.last_event:<24} | "
            f"current_task={str(agent.current_task):<8} | "
            f"progress={agent.task_progress} | "
            f"energy={agent.energy} | "
            f"wealth={agent.wealth}"
        )


if __name__ == "__main__":
    main()
