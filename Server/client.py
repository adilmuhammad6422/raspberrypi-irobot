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


import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
        )
        sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.recv_total += len(recv_data)
            print(f"Received {recv_data.decode('utf-8')} from connection {data.connid}")
            if recv_data.decode('utf-8') == 'straight':
                print("Roomba going straight.")
                sock.sendall(b'straight')
            elif recv_data.decode('utf-8') == 'left':
                print("Roomba going left.")
                sock.sendall(b'left')
            elif recv_data.decode('utf-8') == 'right':
                print("Roomba going right.")
                sock.sendall(b'right')
            elif recv_data.decode('utf-8') == 'quit':
                print("Quitting.")
                sock.sendall(b'quit')
                sel.unregister(sock)
                sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {data.outb.decode('utf-8')} to connection {data.connid}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

HOST = "192.168.1.100"
PORT = 44700

start_connections(HOST, PORT, 1)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
 