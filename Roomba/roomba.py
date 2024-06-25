import serial
import time

# Define the serial port and baud rate.
ser = serial.Serial('49619', 57600)  # Update to the correct port

# Function to send commands to the iRobot Create
def send_command(command):
    ser.write(command.encode())

# Wake up the iRobot Create
ser.write(b'\x80')  # Start command
time.sleep(1)

# Set mode to Safe mode
ser.write(b'\x83')  # Safe mode command
time.sleep(1)

# Move forward
# Opcode for drive: 137 (0x89)
# Velocity high byte, velocity low byte, radius high byte, radius low byte
# Example: Move forward at 200 mm/s, straight (radius 0x8000)
drive_command = bytes([137, 0, 200, 128, 0])
ser.write(drive_command)
time.sleep(2)  # Move for 2 seconds

# Stop
ser.write(bytes([137, 0, 0, 0, 0]))  # Stop command
time.sleep(1)

ser.close()
