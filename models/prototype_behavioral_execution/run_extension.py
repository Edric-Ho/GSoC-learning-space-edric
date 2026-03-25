from behavioral_execution.model import ExtendedNeedsModel


def main() -> None:
    model = ExtendedNeedsModel(n_agents=1, seed=100)

    print("Extended Behavioral Execution Layer trace")
    print("-" * 70)

    for tick in range(12):
        model.step()
        agent = model.agents_list[0]
        current = agent.current_action.name if agent.current_action else "None"
        print(
            f"tick={tick:02d} | "
            f"event={agent.last_action_event:<20} | "
            f"current_action={current:<10} | "
            f"progress={agent.action_progress} | "
            f"energy={agent.energy} | "
            f"wealth={agent.wealth}"
        )


if __name__ == "__main__":
    main()
