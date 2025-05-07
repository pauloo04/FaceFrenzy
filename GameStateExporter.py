class GameStateExporter:
    def __init__(self, controller):
        self.controller = controller

    def export(self):
        return {
            "score": self.controller.score,
            "round": self.controller.round,
            "strikes": self.controller.strikes,
            "target_faces": self.controller.target_faces,
            "detected_faces": self.controller.detected_faces,
            "current_state": self.controller.state.__class__.__name__,
        }