import socket

HOST = "192.168.1.102"  # Change this to your IP address
PORT = 44700  # Port to connect to

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        response = client_socket.recv(1024).decode('utf-8')
        if response:
            if response == 'straight':
                print("Roomba going straight.")
                client_socket.sendall(b'straight')
            elif response == 'left':
                print("Roomba going left.")
                client_socket.sendall(b'left')
            elif response == 'right':
                print("Roomba going right.")
                client_socket.sendall(b'right')
            elif response == 'quit':
                print("Stopping..")
                client_socket.sendall(b'stop')
                client_socket.shutdown(socket.SHUT_RDWR) # Stop both sending and receiving data using SHUT_RDWR
            elif response == 'quit':
                print("Quitting.")
                client_socket.sendall(b'quit')
                client_socket.close()
                break

finally:
    client_socket.close()

 