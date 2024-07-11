import serial
import time
import sys

# Robot class contains the implementation and calling functions for the Roomba
class Robot:
    def __init__(self, port='/dev/ttyUSB0', baudrate=57600, timeout=0.01, velocity=200):
        self.tty = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.velocity = velocity
        self.bump_thresh = 0.1  # 100 ms (converted to seconds for time.sleep())
        self.bump_left_time = self.bump_right_time = None

    def set_velocity(self, velocity):
        print("Setting velocity to:", velocity)
        self.velocity = velocity

    def __write_command(self, commands):
        for x in commands:
            self.tty.write(bytes([x]))

    def __call_command(self, radius):
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(command)

    def __convert_to_bytes(self, velocity, radius):
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        radius_high_byte = (radius >> 8) & 0xFF
        radius_low_byte = radius & 0xFF
        return vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte

    def drive_straight(self, duration):
        print('Driving Straight...')
        self.__call_command(32768)  # Calls drive command, 32768 is the radius for driving straight
        time.sleep(duration)

    def turn_dynamic_angle(self, angle):
        print('Turning ' + str(angle) + ' degree')
        if angle == 0:
            radius = 32768
        else:
            radius = 1 / (angle / 90.0)
        self.__call_command(int(radius))
        time_to_turn = abs(angle) / 90.0
        time.sleep(time_to_turn)

    def stop(self):
        print("Stopping the robot...")
        self.__write_command([137, 0, 0, 0, 0])

    def turn_while_driving(self, radius, duration):
        print('Turns left while driving...')
        self.drive_straight(duration)
        self.__call_command(radius)
        time.sleep(duration)

    def start(self):
        print("Starting the robot")
        self.__write_command([128, 132])
        time.sleep(1)

    def detect_bumper(self):
        self.__write_command([149, 1, 7])  # Request bumper sensor data
        inp = self.tty.read(1)
        if inp:
            bump = ord(inp)
            bump_right = bump & 0b00000001
            bump_left = bump & 0b00000010
            
            if bump_right:
                if self.bump_right_time is None:
                    self.bump_right_time = time.time()
                elif time.time() - self.bump_right_time > self.bump_thresh:
                    print('Bump right detected for:', self.bump_right_time)
                    self.bump_right_time = None
                    return False, True  # right bump detected
            else:
                self.bump_right_time = None
            
            if bump_left:
                if self.bump_left_time is None:
                    self.bump_left_time = time.time()
                elif time.time() - self.bump_left_time > self.bump_thresh:
                    print('Bump left detected for:', self.bump_left_time)
                    self.bump_left_time = None
                    return True, False  # left bump detected
            else:
                self.bump_left_time = None

        return False, False  # no bump detected

    def turn_left(self, duration=1):
        print('Turning left...')
        radius = 1  # Special code for turning in place counterclockwise
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(turn_command)
        time.sleep(duration)
        self.stop()

    def turn_right(self, duration=1):
        print('Turning right...')
        radius = -1  # Special code for turning in place clockwise
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        turn_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(turn_command)
        time.sleep(duration)
        self.stop()

    def drive_straight_with_bumper_detection(self, duration, angle_to_turn):
        # duration: seconds. the amount of time this test should run for
        # angle_to_turn: degrees. the angle to turn (left or right) when a bump is detected 
        print('Driving Straight with Bumper Detection...')
        radius = 32768  # Special code for driving straight (0x8000)
        vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte = self.__convert_to_bytes(self.velocity, radius)
        drive_command = [137, vel_high_byte, vel_low_byte, radius_high_byte, radius_low_byte]
        self.__write_command(drive_command)
        driving_forward = True

        start_time = time.time()
        while time.time() - start_time < duration:
            time.sleep(0.1)
            bump_left, bump_right = self.detect_bumper()
            if bump_left:
                print("Left bump detected, turning right...")
                driving_forward = False
                self.stop()
                self.turn_dynamic_angle(angle_to_turn)
            elif bump_right:
                print("Right bump detected, turning left...")
                driving_forward = False
                self.stop()
                self.turn_dynamic_angle(-angle_to_turn)
            else:
                if not driving_forward:
                    self.__write_command(drive_command)
                    driving_forward = True

        self.stop()

# Testing methods

def test_drive_and_turn(robot):
    robot.drive_straight(2)
    robot.stop()
    robot.turn_dynamic_angle(-90)
    robot.stop()
    robot.drive_straight(3)
    robot.stop()
    robot.turn_dynamic_angle(90)
    robot.stop()
    robot.drive_straight(2)
    robot.stop()
    robot.turn_dynamic_angle(45)
    robot.stop()
    robot.drive_straight(2)
    robot.stop()

def test_turn_while_driving(robot):
    robot.drive_straight(2)
    robot.turn_while_driving(-500, 2)
    robot.turn_while_driving(500, 2)
    robot.stop()

def main():
    robot = Robot()
    robot.start()
    robot.set_velocity(200)
    robot.drive_straight_with_bumper_detection(30, 90)

if __name__ == '__main__':
    main()
