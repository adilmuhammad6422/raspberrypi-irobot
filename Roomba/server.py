import socket
import selectors
import types

# Define the host and port for the server
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 44700  # Port to listen on (non-privileged ports are > 1023)

# Create a default selector object to handle multiple connections
sel = selectors.DefaultSelector()

# Dictionary to keep track of active connections
connections = {}

def print_active_connections():
    """
    Prints the list of active connections.
    """
    if connections:
        print("\nActive connections:")
        for i, conn in enumerate(connections.keys()):
            print(i, ":", connections[conn].addr)
    else:
        print("No active connections.")

def accept_wrapper(sock):
    """
    Accepts a new connection from the client.
    """
    conn, addr = sock.accept()  # Accept the connection
    print("Accepted connection from", addr)
    conn.setblocking(False)  # Set the connection to non-blocking mode
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")  # Initialize connection data
    events = selectors.EVENT_READ | selectors.EVENT_WRITE  # Set the events to monitor
    sel.register(conn, events, data=data)  # Register the connection with the selector
    connections[conn] = data  # Add connection to the dictionary
    print_active_connections()  # Print the updated list of active connections

def service_connection(key, mask):
    """
    Handles servicing of a connection, both reading from and writing to the socket.
    """
    sock = key.fileobj  # Get the socket object
    data = key.data  # Get the connection data
    try:
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Read data from the socket
            if recv_data:
                data.inb += recv_data  # Append received data to inb buffer
                print("Received", recv_data.decode('utf-8'), "from", data.addr)
                if recv_data.decode('utf-8').strip() == 'quit':
                    raise ConnectionResetError("Client sent 'quit' command")

        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print("Sending", data.outb.decode('utf-8'), "to", data.addr)
                sent = sock.send(data.outb)  # Send data from outb buffer to the socket
                data.outb = data.outb[sent:]  # Remove sent data from outb buffer

    except (ConnectionResetError, BrokenPipeError) as e:
        print(f"Closing connection to {data.addr}: {e}")
        sel.unregister(sock)
        sock.close()
        if sock in connections:
            del connections[sock]
        print_active_connections()

# Set up the listening socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))  # Bind the socket to the host and port
lsock.listen()  # Listen for incoming connections
print("Server is listening on", HOST, ":", PORT)
lsock.setblocking(False)  # Set the socket to non-blocking mode
sel.register(lsock, selectors.EVENT_READ, data=None)  # Register the listening socket with the selector

try:
    while True:
        events = sel.select(timeout=None)  # Wait for events
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)  # Accept new connection
            else:
                service_connection(key, mask)  # Service existing connection

        option = input("Enter 'all' to broadcast a message to all connections or the connection number to send a message to a specific connection: ").strip()
        try:
            if option.lower() == 'all':
                msg_to_send = input("Send a message to all connections: ")
                for conn in connections.keys():
                    connections[conn].outb = msg_to_send.encode('utf-8')  # Broadcast message to all connections
                print_active_connections()  # Print active connections after sending the message
            else:
                conn_index = int(option)
                conn = list(connections.keys())[conn_index]
                msg_to_send = input("Send a message: ")
                connections[conn].outb = msg_to_send.encode('utf-8')  # Send message to a specific connection
                print_active_connections()  # Print active connections after sending the message
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()  # Close the selector
