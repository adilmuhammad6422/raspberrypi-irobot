import serial
import time

def send(tty, commands):
    tty.write(bytearray(commands))

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)

    send(tty, [128, 132])
    time.sleep(1)
    while True:
        time.sleep(0.1)

        send(tty, [149, 1, 7])
        inp = tty.read(1)
        if inp:
            bump = ord(inp)
            if bump:
                print("Bump, Rotating ...")
                send(tty, [137, 0, 50, 0, 1])
                time.sleep(0.1)
            else:
                send(tty, [137, 0, 200, 128, 0])

if __name__ == '__main__':
    main()
