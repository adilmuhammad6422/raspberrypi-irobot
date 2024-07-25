# Raspberry Pi-irobot

### How to sign into Raspberry Pi 3 using ssh
Find the IP Address of the Raspberry Pi (hostname -I) in the command line
  on Macbook terminal type "ssh pi@192.168.x.x" to get into Raspberry Pi 3 command line
  then from there, you can type commands through the terminal

# Installing Raspberry Pi OS on a Raspberry Pi 3

## Prerequisites
- **Raspberry Pi 3**
- **SD Card Reader**
- **Computer with internet access**

## Step 1: Prepare the SD Card

### 1. Format the SD Card

1. **Download and Install SD Card Formatter**:
   - Visit the [SD Card Formatter download page](https://www.sdcard.org/downloads/formatter/).
   - Scroll down to “SD Memory Card Formatter Download for Windows/Mac”
   - Click on your OS, then scroll down and click accept

2. **Insert the Raspberry Pi's SD Card**:
   - Insert the SD card into your computer’s SD card slot or use a reader.

3. **Open SD Card Formatter**:
   - Launch the SD Card Formatter application.

4. **Select the SD Card**:
   - Choose your SD card from the list of drives.

5. **Choose "Overwrite" Formatting Option**:

6. **Start Formatting**:
   - Click “Format” and confirm.

## Step 2: Write the Image to the SD Card

1. **Download and Install Raspberry Pi Imager**:
   - Visit the [Raspberry Pi Imager download page](https://www.raspberrypi.com/software/).
   - Download and install the version for your OS.

2. **Open Raspberry Pi Imager**:
   - Launch the application.

3. **Choose the Operating System**:
   - Click “CHOOSE OS” and select your preferred Raspberry Pi OS version.

4. **Select Storage**:
   - Click “CHOOSE STORAGE” and select your SD card.

5. **Write the Image**:
   - Click “WRITE” and confirm. Wait for the process to complete.

6. **Eject the SD Card**:
   - Safely eject the SD card from your computer.

## Step 3: Set Up the Raspberry Pi

1. **Insert the SD Card**:
   - Place the SD card into your Raspberry Pi 3.

2. **Connect Peripherals**:
   - Attach a keyboard, mouse, and monitor.

3. **Power Up**:
   - Connect the power supply to boot the Raspberry Pi.

4. **Complete Initial Configuration**:
   - Follow the on-screen setup wizard (language, time zone, Wi-Fi, etc.).
   - Set the username as "pi" and password as "raspberry"
   - Connect to "linksys" wifi

5. **Update the System**:
   - Open a terminal and run:
     ```sh
     sudo apt update
     sudo apt upgrade
     ```

# How to SSH (remote connection) into your Raspberry Pi from your computer
1. **Enable SSH**:
   - Open the Raspberry Pi Configuration tool from the Preferences menu.
   - Go to the Interfaces tab.
   - Enable SSH.
    
2. **Get your IP Address**
   - Get your Raspberry Pi's IP Address
     ```sh
     hostname -I
     ```

4. **SSH into Raspberry Pi**
   - SSH command
     ```sh
     ssh pi@<Raspberry_Pi_IP_address>
     ```

# Libcreate C++ Library
## Step 1: Setup

1. **SSH into your Raspberry Pi's IP**
   - SSH command
     ```sh
     ssh pi@<Raspberry_Pi_IP_address>
     ```
2. **Installation**:
   - Install
     ```sh
     sudo apt-get install build-essential cmake libboost-system-dev libboost-thread-dev
     ```
   - Serial Permissions
     ```sh
     sudo usermod -a -G dialout $USER
     ```
   - CMake
     ```sh
     git clone https://github.com/AutonomyLab/libcreate.git
     cd libcreate
     mkdir build && cd build
     cmake ..
     make
     sudo make install
     ```

## Step 2: Build and Run
1. **Build**
     ```sh
     cd ..
     cd examples
     export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
     ```
2. **Compile**
     ```sh
     g++ -o bumpers bumpers.cpp -I/usr/local/include -L/usr/local/lib -lcreate
     ```     
     
3. **Run**
   ```sh
   ./bumpers create1
   ```


























# How to get Roomba working (Python)
## Update the package list
sudo apt-get update

sudo apt-get upgrade

## Ensure pip is installed:
sudo apt-get install python3-pip

Install pyserial using pip:

pip3 install pyserial


## Update Roomba
rm -rf raspberrypi-irobot

GIT_SSL_NO_VERIFY=true git clone https://github.com/adilmuhammad6422/raspberrypi-irobot.git



