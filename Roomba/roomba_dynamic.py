import serial
import time

class Robot:
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01, velocity=200):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.velocity = velocity
    
    def set_velocity(self, velocity):
        print("Setting velocity to:", velocity)  # Debugging print
        self.velocity = velocity

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

    def drive_straight(self):
        print('Driving Straight...')

        radius = 32768  # Special code for driving straight (0x8000)

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(self.velocity, radius)
        
        # Send drive command
        drive_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(drive_command)

    def turn_right(self):
        print('Turning right...')

        radius = -1  # Special code for turning in place clockwise

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(self.velocity, radius)

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(turn_command)
        
        # Adjust the sleep duration to achieve the turn
        time.sleep(1.0)  # Adjust this value as necessary for a 90-degree turn

        # Stop the robot after turning
        self.stop()
            
    def stop(self):
        print("Stopping the robot")  # Debugging print
        self.send([137, 0, 0, 0, 0])

    def start(self):
        print("Starting the robot")  # Debugging print
        self.send([128, 132])
        time.sleep(1)

    def drive_infinite_with_bumper_detection(self):
        print('Driving Straight with Bumper Detection...')

        radius = 32768  # Special code for driving straight (0x8000)

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.convert_to_bytes(self.velocity, radius)
        
        # Send drive command
        drive_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.send(drive_command)

        while True:
            time.sleep(0.1)

            self.send([149, 1, 7])  # Request bumper sensor data
            inp = self.tty.read(1)
            if inp:
                bump = ord(inp)
                print("Received:", bump, "Binary:", format(bump, '08b'))
                
                bump_right = bump & 0b00000001
                bump_left = bump & 0b00000010
                
                if bump_right or bump_left:
                    print("Bump detected, turning right...")
                    self.turn_right()
                    self.drive_straight()  # Continue moving forward

def main():
    robot = Robot()
    robot.start()
    robot.set_velocity(200)
    robot.drive_infinite_with_bumper_detection()

if __name__ == '__main__':
    main()
