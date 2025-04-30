import cv2
import sys
import time
import numpy as np  # Needed for fallback frame
from pynq.overlays.base import BaseOverlay
from pynq.lib.video import VideoMode

from FaceDetector import FaceDetector
from CameraManager import CameraManager
from DisplayManager import DisplayManager
from GameController import GameController
from IOHandler import IOHandler

print("Face Frenzy Game Starting...")

# --- Hardware Check: HDMI and Camera ---
print("[*] Checking HDMI output...")
try:
    base = BaseOverlay("base.bit")
    base.video.hdmi_out.configure(VideoMode(640, 480, 24))
    base.video.hdmi_out.start()
    print("[✓] HDMI output initialized.")
except Exception as e:
    print("[✗] HDMI out error:", e)
    sys.exit(1)

print("[*] Checking USB camera...")
camera_test = cv2.VideoCapture(0)
if not camera_test.isOpened():
    print("[✗] USB camera not detected.")
    sys.exit(1)
camera_test.release()
print("[✓] All hardware checks passed.")

# Initialize components (reuse base)
camera = CameraManager()
detector = FaceDetector()
display = DisplayManager(resolution=(640, 480))
io = IOHandler(base)

# Game setup
game = GameController(camera=camera, detector=detector, display=display, io=io, max_players=4)

print("Face Frenzy Components Loaded, Starting...")

try:
    while True:
        frame = camera.get_frame()
        if frame is None:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)  # fallback blank frame

        game.tick()
        display.show_frame(frame)
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Game interrupted by user.")

finally:
    camera.release()
    display.stop()
    io.clear_leds()