import serial
import time

def send(tty, commands):
    tty.write(bytearray(commands))
    print("Sent:", commands)

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)

    send(tty, [128, 132])  # Start the robot in safe mode
    time.sleep(1)
    
    while True:
        time.sleep(0.1)

        send(tty, [149, 1, 7])  # Request bumper sensor data
        inp = tty.read(1)
        if inp:
            bump = ord(inp)
            print("Received:", bump, "Binary:", format(bump, '08b'))
            
            bump_right = bump & 0b00000001
            bump_left = bump & 0b00000010
            
            if bump_right or bump_left:
                print("Bump detected, Rotating ...")
                send(tty, [137, 0, 50, 0, 1])  # Rotate command
                time.sleep(0.1)
            else:
                send(tty, [137, 0, 200, 128, 0])  # Move forward command

if __name__ == '__main__':
    main()
