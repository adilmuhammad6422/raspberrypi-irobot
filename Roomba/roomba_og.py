import serial
import time

def send(tty, commands):
    for x in commands:
        tty.write(bytes([x]))

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=0.01)

    send(tty, [128, 132])  # Start and set the mode
    time.sleep(1)
    
    while True:
        time.sleep(100.0 / 1000.0)
        
        send(tty, [149, 1, 7])  # Request sensor data
        inp = tty.read(10)  # Read more bytes to capture the response
        
        if inp:
            bump = inp[0] & 0x03  # Extract bump data (assuming bump data is in the first byte)
            if bump:
                print("Bump, Rotating ...")
                send(tty, [137, 0, 50, 0, 1])  # Rotate
                time.sleep(0.1)
            else:
                send(tty, [137, 0, 200, 128, 0])  # Move forward

    tty.close()

if __name__ == '__main__':
    main()
