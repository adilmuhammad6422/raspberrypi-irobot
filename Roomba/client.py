import socket
from roomba_dyna import Robot

HOST = "192.168.1.102"  # Change this to your computer IP address
PORT = 44700  # Port to connect to

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

robot = Robot()  # Create an instance of Robot
robot.start()  # Start the robot

try:
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        if response:
            if response == 'straight':
                print("Roomba going straight.")
                robot.set_velocity(200)
                robot.drive_straight(2)  # Drive straight for 2 seconds as an example
                client_socket.sendall(b'straight')
            elif response == 'left':
                print("Roomba going left.")
                robot.set_velocity(200)
                robot.turn_dynamic_angle(-90)  # Turn left by 90 degrees as an example
                client_socket.sendall(b'left')
            elif response == 'right':
                print("Roomba going right.")
                robot.set_velocity(200)
                robot.turn_dynamic_angle(90)  # Turn right by 90 degrees as an example
                client_socket.sendall(b'right')
            elif response == 'stop':
                print("Stopping..")
                robot.stop()  # Stop the robot
                client_socket.sendall(b'stop')
                client_socket.shutdown(socket.SHUT_RDWR)  # Stop both sending and receiving data using SHUT_RDWR
            elif response == 'quit':
                print("Quitting.")
                robot.stop()  # Ensure the robot stops before quitting
                client_socket.sendall(b'quit')
                client_socket.close()
                break

finally:
    robot.stop()  # Ensure the robot stops in case of an exception
    client_socket.close()
