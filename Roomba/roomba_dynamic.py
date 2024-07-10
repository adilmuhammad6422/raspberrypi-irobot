import serial
import time
import sys

# Robot class contains the implementation and calling functions for the roomba
class Robot:
    # Initializes the tty and velocity from the parameters
    # default port is '/dev/ttyUSB0'
    # default baudrate is 57600
    # default timeout is 0.01
    # default velocity is 200
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01, velocity=200):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.velocity = velocity

        self.bump_thresh = 1000 # 100 ms
        self.bump_left_time = self.bump_right_time = None
    
    # Sets the velocity of the robot
    def set_velocity(self, velocity):
        print("Setting velocity to:", velocity)  # Debugging print
        self.velocity = velocity

    # Writes Commands to the tty
    def __write_command(self, commands):
        # print("Sending commands:", commands)  # Debugging print
        for x in commands:
            self.tty.write(bytes([x]))
    
    # Calls robot commands
    def __call_command(self, radius):
        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        
        # Send drive command
        command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(command)

    # Helper function to convert velocity and radius 
    # to high bytes and low bytes for the roomba to understand
    def __convert_to_bytes(self, velocity, radius):
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        radius_high_byte = (radius >> 8) & 0xFF
        radius_low_byte = radius & 0xFF
        return vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte

    # Function that makes the robot drive straight for a set duration
    def drive_straight(self, duration):
        print('Driving Straight...')

        self.__call_command(32768) # Calls drive command, 32768 is the radius for driving straight
        time.sleep(duration) # Wait for the specified duration

    # Function for turning x degrees
    # Negative angle for turning left, positive angles for turning right
    def turn_dynamic_angle(self, angle):
        print('Turning ' + str(angle) + ' degree')

        # If the angle is 0 drive straight, otherwise turn porportionally for the given angle
        if angle == 0:
            radius = 32768
        else:
            radius = 1 / (angle / 90.0)


        self.__call_command(int(radius))
        
        # Waits for the angle to turn
        time_to_turn = abs(angle) / 90.0
        # time.sleep(time_to_turn)
        time.sleep(time_to_turn)

    # Stops the robot
    def stop(self):
        print("Stopping the robot...")
        self.__write_command([137, 0, 0, 0, 0]) # Sets the velocity and radius to 0

    # Function for turning the robot while its driving
    # It turns the given radius for a given duration
    def turn_while_driving(self, radius, duration):
        print('Turns left while driving...')
        self.drive_straight(duration)
        self.__call_command(radius)
        
        # Sleeps for the time it takes to turn
        time.sleep(duration)

    # Starts the robot to accept commands
    def start(self):
        print("Starting the robot")  # Debugging print
        self.__write_command([128, 132])
        time.sleep(1)

    # Function to detect if it's a left bump or right bump
    def detect_bumper(self):
        self.__write_command([149, 1, 7])  # Request bumper sensor data
        inp = self.tty.read(1)
        if inp:
            bump = ord(inp)
            # print("Received:", bump, "Binary:", format(bump, '08b'))
            
            bump_right = bump & 0b00000001
            bump_left = bump & 0b00000010
            
            if bump_right:
                if self.bump_right_time is None:
                    self.bump_right_time = time.time()
                    bump_right = False
                else:
                    if time.time() - self.bump_right_time > self.bump_thresh:
                        # right bump has been pressed for bump_thresh time
                        bump_right = True
                        self.bump_right_time = None
                    else:
                        bump_right = False 
            else:
                self.bump_right_time = None
            
            if bump_left:
                if self.bump_left_time is None:
                    self.bump_left_time = time.time()
                    bump_left = False
                else:
                    if time.time() - self.bump_left_time > self.bump_thresh:
                        # left bump has been pressed for bump_thresh time
                        bump_left = True
                        self.bump_left_time = None
                    else:
                        bump_left = False  
            else:
                self.bump_left_time = None  

            return bump_left, bump_right
        return False, False
    

    def turn_left(self, duration=1):
        print('Turning left...')

        radius = 1  # Special code for turning in place counterclockwise

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(turn_command)
        
        # Adjust the sleep duration to achieve the turn
        time.sleep(duration)  # Adjust this value as necessary

        # Stop the robot after turning
        self.stop()

    def turn_right(self, duration=1):
        print('Turning right...')

        radius = -1  # Special code for turning in place clockwise

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)

        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(turn_command)
        
        # Adjust the sleep duration to achieve the turn
        time.sleep(duration)  # Adjust this value as necessary

        # Stop the robot after turning
        self.stop()

    # Function for driving straight with bumper detection
    def drive_straight_with_bumper_detection(self, duration):
        print('Driving Straight with Bumper Detection...')

        radius = 32768  # Special code for driving straight (0x8000)

        # Convert velocity and radius to bytes
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        
        # Send drive command
        drive_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(drive_command)

        start_time = time.time()
        while time.time() - start_time < duration:
            time.sleep(0.1)

            self.__write_command([149, 1, 7])  # Request bumper sensor data
            inp = self.tty.read(1)
            if inp:
                bump = ord(inp)
                # print("Received:", bump, "Binary:", format(bump, '08b'))
                
                bump_left, bump_right = self.detect_bumper()
                
                if bump_right and bump_left:
                    print("Received:", bump, "Binary:", format(bump, '08b'))
                    if bump_left:
                        print("Left bump detected, turning right...")
                        self.stop()
                        break
                        # self.turn_right(duration=0.5)  # Call turn_right for 0.5 seconds
                    elif bump_right:
                        print("Right bump detected, turning left...")
                        self.stop()
                        break
                        # self.turn_left(duration=0.5)  # Call turn_left for 0.5 seconds
                # else:
                #     print('Going straight...')
                #     self.__write_command(drive_command)  # Continue moving forward

        # Stop the robot
        self.stop()



    # def test_bumper_detection(self, duration):
    #     print('Driving Straight with Bumper Detection...')
    #     self.__call_command(32768)

    #     # time.sleep(5)
    #     # bump_left, bump_right = self.detect_bumper()
    #     # print(bump_left, bump_right )

    #     start_time = time.time()
    #     while time.time() - start_time < duration:
    #         bump_left, bump_right = self.detect_bumper()
    #         if bump_left:
    #             print("Left bump detected, turning right...")
    #             self.stop()
    #             break
    #         elif bump_right:
    #             print("Right bump detected, turning left...")
    #             self.stop()
    #             break
    #     # # Stop the robot
    #     # self.stop()

