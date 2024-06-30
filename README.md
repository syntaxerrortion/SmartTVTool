# SmartTVTool
By using the adb port on the smart TV, you can play the (.mp4) format you want on your smart TV with this tool.


### Smart TV Tool Explanation

#### Purpose:
This tool is designed to detect Smart TVs or Android TV devices on your local network and send specific commands to these devices. Specifically, this tool aims to connect to devices via ADB (Android Debug Bridge), assuming that port 5555 is open on the devices.

#### Features:
1. **Network Scanning**: Scans the local network to detect devices with port 5555 open.
2. **Device Connection**: Connects to detected devices using ADB.
3. **File Upload and Video Playback**: Uploads a specified video file to the device and plays the video on the device.

#### Usage Steps:

1. **Starting the Tool**:
   - When you run the tool, the terminal screen is cleared, and the main menu is displayed in yellow. The user is presented with two options: "Scan & Execute" and "Exit".
   - The `Scan & Execute` option scans the network for devices and executes specific commands.
   - The `Exit` option terminates the tool.

2. **Network Scanning and Device Connection**:
   - When the user selects the "Scan & Execute" option, the tool scans the local network for devices with port 5555 open and lists them.
   - The user selects a device from the list, and the tool attempts to connect to this device via ADB.
   - If the connection is successful, the user is prompted to specify a video file to upload to the device.

3. **File Upload and Video Playback**:
   - After the user specifies the video file, the tool uploads this file to the device.
   - Once the file is uploaded, the tool sends a command to the device to play the video file.
   - If the video cannot be played, an error message is displayed.

### Important Points:
- **ADB (Android Debug Bridge)**: This tool connects to devices and sends commands using ADB. Ensure that ADB is correctly installed and operational on both the device and the computer.
- **Nmap**: The network scanning is done using `nmap`. Ensure `nmap` is installed on your computer and is included in the PATH variable.
- **Security**: Tools like this should only be used for legal and ethical purposes. Unauthorized access to others' networks and devices is illegal and can have serious consequences.

This tool facilitates the process of sending files and playing videos on Smart TV or Android TV devices on your network. However, always ensure to operate within ethical and legal boundaries.
