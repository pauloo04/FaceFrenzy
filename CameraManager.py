# import cv2

# def get_frame():
#     # Open the first USB camera (device 0)
#     cap = cv2.VideoCapture(0)

#     # Check if the camera opened successfully
#     if not cap.isOpened():
#         print("Cannot open camera")
#         exit()

#     # Capture a single frame
#     ret, frame = cap.read()

#     # Check if frame was captured
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#     else:
#         # Save the frame as an image (optional)
#         cv2.imwrite("/home/xilinx/captured_frame.jpg", frame)
#         print("Frame captured and saved.")

#     # Release the camera
#     cap.release()

from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
base = BaseOverlay("base.bit")

Mode = VideoMode(1920, 1080, 24)
hdmi_out = base.video.hdmi_out
hdmi_out.configure(Mode,PIXEL_BGR)
hdmi_out.start()

frame_out_w = 1920
frame_out_h = 1080
frame_in_w = 1920
frame_in_h = 1080


# SOMETHING IN BETWEEN BEGINNIGN WITH import os


import cv2
np_frame = frame_vga
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

gray = cv2.cvtColor(np_frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detect