# 🧠 Face Frenzy

**Face Frenzy** is a fast-paced, interactive face detection game that blends embedded hardware with computer vision. Built using **Zynq P2 boards** for hardware interfacing and **Python** for the software layer, this project challenges users to match a given number of faces in front of a USB camera — or lose a life!

This repository contains homework assignment case-based learning exercises for the Designing Software Systems with Embedded Elements (F25) course led by **Associate Professor Krzysztof Sierszecki** at the University of Southern Denmark (SDU).

**Course Instructor**: [Krzysztof Sierszecki](https://portal.findresearcher.sdu.dk/en/persons/krzys)  
**Institution**: University of Southern Denmark (SDU)

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

- Real-time face detection - not really realtime. It was planned using the FPGA, but never implemented. Analysis frames realtime uses too much resources without the FPGA offloading, therefore not viable. There is a FPGA possibility - https://github.com/sefaburakokcu/finn-quantized-yolo in case someone would like to install old software on the board for Python 3.8. Unfortunately for this project, however, that is way out of scope. 
- Seamless hardware-software integration
- Randomized target face count
- Countdown timer for added pressure
- Simple 3-life game mechanic
- Modular and extensible codebase

---

## Startup
In order to run the game, enter the pynq environment by running in ssh:
```
source /etc/profile.d/pynq_venv.sh
source /etc/profile.d/xrt_setup.sh
```
then start the main.py as you normally would. 


> This repository is not affiliated with SDU or Krzysztof Sierszecki
