import serial
import time

def send(tty, commands):
    for x in commands:
        tty.write(bytes([x]))

def convert_to_bytes(velocity, radius):
    vel_high_byte = (velocity >> 8) & 0xFF
    vel_low_byte = velocity & 0xFF
    rad_high_byte = (radius >> 8) & 0xFF
    rad_low_byte = radius & 0xFF
    return vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte

def wait_angle(tty, angle):
    angle_high = (angle >> 8) & 0xFF
    angle_low = angle & 0xFF
    tty.write(bytes([157, angle_high, angle_low]))

# def turn_angle(tty, angle):
#     radius = 32767 if angle > 0 else -32768
#     drive_straight(tty, radius)
#     self.wait_angle(angle)

def turn(tty, angle, velocity=100):
        # Calculate radius for in-place turn (straight turn in place is 32768 or -1 in OI)
        radius = 32767 if angle > 0 else -32768
        drive(tty, velocity, radius)
        wait_angle(angle)
        stop()

def drive(tty, velocity, radius):
        # Drive command: 137 [velocity high byte] [velocity low byte] [radius high byte] [radius low byte]
        velocity_high = (velocity >> 8) & 0xFF
        velocity_low = velocity & 0xFF
        radius_high = (radius >> 8) & 0xFF
        radius_low = radius & 0xFF
        command = bytes([137, velocity_high, velocity_low, radius_high, radius_low])
        send_command(tty, command)

def send_command(tty, command):
        tty.write(command)
        time.sleep(0.1)  # small delay to ensure command is sent properly

def stop():
        # Stop the robot by setting velocity to 0
        drive(0, 0)

def drive_straight(tty, duration):
    # Drive command: 137
    velocity = 200  # mm/s (positive value for forward, negative for backward)
    radius = 32768  # Special code for driving straight (0x8000)

    vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte = convert_to_bytes(velocity, radius)

    drive_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    send(tty, drive_command)

    # Wait for the specified duration
    time.sleep(duration)

    # Stop the robot
    send(tty, [137, 0, 0, 0, 0])

def drive_and_turn(tty):
    # Drive straight for 5 seconds
    drive_straight(tty, 5)

    # Turn right 90 degrees
    turn(tty, 90, 100)

    drive_straight(tty, 5)

    tty.close()

    # velocity = 200  # mm/s
    # radius = -140  # Special code for turning in place clockwise

    # vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte = convert_to_bytes(velocity, radius)
    # turn_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    # send(tty, turn_command)

    # Time to turn 90 degrees (adjust based on your robot's turning speed)
    # time.sleep(2)

    # Stop the robot after turning
    # send(tty, [137, 0, 0, 0, 0])

    # Drive straight for another 5 seconds
    
    # tty.close()

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=0.01)

    send(tty, [128, 132])
    time.sleep(1)

    #drive_straight(tty, 5)
    drive_and_turn(tty)

    # try:
    #     while True:
    #         time.sleep(0.1)

    #         send(tty, [149, 1, 7])
    #         inp = tty.read(1)
    #         if inp:
    #             bump = inp[0]
    #             if bump:
    #                 print("Bump, Rotating ...")
    #                 send(tty, [137, 0, 50, 0, 1])
    #                 time.sleep(0.1)
    #             else:
    #                 send(tty, [137, 0, 200, 128, 0])
    # except KeyboardInterrupt:
    #     # Gracefully close the serial connection on exit
    #     tty.close()

if __name__ == '__main__':
    main()
