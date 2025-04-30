import cv2
import os
import time

class FaceDetector:
    def __init__(self):
        cascade_path = "haarcascade_frontalface_default.xml"
        if not os.path.exists(cascade_path):
            raise FileNotFoundError(f"Haar cascade not found at: {cascade_path}")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_faces_with_boxes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        return faces, time.time()  # placeholder for compatibility