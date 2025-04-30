import time
import numpy as np
from FaceDetector import FaceDetector
from CameraManager import CameraManager
from DisplayManager import DisplayManager
from GameController import GameController
from IOHandler import IOHandler
from pynq.overlays.base import BaseOverlay

print("Face Frenzy Game Starting...")

# Initialize overlay
base = BaseOverlay("base.bit")

# Initialize components
camera = CameraManager()
detector = FaceDetector()
display = DisplayManager(resolution=(640, 480))
io = IOHandler(base)

# Create game controller
game = GameController(camera=camera, detector=detector, display=display, io=io, max_players=4)

print("Components initialized. Running game loop...")

try:
    while True:
        frame = camera.get_frame()
        if frame is not None:
            game.tick()
            display.show_frame(frame)
            time.sleep(0.05)
        else:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Game interrupted by user.")
finally:
    camera.release()
    display.stop()
    io.clear_leds()