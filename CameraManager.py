import cv2

class PCCameraManager:
    def __init__(self):
        # Open the first USB camera (device 0)
        self.cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

    def get_frame(self):
        # Capture a single frame
        ret, frame = self.cap.read()

        # Check if frame was captured
        if not ret:
            print("Can't receive frame. Exiting ...")
        else:
            return frame

    def release(self):
        # Release the camera
        self.cap.release()
