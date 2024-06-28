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

    def turn_angle(self, angle, speed):
        # angle: desired turn angle in degrees
        # speed: speed of the turn in mm/s

        # Convert angle to radians
        angle_rad = angle * (3.14159 / 180.0)

        # Calculate time to turn based on the speed and angle
        # Assuming wheel base (distance between wheels) of 235 mm
        wheel_base = 235.0

        # Turn radius for in-place turn is half of the wheel base
        turn_radius = wheel_base / 2.0

        # Time to turn (seconds)
        turn_time = (angle_rad * turn_radius) / speed

        # Command for turning in place (clockwise or counterclockwise)
        if angle > 0:
            # Turn left
            left_speed = -speed
            right_speed = speed
        else:
            # Turn right
            left_speed = speed
            right_speed = -speed

        # Convert speeds to high and low byte
        left_speed_high = (left_speed >> 8) & 0xFF
        left_speed_low = left_speed & 0xFF
        right_speed_high = (right_speed >> 8) & 0xFF
        right_speed_low = right_speed & 0xFF

        # Drive command (137) + wheel speeds
        command = [137, right_speed_high, right_speed_low, left_speed_high, left_speed_low]
        self.send(bytearray(command))

        # Wait for the turn to complete
        time.sleep(abs(turn_time))

        # Stop the robot
        self.send([137, 0, 0, 0, 0])

    def drive_and_turn(self):
        # Drive straight for 5 seconds
        self.drive_straight(5)

        # Turn 90 degrees to the right
        self.turn_angle(-90, 200)

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
    robot.drive_and_turn()

if __name__ == '__main__':
    main()
