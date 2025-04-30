from FaceDetector import FaceDetector
import time

detector = FaceDetector()

try:
    for _ in range(10):
        frame = detector.get_frame()
        count = detector.detect_faces(frame)
        print(f"Detected {count} face(s)")
        time.sleep(1)
finally:
    detector.release()
