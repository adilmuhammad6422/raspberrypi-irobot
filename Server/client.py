import socket

HOST = "192.168.1.100"
PORT = 44700
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
while True:
    response = client_socket.recv(1024).decode('utf-8')
    if response == 'straignt':
        print("Roomba going Straight.")
        client_socket.sendall(str.encode('straight'))
    if response == 'left':
        print("Roomba going left.")
        client_socket.sendall(str.encode('left'))
    if response == 'right':
        print("Roomba going right.")
        client_socket.sendall(str.encode('right'))
    if response == 'quit':
        print("Quitting.")
        client_socket.sendall(str.encode('quit'))
        client_socket.close()
        break
    