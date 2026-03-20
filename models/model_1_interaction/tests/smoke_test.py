"""VSmall smoke test for the local inequality Mesa project."""

from models.model_1_interaction.core import LocalInequalityModel
# Intentionally lightweight: this only checks that the model runs at all.

def main() -> None:
    model = LocalInequalityModel(width=5, height=5, seed=123)
    for _ in range(3):
        model.step()

    assert len(model.agents) == 25, "Expected one agent per grid cell."
    assert model.compute_gini() >= 0.0, "Gini should be nonnegative."
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
