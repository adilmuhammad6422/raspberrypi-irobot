# Installing Raspberry Pi OS on a Raspberry Pi 3
[Back to main](README.md)

## Table of Contents
- [When to use this guide](#when-to-use-this-guide)
- [Prerequisites](#prerequisites)
- Factory reset and starting from scratch:
    - [Step 1: Format SD Card](#step-1-format-sd-card)
    - [Step 2: Install Raspberry Pi Image on SD Card](#step-2-write-the-pi-image-to-the-sd-card)
    - [Step 3: Setup Raspberry Pi](#step-3-set-up-the-raspberry-pi)
- [Updating wifi router](#changing-which-router-to-connect-to)


## When to use this guide
This guide should be used when:
- you have a brand new SD card.
- your Pi OS is outdated.
- you want to reset and start from scratch.


## Prerequisites
- **Raspberry Pi 3**
- **SD Card Reader**
- **Computer with internet access**

## Step 1: Format SD Card


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

## Step 2: Write the Pi Image to the SD Card

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


## Changing which router to connect to

Option 1 - using GUI  
Option 2 - using SSH
