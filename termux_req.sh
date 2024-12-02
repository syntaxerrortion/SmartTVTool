#!/bin/bash


echo "[*] Requirements installing..."


pkg update -y && pkg upgrade -y


pkg install python -y
pip install --upgrade pip


pip install requests colorama pyfiglet


pkg install nmap -y


pkg install android-tools -y

echo "[+] Requirements done!"
