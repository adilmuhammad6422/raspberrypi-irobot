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

def turn_angle(tty, angle):
    angle_high = (angle >> 8) & 0xFF
    angle_low = angle & 0xFF
    tty.write(bytes([157, angle_high, angle_low]))



def drive_straight(tty, duration):
    # Drive command: 137
    velocity = 200  # mm/s (positive value for forward, negative for backward)
    radius = 32768  # Special code for driving straight (0x8000)

    # Convert velocity and radius to bytes
    vel_high_byte = (velocity >> 8) & 0xFF
    vel_low_byte = velocity & 0xFF
    rad_high_byte = (radius >> 8) & 0xFF
    rad_low_byte = radius & 0xFF
    vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte = convert_to_bytes(velocity, radius)

    drive_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    send(tty, drive_command)

    # Drive straight for 5 seconds
    drive_straight(tty, 5)

    # Turn right
    velocity = 200  # mm/s
    radius = -140  # Special code for turning in place clockwise
    # Turn right 90 degrees
    turn_angle(tty, 90)

    # Convert velocity and radius to bytes
    vel_high_byte = (velocity >> 8) & 0xFF
    vel_low_byte = velocity & 0xFF
    rad_high_byte = (radius >> 8) & 0xFF
    rad_low_byte = radius & 0xFF
    drive_straight(tty, 5)

    tty.close()

    # velocity = 200  # mm/s
    # radius = -140  # Special code for turning in place clockwise

    turn_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    send(tty, turn_command)
    # vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte = convert_to_bytes(velocity, radius)
    # turn_command = [137, vel_high_byte, vel_low_byte, rad_high_byte, rad_low_byte]
    # send(tty, turn_command)

    # Time to turn 90 degrees (adjust based on your robot's turning speed)
    time.sleep(2)
    # time.sleep(2)

    # Stop the robot after turning
    send(tty, [137, 0, 0, 0, 0])
    # send(tty, [137, 0, 0, 0, 0])

    # Drive straight for another 5 seconds
    drive_straight(tty, 5)
    
    # tty.close()

def drive_and_turn(tty):
    # Drive straight for 5 seconds
    drive_straight(tty, 5)

    # Turn right
    velocity = 200  # mm/s
    radius = -120  # Special code for turning in place clockwise
    radius = -140  # Special code for turning in place clockwise

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
    drive_straight(tty, 5)

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=0.01)

    send(tty, [128, 132])
    time.sleep(1)

    #drive_straight(tty, 5)
    drive_and_turn(tty, 5)

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