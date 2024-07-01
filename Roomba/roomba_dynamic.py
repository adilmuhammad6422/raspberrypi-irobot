import serial
import time

class Robot:
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def send(self, commands):
        print("Sending commands:", commands)  # Debugging print
        for x in commands:
            self.tty.write(bytes([x]))

    def convert_to_bytes(self, velocity, radius):
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        radius_high_byte = (radius >> 8) & 0xFF
        radius_low_byte = radius & 0xFF
        return vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte

    def drive_straight(self, duration):
        velocity = 200  # mm/s (positive value for forward, negative for backward)
        radius = 32768  # Special code for driving straight (0x8000)

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(velocity, radius)
        
        # Send drive command
        drive_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(drive_command)

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the robot
        self.stop()

    def turn_left(self):
        velocity = 200  # mm/s
        radius = 1  # Special code for turning in place counterclockwise

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(velocity, radius)

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(turn_command)
        
        # Adjust the sleep duration to achieve a 90-degree turn
        time.sleep(1)  # Adjust this value as necessary

        # Stop the robot after turning
        self.stop()

    def turn_right(self):
        velocity = 200  # mm/s
        radius = -1  # Special code for turning in place clockwise

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(velocity, radius)

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(turn_command)
        
        # Adjust the sleep duration to achieve a 90-degree turn
        time.sleep(1)  # Adjust this value as necessary

        # Stop the robot after turning
        self.stop()

    def turn_dynamic(self, velocity, angle):
        if angle == 0:
            radius = 32768  # Drive straight
        else:
            radius = 1 / (angle / 90.0)  # Adjust radius proportionally for the given angle

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(velocity, int(radius))

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(turn_command)
        
        # Adjust the sleep duration based on the angle and speed
        time_to_turn = abs(angle) / 90.0  # Adjust this value as necessary
        time.sleep(time_to_turn)

        # Stop the robot after turning
        self.stop()

    def stop(self):
        print("Stopping the robot")  # Debugging print
        self.send([137, 0, 0, 0, 0])

    def drive_and_turn(self):
        # Drive straight for 5 seconds
        self.drive_straight(2)

        # Turn left
        self.turn_left()

        # Drive straight for another 2 seconds
        self.drive_straight(3)

        # Turn right
        self.turn_right()

        # Drive straight for another 2 seconds
        self.drive_straight(2)

        # Turn dynamically by 45 degrees
        self.turn_dynamic(200, 45)

        # Drive straight for another 2 seconds
        self.drive_straight(2)

        # Stop the robot after driving straight
        self.stop()

    def start(self):
        print("Starting the robot")  # Debugging print
        self.send([128, 132])
        time.sleep(1)

def main():
    robot = Robot()
    robot.start()
    robot.drive_and_turn()

if __name__ == '__main__':
    main()
