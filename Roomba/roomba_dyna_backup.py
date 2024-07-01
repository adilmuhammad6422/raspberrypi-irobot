import serial
import time

class Robot:
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def send(self, commands):
        print("Sending commands:", commands)  # Debugging print
        self.tty.write(bytearray(commands))

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

    def stop(self):
        print("Stopping the robot")  # Debugging print
        self.send([137, 0, 0, 0, 0])

    def drive_infinite_and_turn_right_90(self):
        self.send([128, 132])  # Start the robot in Safe mode
        time.sleep(1)

        try:
            while True:
                self.send([137, 0, 200, 128, 0])  # Drive forward
                time.sleep(0.1)
                
                self.send([142, 7])  # Request bump sensor data
                inp = self.tty.read(1)
                if inp:
                    bump = ord(inp) & 0x03  # Check the bump sensors (bits 0 and 1)
                    if bump:
                        print("Bump detected, rotating...")
                        self.send([137, 0, 50, 0, 1])  # Turn in place clockwise
                        time.sleep(0.5)  # Adjust the sleep duration as necessary
                    else:
                        self.send([137, 0, 200, 128, 0])  # Continue driving forward
        except KeyboardInterrupt:
            print("Interrupted, stopping the robot...")
            self.stop()
        
        self.tty.close()

    def start(self):
        print("Starting the robot")  # Debugging print
        self.send([128, 132])
        time.sleep(1)

def main():
    robot = Robot()
    robot.start()
    robot.drive_infinite_and_turn_right_90()

if __name__ == '__main__':
    main()
