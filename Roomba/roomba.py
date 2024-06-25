import serial
import time

def send(tty, commands):
    for x in commands:
        tty.write(chr(x))

def main():
    tty = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=0.01)

    send(tty, [128, 132])
    time.sleep(1)
    while 1:
        time.sleep(100.0/1000.0)

        send(tty, [149, 1, 7])
        inp = tty.read(1)
        if inp:
            bump = ord(inp[0])
            if bump:
                print("Bump, Rotating ...")
                send(tty, [137, 0, 50, 0, 1])
                time.sleep(0.1)
            else:
                send(tty, [137, 0, 200, 128, 0])
        tty.close()

    if __name__ == '__main__':
        main()