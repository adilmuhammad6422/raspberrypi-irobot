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
        command_parts = response.split()
        command = command_parts[0]
        duration = None
        if len(command_parts) > 1:
            try:
               duration = int(command_parts[1])
            except ValueError:
                print("space error")
                continue
        if response:
            if command == 'straight':
                print("Roomba going straight.")
                robot.set_velocity(200)
                robot.drive_straight(duration)  # Drive straight for 2 seconds as an example
                client_socket.sendall(b'straight')
            elif command == 'left':
                print("Roomba going left.")
                robot.set_velocity(200)
                robot.stop()
                robot.turn_dynamic_angle(90)  # Turn left by 90 degrees as an example
                robot.stop()
                client_socket.sendall(b'left')
            elif command == 'right':
                print("Roomba going right.")
                robot.set_velocity(200)
                robot.stop()
                robot.turn_dynamic_angle(-90)  # Turn right by 90 degrees as an example
                robot.stop()
                client_socket.sendall(b'right')
            elif command == 'stop':
                print("Stopping..")
                robot.stop()  # Stop the robot
                client_socket.sendall(b'stop')
            elif command == 'quit':
                print("Quitting.")
                robot.stop()  # Ensure the robot stops before quitting
                client_socket.sendall(b'quit')
                client_socket.close()
                break

finally:
    robot.stop()  # Ensure the robot stops in case of an exception
    client_socket.close()
