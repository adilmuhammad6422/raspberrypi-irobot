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
   - Click “CHOOSE OS” and select Raspberry Pi OS(64 bit)

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
   - Set hostname to the sticker on the raspberry pi ex. "bp012"
   - Set the username as "pi" and password as "raspberry"
   - Connect to "linksys" wifi
   - Use firefox as default browser
     
5. **Update the System**:
   - Open a terminal and run:
     ```sh
     sudo apt update
     sudo apt upgrade
     ```

# How to SSH (remote connection) into your Raspberry Pi from your computer
1. **Get your IP Address**
   - Go into preferences and enable SSH and click "ok" then reboot
   - Get your Raspberry Pi's IP Address
     ```sh
     hostname -I
     ```

3. **SSH into Raspberry Pi**
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
     ```sh
     sudo apt-get install build-essential cmake libboost-system-dev libboost-thread-dev
     git clone https://github.com/adilmuhammad6422/raspberrypi-irobot.git
     sudo usermod -a -G dialout $USER
     cd raspberrypi-irobot/Roomba
     mkdir build && cd build
     cmake ..
     make
     sudo make install
     ```

## Step 2: Build and Run
1. **Build**
     ```sh
     cd raspberrypi-irobot/Roomba
     g++ -o roomba_bumper roomba_bumper.cpp -I/usr/local/include -L/usr/local/lib -lcreate
     ```
2. **Run**
     ```sh
     export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
     ./roomba_bumper
     ```

## Compile Client.cpp
```sh
g++ client.cpp -o client -lcreate -pthread
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./client
```
