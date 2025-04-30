#!/bin/bash

# Ensure this script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo ./start.sh"
  exit 1
fi

echo "[+] Setting up PYNQ environment..."
source /etc/profile.d/pynq_venv.sh
source /etc/profile.d/xrt_setup.sh

echo "[+] Launching Face Frenzy game..."
python3 /home/xilinx/case-II/main.py