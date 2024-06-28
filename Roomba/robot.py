import serial
import time

class Robot:
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def send(self, commands):
        for x in commands:
            self.tty.write(bytes([x]))

    def drive_straight(self, duration):
        velocity = 200  # mm/s (positive value for forward, negative for backward)
        radius = 32768  # Special code for driving straight (0x8000)

        # Convert velocity and radius to bytes
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        rad_high_byte = (radius >> 8) & 0xFF
        rad_low_byte = radius & 0xFF

        drive_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
        self.send(drive_command)

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the robot
        self.send([137, 0, 0, 0, 0])

    def drive_and_turn(self, angle):
        # Drive straight for 5 seconds
        self.drive_straight(5)

        # Turn right
        velocity = 200  # mm/s
        radius = 150  # Special code for turning in place clockwise

        # Determine direction and duration based on the angle
        if angle > 0:
            radius = -2000  # Special code for turning in place clockwise
        else:
            radius = 2000  # Special code for turning in place counter-clockwise

        # Calculate duration needed to turn the specified angle
        turning_speed = 90  # degrees per second, adjust based on your robot's turning speed
        duration = abs(angle) / turning_speed

        # Convert velocity and radius to bytes
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        rad_high_byte = (radius >> 8) & 0xFF
        rad_low_byte = radius & 0xFF

        turn_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
        self.send(turn_command)

        # Wait for the calculated duration
        time.sleep(duration)

        # Time to turn 90 degrees (adjust based on your robot's turning speed)
        time.sleep(2)

        # Stop the robot after turning
        self.send([137, 0, 0, 0, 0])

        # Drive straight for another 2 seconds
        self.drive_straight(2)

        # Stop the robot after driving straight
        self.send([137, 0, 0, 0, 0])

    def start(self):
        self.send([128, 132])
        time.sleep(1)

def main():
    robot = Robot()
    robot.start()
    robot.drive_and_turn(90)

if __name__ == '__main__':
    main()
