class PredictorStrategy:
    def predict(self, attendance_history: list[int]) -> float:
        raise NotImplementedError


class MovingAveragePredictor(PredictorStrategy):
    def __init__(self, window: int = 5):
        self.window = window

    def predict(self, attendance_history: list[int]) -> float:
        if not attendance_history:
            return 0.0
        recent = attendance_history[-self.window :]
        return sum(recent) / len(recent)
