#import socket

#HOST = "0.0.0.0"  # Listen on all available interfaces
#PORT = 44700  # Port to listen on (non-privileged ports are > 1023)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) #as s:
    #s.bind((HOST, PORT))
    #s.listen()
    #print(f"Server is listening on {HOST}:{PORT}...")
    #conn, addr = s.accept()
    #with conn:
        #print(f"Connected by {addr}")
        #while True:
            #msg_to_send = input("send a message:")
            #conn.sendall(str.encode(msg_to_send))
            #msg_received = conn.recv(1024).decode('utf-8')
            #if msg_received == 'quit':
                #break

import socket
import selectors
import types

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 44700  # Port to listen on (non-privileged ports are > 1023)

sel = selectors.DefaultSelector()
connections = {}

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("Accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    connections[conn] = data

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.inb += recv_data
            print("Received", recv_data.decode('utf-8'), "from", data.addr)
            if recv_data.decode('utf-8').strip() == 'quit':
                sel.unregister(sock)
                sock.close()
                print("Closed connection to", data.addr)
                del connections[sock]
        else:
            print("Closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
            del connections[sock]
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("Sending", data.outb.decode('utf-8'), "to", data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

# Set up the listening socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print("Server is listening on", HOST, ":", PORT)
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
        
        if connections:
            print("\nActive connections:")
            for i, conn in enumerate(connections.keys()):
                print(i, ":", connections[conn].addr)

            try:
                option = input("Enter 'all' to broadcast a message to all connections or the connection number to send a message to a specific connection: ").strip()
                if option.lower() == 'all':
                    msg_to_send = input("Send a message to all connections: ")
                    for conn in connections.keys():
                        connections[conn].outb = msg_to_send.encode('utf-8')
                else:
                    conn_index = int(option)
                    conn = list(connections.keys())[conn_index]
                    msg_to_send = input("Send a message: ")
                    connections[conn].outb = msg_to_send.encode('utf-8')
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()


