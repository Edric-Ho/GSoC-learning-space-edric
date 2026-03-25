from behavioral_execution.model import SimpleNeedsModel


def main() -> None:
    model = SimpleNeedsModel(n_agents=1, seed=42)
    agent = list(model.agents)[0]

    print("Behavioral Execution Layer trace")
    print("-" * 70)

    for tick in range(10):
        if tick == 4:
            agent.energy = 2  # force low-energy interruption scenario

        model.step()

        current = agent.current_action.name if agent.current_action else "None"
        progress = agent.current_action.progress if agent.current_action else "None"

        print(
            f"tick={tick:02d} | "
            f"event={agent.last_action_event:<24} | "
            f"current_action={current:<10} | "
            f"progress={progress} | "
            f"energy={agent.energy} | "
            f"wealth={agent.wealth}"
        )


if __name__ == "__main__":
    main()
