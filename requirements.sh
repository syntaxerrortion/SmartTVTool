#!/bin/bash


echo "[*] Requirements installing..."


apt update -y && pkg upgrade -y


apt install python3 -y
pip install --upgrade pip --break-system-packages


pip install requests colorama pyfiglet --break-system-packages


apt install nmap -y


apt install adb -y

apt install ffmpeg wget git gcc make meson -y

echo "[*] Scrcpy installing..."
git clone https://github.com/Genymobile/scrcpy.git
cd scrcpy
meson build
cd build
ninja
sudo ninja install
cd ../..


echo "[+] Requirements done!"
