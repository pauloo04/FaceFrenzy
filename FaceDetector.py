import cv2

class FaceDetector:
    def __init__(self, cascade_path="haarcascade_frontalface_default.xml"):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.video_capture = cv2.VideoCapture(0)  # Adjust index if needed

        if not self.video_capture.isOpened():
            raise Exception("Webcam could not be opened.")

    def get_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            raise Exception("Failed to read from camera.")
        return frame

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        return len(faces)

    def release(self):
        self.video_capture.release()