# Testing methods

# Test method for driving and turning
def test_drive_and_turn(robot):
        # Drive straight for 2 seconds
        robot.drive_straight(2)
        robot.stop()
    
        # Turn left
        robot.turn_dynamic_angle(-90)
        robot.stop()

        # Drive straight for another 2 seconds
        robot.drive_straight(3)
        robot.stop()

        # Turn right
        robot.turn_dynamic_angle(90)
        robot.stop()

        # Drive straight for another 2 seconds
        robot.drive_straight(2)
        robot.stop()

        # Turn dynamically by 45 degrees
        robot.turn_dynamic_angle(45)
        robot.stop()

        # Drive straight for another 2 seconds
        robot.drive_straight(2)
        

        # Stop the robot after driving straight
        robot.stop()

# Test method for turning WHILE driving
def test_turn_while_driving(robot):
        # Drive straight for another 2 seconds
        robot.drive_straight(2)

        # Turn left while driving with a radius of 500mm for 2 seconds
        robot.turn_while_driving(-500, 2)

        # Turn right while driving with a radius of 500mm for 2 seconds
        robot.turn_while_driving(500, 2)

        # Stop the robot after driving straight
        robot.stop()

# The main method
def main():
    robot = Robot()
    robot.start()
    robot.set_velocity(200)
    robot.drive_straight_with_bumper_detection(10000)
    

# Calls the main method
if __name__ == '__main__':
    main()