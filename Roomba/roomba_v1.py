import serial
import time

def send(tty, commands):
    for x in commands:
        tty.write(bytes([x]))

def drive_straight(tty, duration):
    # Drive command: 137
    velocity = 200  # mm/s (positive value for forward, negative for backward)
    radius = 32768  # Special code for driving straight (0x8000)

    # Convert velocity and radius to bytes
    vel_high_byte = (velocity >> 8) & 0xFF
    vel_low_byte = velocity & 0xFF
    rad_high_byte = (radius >> 8) & 0xFF
    rad_low_byte = radius & 0xFF

    drive_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    send(tty, drive_command)

    # Wait for the specified duration
    time.sleep(duration)

    # Stop the robot
    send(tty, [137, 0, 0, 0, 0])

def drive_and_turn(tty):
    # Drive straight for 5 seconds
    drive_straight(tty, 2)

    # Turn right
    velocity = 500  # mm/s
    radius = -2000  # Special code for turning in place clockwise
    radius = 150  # Special code for turning in place clockwise

    # Convert velocity and radius to bytes
    vel_high_byte = (velocity >> 8) & 0xFF
    vel_low_byte = velocity & 0xFF
    rad_high_byte = (radius >> 8) & 0xFF
    rad_low_byte = radius & 0xFF

    turn_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    send(tty, turn_command)

    # Time to turn 90 degrees (adjust based on your robot's turning speed)
    time.sleep(2)

    # Stop the robot after turning
    send(tty, [137, 0, 0, 0, 0])

    # Drive straight for another 5 seconds
    drive_straight(tty, 2)

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=0.01)

    send(tty, [128, 132])
    time.sleep(1)

    drive_and_turn(tty)

if __name__ == '__main__':
    main()