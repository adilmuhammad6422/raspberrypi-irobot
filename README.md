# Raspberry Pi-irobot

## Table of Contents
- [TODO List](#todos)
- [About](#-about)
- [Pre-requisites](#prerequisites)
   - [Fresh Install, Updating OS, & Changing Router](RaspberryOs.md)
   - [Connecting to your Pi](#how-to-ssh-remote-connection-into-your-raspberry-pi-from-your-computer)
- [Installation](#installation)
   - [Clone and setup repo](#step-1-setup)
   - [Setup startup file](#step-2-setup-startup-file)
- [Usage](#usage)


## TODOs
### Software Todos:
- [ ] meet with Nathan to ask about the commented todos in the readme
- [ ] readme todos: Sanity check 2 - connect with server, server should send "hello", client should send back "hello OK"
- [ ] readme todos: verify startup file
- [ ] if demo is running, how can we stop it? interrupt added, needs to be verified.
### Physical Todos:
- [ ] All 12 pis have updated OS, installed software
- [ ] All 12 pis can communicate with roomba (Sanity Check 1)
   - [ ] Go forward
   - [ ] Left/Right bumber
   - [ ] Virtual wall
- [ ] All 12 pis can communicate with server (Sanity Check 2)
- [ ] Run all 12 pis together on final testbed
### ICRA hardware list:
- Main Hardware:
   - [ ] 12 + ? rasperry pis
   - [ ] 12 + ? roombas
   - [ ] 12 + ? red cardboard sheets
   - [ ] 1 outdoor nav router 
   - [ ] 4 virtual walls
- Batteries:
   - [ ] 24 battery packs for pis
   - [ ] 24 rechargeable batteries for roombas
   - [ ] 12 Batteries for Virtual walls (2 each)
- Cables
   - [ ] 24 small micro USB cables for battery packs
   - [ ] 24 Roomba chargers
   - [ ] 12 pi - roomba comm cables
- Supporting Hardware:
   - [ ] 1 mouse
   - [ ] 1 keyboard
   - [ ] 1 monitor
   - [ ] 1 HDMI cable
   - [ ] 1 long microUSB cable
   - [ ] 1 USB wall adapter


## 🚀 About
This project provides an interface to send commands to the IRobot Create Roomba. There are two parts:
1. server.py
2. client.cpp

The server.py is meant to run on a pc, connect with the client.cpp that runs on the pis. The server can basically send these commands:
- "runDemo x" // where x is the number of seconds to run the demo for. see [roomba_bumper](Roomba/roomba_bumper.cpp) for details.
- "stop" // to stop the roombas.

See [Usage](#usage).

<!-- TODO: client.py, driver_circle.cpp, roomba_dyna.py, roomba_dynamic.py - are any of these files used? -->

<!-- 
TODO: should we delete this section? It seems to be the same information as below.

## How to connect to Raspberry Pi 3 using ssh
Find the IP Address of the Raspberry Pi (hostname -I) in the command line
  on Macbook terminal type "ssh pi@192.168.x.x" to get into Raspberry Pi 3 command line
  then from there, you can type commands through the terminal 
  -->

## Prerequisites for Installation
For fresh installation of a pi see [this](RaspberryOs.md).
### How to SSH (remote connection) into your Raspberry Pi from your computer
1. If your Pi does not have SSH enabled:
   - Connect your Pi to a monitor
   - Go into preferences and enable SSH and click "ok" then reboot
2. Find Pi's IP Address
   - One way to find the ip address of the pi is to use the router's homepage.
   <!-- - Another way is to connect Get your Raspberry Pi's IP Address
     ```sh
     hostname -I
     ``` -->
3. SSH into Raspberry Pi, password: raspberry
     ```sh
     ssh pi@<Raspberry_Pi_IP_address>
     ```

## Installation
### Step 1: Setup

1. SSH into your Raspberry Pi's IP, password: raspberry

   ```sh
   ssh pi@<Raspberry_Pi_IP_address>
   ```
2. Install dependencies, clone repository and compile libarary:
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

#### Sanity check 1 
Building and running roomba_bumper.cpp to verify pi-roomba communication.
1. Build
     ```sh
     cd raspberrypi-irobot/Roomba
     g++ -o roomba_bumper roomba_bumper.cpp -I/usr/local/include -L/usr/local/lib -lcreate
     ```
2. Run. This should make the roomba go forward at 0.2m/s while turning left/right and 180° if it touches an obstacle on its left/right or detects a virtual wall, respectively. See [roomba_bumper.cpp](Roomba/roomba_bumper.cpp) for details.
     ```sh
     export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
     ./roomba_bumper
     ```

#### Sanity check 2
Building and running client.cpp to verify server-client communication.
```sh
g++ -o client client.cpp -I/usr/local/include -L/usr/local/lib -lcreate -pthread
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./client
```
TODO: incomplete, need to add info on how to setup server on pc, and send basic commands to pi and for pi to respond.

<!-- 
TODO:  The below code seems to create a startup file for running roomba_bumper directly? Is this correct? roomba_bumper is supposed to be a testing file to test whether the pi->roomba communication is working.

## Bash Roomba_bumper
```sh
nano ~/start_robot.sh
```

```bash
 #!/bin/bash
 # Navigate to the directory containing your C++ file
 cd raspberrypi-irobot/Roomba

 git checkout -- .
 git pull origin main

 # Compile the C++ file
 g++ -o roomba_bumper roomba_bumper.cpp -I/usr/local/include -L/usr/local/lib -lcreate

 # Run the compiled program
 export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
 ./roomba_bumper
```

## Startup
```sh
crontab -e
@reboot /home/pi/start_robot.sh
```

### Running

```sh
chmod +x start_robot.sh
./start_robot.sh
``` -->

### Step 2: Setup startup file
<!-- 
I have created a startup file so that the user does not have to. they just have to link it in the raspberry pi.

1. **create startup file**
   ```sh
   nano ~/start_client.sh
   ```

```bash
 #!/bin/bash
cd $HOME/raspberrypi-irobot/Roomba
g++ -o client client.cpp -I/usr/local/include -L/usr/local/lib -lcreate -pthread
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./client
``` -->

To have your pi automatically run client.cpp on startup.
```sh
crontab -e
@reboot /home/pi/raspberrypi-irobot/start_client.sh
```

TODO: verify the startup files.

```sh
chmod +x $HOME/raspberrypi-irobot/start_client.sh
.$HOME/raspberrypi-irobot/start_client.sh
```

## Usage
Now that the pi is setup do this:
1. Connect the pi with the roomba and battery. Keep the pi off by turning the battery pack off. 
2. Run server.py on pc, making sure it is connected to the router
3. Turn on the roomba first - TODO: ask nathan/adil whether we should turn the pi first or roomba first
4. Turn on the batteries of the pis. This should turn on the pi. You should hear a beep sound from the roomba and see on the server that the pis are connecting.
5. Send the command "runDemo 60" via the server. All the roombas should start moving forward at 0.2m/s for 60 seconds while turning left/right if it bumps into anything on its left/right and turning 180° if it senses a virtual wall. 
   1. Optionally, within the 60s you can send the command "stop" from the server. All the roombas should stop momentarily.
