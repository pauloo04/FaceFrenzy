from FaceDetector import FaceDetector
from CameraManager import PCCameraManager
import time

cameraManager = PCCameraManager()
detector = FaceDetector()

try:
    for _ in range(10):
        frame = cameraManager.get_frame()
        count = detector.detect_faces(frame)
        print(f"Detected {count} face(s)")
        time.sleep(1)
finally:
    cameraManager.release()
