#import socket

#HOST = "192.168.1.100"
#PORT = 44700
#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect((HOST,PORT))
#while True:
    #response = client_socket.recv(1024).decode('utf-8')
    #if response == 'straignt':
        #print("Roomba going Straight.")
        #client_socket.sendall(str.encode('straight'))
    #if response == 'left':
        #print("Roomba going left.")
        #client_socket.sendall(str.encode('left'))
    #if response == 'right':
        #print("Roomba going right.")
        #client_socket.sendall(str.encode('right'))
    #if response == 'quit':
        #print("Quitting.")
        #client_socket.sendall(str.encode('quit'))
        #client_socket.close()
        #break


import socket

HOST = "192.168.1.100"  # Change this to your server's IP address
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
                print("Quitting.")
                client_socket.sendall(b'quit')
                client_socket.close()
                break
finally:
    client_socket.close()

 