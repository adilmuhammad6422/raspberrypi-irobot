import serial
import time

class Roomba:
    def __init__(self, port):
        self.ser = serial.Serial(port, 57600)

    def send_command(self, command):
        self.ser.write(command)
        time.sleep(0.1)  # small delay to ensure command is sent properly

    def drive(self, velocity, radius):
        # Drive command: 137 [velocity high byte] [velocity low byte] [radius high byte] [radius low byte]
        velocity_high = (velocity >> 8) & 0xFF
        velocity_low = velocity & 0xFF
        radius_high = (radius >> 8) & 0xFF
        radius_low = radius & 0xFF
        command = bytes([137, velocity_high, velocity_low, radius_high, radius_low])
        self.send_command(command)

    def wait_angle(self, angle):
        # Wait angle command: 157 [angle high byte] [angle low byte]
        angle_high = (angle >> 8) & 0xFF
        angle_low = angle & 0xFF
        command = bytes([157, angle_high, angle_low])
        self.send_command(command)

    def stop(self):
        # Stop the robot by setting velocity to 0
        self.drive(0, 0)

    def turn(self, angle, velocity=100):
        # Calculate radius for in-place turn (straight turn in place is 32768 or -1 in OI)
        radius = 32767 if angle > 0 else -32768
        self.drive(velocity, radius)
        self.wait_angle(angle)
        self.stop()

    def close(self):
        self.ser.close()

    def straight(self, duration):
         # Drive command: 137
        velocity = 200  # mm/s (positive value for forward, negative for backward)
        radius = 32768  # Special code for driving straight (0x8000)

        vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte = self.convert_to_bytes(velocity, radius)

        drive_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
        self.send(self.ser, drive_command)

        # Wait for the specified duration
        time.sleep(duration)

        # Stop the robot
        self.send(self.ser, [137, 0, 0, 0, 0])

    def send(tty, commands):
        for x in commands:
            tty.write(bytes([x]))
    
    def convert_to_bytes(self, velocity, radius):
        vel_high_byte = (velocity >> 8) & 0xFF
        vel_low_byte = velocity & 0xFF
        rad_high_byte = (radius >> 8) & 0xFF
        rad_low_byte = radius & 0xFF
        return vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte

# Example usage
if __name__ == "__main__":
    robot = Roomba('/dev/ttyUSB0')

    robot.straight(5)

    robot.close()
