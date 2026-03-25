from baseline_monolithic import MonolithicNeedsAgent
from behavioral_execution.model import SimpleNeedsModel


def run_monolithic(steps: int = 10):
    agent = MonolithicNeedsAgent()
    rows = []
    for tick in range(steps):
        agent.step()
        rows.append(
            {
                "tick": tick,
                "event": agent.last_event,
                "energy": agent.energy,
                "wealth": agent.wealth,
            }
        )
    return rows


def run_behavioral(steps: int = 10):
    model = SimpleNeedsModel(n_agents=1, seed=100)
    agent = model.agents_list[0]
    rows = []
    for tick in range(steps):
        model.step()
        rows.append(
            {
                "tick": tick,
                "event": agent.last_action_event,
                "energy": agent.energy,
                "wealth": agent.wealth,
            }
        )
    return rows


def main() -> None:
    mono = run_monolithic()
    beh = run_behavioral()

    print("Monolithic:")
    for row in mono:
        print(row)

    print("\nBehavioral Execution Layer:")
    for row in beh:
        print(row)


if __name__ == "__main__":
    main()
