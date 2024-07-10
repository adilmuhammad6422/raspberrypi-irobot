# Raspberry Pi-irobot


### How to sign into Raspberry Pi 3 using ssh
Find the IP Address of the Raspberry Pi (hostname -I) in the command line
  on Macbook terminal type "ssh pi@192.168.x.x" to get into Raspberry Pi 3 command line
  then from there, you can type commands through the terminal


### How to get Roomba working
# Update the package list
sudo apt-get update

sudo apt-get upgrade

# Ensure pip is installed:
sudo apt-get install python3-pip

Install pyserial using pip:

pip3 install pyserial


