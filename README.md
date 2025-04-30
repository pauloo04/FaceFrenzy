# 🧠 Face Frenzy

**Face Frenzy** is a fast-paced, interactive face detection game that blends embedded hardware with computer vision. Built using **Zynq P2 boards** for hardware interfacing and **Python** for the software layer, this project challenges users to match a given number of faces in front of a USB camera — or lose a life!

---

## 🎮 How It Works

1. A **random target number** of faces is displayed on screen.
2. A **countdown** begins to give players time to gather the correct number of people.
3. After the countdown, a **frame is captured** using a USB camera.
4. The system uses **OpenCV** to detect how many faces are present.
5. If the detected face count **matches** the target, players move on.
6. If it **does not match**, players **lose one life**.
7. Players have a total of **3 lives** — lose them all and it's game over!

---

## 🧰 Tech Stack

- 🔌 **Hardware**: Zynq P2 Board  
- 🐍 **Software**: Python 3  
- 📸 **Camera**: USB webcam  
- 🧠 **Computer Vision**: OpenCV (Haar Cascades or DNN)

---

## 🚀 Features

- Real-time face detection
- Seamless hardware-software integration
- Randomized target face count
- Countdown timer for added pressure
- Simple 3-life game mechanic
- Modular and extensible codebase

---

## 🛠️ Setup Instructions

> _Coming Soon — or customize based on your actual implementation._

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-frenzy.git
   cd face-frenzy
