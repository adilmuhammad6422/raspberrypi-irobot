import socket
from roomba_dyna import Robot
import time

HOST = "192.168.1.102"  # Change this to your computer IP address
PORT = 44700  # Port to connect to

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

robot = Robot()  # Create an instance of Robot
robot.start()  # Start the robot
robot.set_velocity(200)

try:
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        command_parts = response.split()
        command = command_parts[0]
        parameters = []
        param1 = None
        if len(command_parts) > 1:
            try:
               param1 = int(command_parts[1])
               param2 = int(command_parts[2])
            except ValueError:
                print("space error")
            except IndexError:
                print("index out of bounds")

        if response:
            if command == 'straight':
                print("Roomba going straight.")
                robot.drive_straight()  # Drive straight 
                time.sleep(param1)  # sleep for param1 seconds
                robot.stop()    # stop
                client_socket.sendall(b'going straight')
            elif command == 'left':
                print("Roomba going left.")
                robot.stop()
                robot.turn_dynamic_angle(param1)  # Turn left by 90 degrees as an example
                robot.stop()
                client_socket.sendall(b'turning left')
            elif command == 'right':
                print("Roomba going right.")
                robot.stop()
                robot.turn_dynamic_angle(-param1)  # Turn right by 90 degrees as an example
                robot.stop()
                client_socket.sendall(b'turning right')
            elif command == 'stop':
                print("Stopping..")
                robot.stop()  # Stop the robot
                client_socket.sendall(b'stopping')
            elif command == 'quit':
                print("Quitting.")
                robot.stop()  # Ensure the robot stops before quitting
                client_socket.sendall(b'quitting')
                client_socket.close()
                break
            elif command == "forward_with_bump":
                print("Roomba going forward with bump.")
                robot.stop()
                robot.drive_straight_with_bumper_detection(param1, param2)  # goes forward and turns param2 right/left for param1 duration
                robot.stop()
                client_socket.sendall(b'going forward with bump detection')
            elif command == "read_bumper":
                print("reading bumper")
                left_bump, right_bump = robot.detect_bumper()
                print("left bump:", left_bump)
                print("right bump:", right_bump)

finally:
    robot.stop()  # Ensure the robot stops in case of an exception
    client_socket.close()
