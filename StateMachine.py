from enum import Enum, auto
import time
import random

class GameState(Enum):
    IDLE = auto()
    GET_READY = auto()
    SHOW_FACES = auto()
    COUNTDOWN = auto()
    CAPTURE_AND_DETECT = auto()
    EVALUATE = auto()
    UPDATE_SCORE = auto()
    GAME_OVER = auto()

class CountdownTimer:
    def start(self, timeout):
        self.timeout = timeout
        self.start_time = time.time()

    def is_finished(self):
        return time.time() - self.start_time >= self.timeout

class OutputManager:
    def display_message(self, msg):
        print(f"[Display] {msg}")

    def feedback_correct(self):
        print("[Feedback] ✅ Correct!")

    def feedback_incorrect(self):
        print("[Feedback] ❌ Incorrect!")

    def display_score(self, score):
        print(f"[Score] {score}")

class GameController:
    def __init__(self, face_detector, camera, countdown_timer, output_manager):
        self.state = GameState.IDLE
        self.face_detector = face_detector
        self.camera = camera
        self.countdown_timer = countdown_timer
        self.output_manager = output_manager

        self.score = 0
        self.strikes = 0
        self.round = 0
        self.max_faces = 5
        self.target_faces = 0
        self.detected_faces = 0
        self.max_strikes = 2

        self.countdown_message_shown = False  # 👈 prevent spam

    def start_game(self):
        self.state = GameState.GET_READY
        self.score = 0
        self.strikes = 0
        self.round = 0
        print("Game started.")

    def update(self):
        if self.state == GameState.GET_READY:
            self.output_manager.display_message("Get Ready...")
            time.sleep(1)
            self.state = GameState.SHOW_FACES

        elif self.state == GameState.SHOW_FACES:
            self.round += 1
            self.target_faces = random.randint(1, self.max_faces)
            self.output_manager.display_message(f"Round {self.round}: Show {self.target_faces} faces!")
            self.countdown_timer.start(3)
            self.countdown_message_shown = False  # 👈 reset flag for new countdown
            self.state = GameState.COUNTDOWN

        elif self.state == GameState.COUNTDOWN:
            if not self.countdown_message_shown:
                self.output_manager.display_message("Countdown...")
                self.countdown_message_shown = True
            if self.countdown_timer.is_finished():
                self.state = GameState.CAPTURE_AND_DETECT

        elif self.state == GameState.CAPTURE_AND_DETECT:
            frame = self.camera.get_frame()
            if frame is None:
                return
            self.detected_faces = self.face_detector.detect_faces(frame)

            import cv2
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow('Face Detection', frame)
            cv2.waitKey(1000)
            self.state = GameState.EVALUATE

        elif self.state == GameState.EVALUATE:
            if self.detected_faces == self.target_faces:
                self.output_manager.feedback_correct()
                self.score += 1
            else:
                self.output_manager.feedback_incorrect()
                self.strikes += 1
            self.state = GameState.UPDATE_SCORE

        elif self.state == GameState.UPDATE_SCORE:
            self.output_manager.display_score(self.score)
            if self.strikes >= self.max_strikes:
                self.state = GameState.GAME_OVER
            else:
                self.state = GameState.SHOW_FACES

        elif self.state == GameState.GAME_OVER:
            self.output_manager.display_message(f"Game Over! Final Score: {self.score}")
            self.state = GameState.IDLE
