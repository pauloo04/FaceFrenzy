🧠 Face Frenzy
Face Frenzy is a fast-paced interactive face detection game built using Zynq P2 boards for hardware control and Python for software logic. Designed for real-time engagement, the game challenges players to match a randomly generated face count using actual people in front of a USB camera.

🎮 Game Overview
The system displays a target number of faces the players must match.

A countdown timer begins.

After the countdown, a frame is captured using a USB camera.

The system uses face detection algorithms to count the number of faces.

If the detected face count matches the target, the player continues.

If it doesn’t match, the player loses one life.

Players have a total of 3 lives—game over if they lose them all!

🧰 Tech Stack
Hardware: Zynq P2 board for system control and interfacing

Software: Python (OpenCV for face detection)

Camera: Standard USB camera

🚀 Features
Real-time face detection using OpenCV

Hardware/software integration with Zynq P2

Dynamic target generation and countdown

Simple 3-life system to track player progress
