from FaceDetector import FaceDetector
from CameraManager import PCCameraManager
from StateMachine import GameController, CountdownTimer, OutputManager, GameState
import cv2

def main():
    face_detector = FaceDetector()
    camera = PCCameraManager()
    countdown = CountdownTimer()
    output = OutputManager()
    controller = GameController(face_detector, camera, countdown, output)

    controller.start_game()

    while True:
        controller.update()
        if controller.state == GameState.IDLE:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quit signal received.")
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
