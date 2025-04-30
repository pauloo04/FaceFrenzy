import random
import time

class GameState:
    def __init__(self, controller):
        self.controller = controller

    def run_once(self):
        raise NotImplementedError("State must implement run_once()")

class IdleState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.player_count = 2  # min
        self.displaying = False

    def run_once(self):
        btn0, btn1, btn3 = self.controller.io.btn0, self.controller.io.btn1, self.controller.io.btn3

        if btn0.read():
            if self.player_count < 5:
                self.player_count += 1
                time.sleep(0.3)

        if btn1.read():
            if self.player_count > 2:
                self.player_count -= 1
                time.sleep(0.3)

        # Always update overlay text to reflect the current player count
        self.controller.display.set_overlay_text(f"Select players: {self.player_count}\nPress BTN3 to Start")

        if btn3.read():
            self.controller.max_players = self.player_count
            self.controller.display.clear_overlay_text()
            self.controller.set_state(GetReadyState(self.controller))
            time.sleep(0.5)

class GetReadyState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.start_time = time.time()
        self.timeout = 2
        self.controller.round += 1
        self.controller.target_faces = random.randint(0, self.controller.max_players)
        self.controller.display.set_overlay_text(f"Show {self.controller.target_faces} face(s)!")

    def run_once(self):
        if time.time() - self.start_time >= self.timeout:
            self.controller.display.clear_overlay_text()
            self.controller.set_state(CountdownState(self.controller))

class CountdownState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.total_time = random.randint(3, 5)
        self.remaining = self.total_time
        self.last_tick = time.time()
        self.controller.display.set_overlay_text(str(self.remaining))
        self.controller.io.set_led_countdown(self.remaining, self.total_time)

    def run_once(self):
        now = time.time()
        if now - self.last_tick >= 1:
            self.remaining -= 1
            self.last_tick = now
            if self.remaining > 0:
                self.controller.display.set_overlay_text(str(self.remaining))
                self.controller.io.set_led_countdown(self.remaining, self.total_time)
            else:
                self.controller.display.clear_overlay_text()
                self.controller.io.clear_leds()
                self.controller.set_state(CaptureState(self.controller))

class CaptureState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.capture_time = time.time()
        self.captured = False
        self.controller.display.white_screen()

    def run_once(self):
        if not self.captured and time.time() - self.capture_time >= 0.3:
            self.controller.captured_frame = self.controller.camera.get_frame()
            self.captured = True
            self.controller.set_state(DetectState(self.controller))


class DetectState(GameState):
    def run_once(self):
        faces, _ = self.controller.detector.detect_faces_with_boxes(self.controller.captured_frame)
        self.controller.detected_faces = len(faces)
        self.controller.set_state(EvaluateState(self.controller))


class EvaluateState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.start_time = time.time()
        success = self.controller.detected_faces == self.controller.target_faces
        if success:
            self.controller.score += 1
            message = "Correct!"
        else:
            self.controller.strikes += 1
            message = "Wrong!"

        self.controller.io.show_result(success)
        self.controller.display.set_overlay_text(message)

    def run_once(self):
        if time.time() - self.start_time >= 2:
            self.controller.display.clear_overlay_text()
            if self.controller.strikes >= 2:
                self.controller.set_state(GameOverState(self.controller))
            else:
                self.controller.set_state(GetReadyState(self.controller))


class GameOverState(GameState):
    def __init__(self, controller):
        super().__init__(controller)
        self.start_time = time.time()
        self.controller.display.set_overlay_text(f"Game Over\nScore: {self.controller.score}")

    def run_once(self):
        if time.time() - self.start_time >= 3:
            self.controller.display.clear_overlay_text()
            self.controller.reset()
            self.controller.set_state(IdleState(self.controller))


class GameController:
    def __init__(self, camera, detector, display, io, max_players=4):
        self.camera = camera
        self.detector = detector
        self.display = display
        self.io = io
        self.max_players = max_players
        self.reset()
        self.state = IdleState(self)

    def reset(self):
        self.score = 0
        self.strikes = 0
        self.round = 0
        self.target_faces = 0
        self.detected_faces = 0
        self.captured_frame = None

    def set_state(self, new_state):
        self.state = new_state

    def tick(self):
        self.state.run_once()