import socket
import selectors
import types

MESSAGE_ALL = True

HOST = "0.0.0.0"
PORT = 44700

sel = selectors.DefaultSelector()
connections = {}

def print_active_connections():
    if connections:
        print("\nActive connections:")
        for i, conn in enumerate(connections.keys()):
            print(i, ":", connections[conn].addr)
    else:
        print("No active connections.")

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print("Accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
    connections[conn] = data
    print_active_connections()

def close_connection(sock):
    """
    Safely closes and removes a socket from the selector and the connections dictionary.
    """
    addr = connections[sock].addr if sock in connections else "Unknown"
    try:
        if sock.fileno() != -1:
            try:
                sel.unregister(sock)
            except Exception as e:
                print(f"Error unregistering socket for {addr}: {e}")
            try:
                sock.close()
            except Exception as e:
                print(f"Error closing socket for {addr}: {e}")
    except Exception as e:
        print(f"Failed to close socket properly: {e}")
    if sock in connections:
        del connections[sock]
    print(f"Closed connection to {addr}")
    print_active_connections()

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    try:
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.inb += recv_data
                print("Received", recv_data.decode('utf-8'), "from", data.addr)
                if recv_data.decode('utf-8').strip() == 'quit':
                    raise ConnectionResetError("Client sent 'quit' command")
            else:
                raise ConnectionResetError("Client disconnected")

        if mask & selectors.EVENT_WRITE and data.outb:
            print("Sending", data.outb.decode('utf-8'), "to", data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

    except (ConnectionResetError, BrokenPipeError, OSError, ValueError) as e:
        print(f"Error with {data.addr}: {e}")
        close_connection(sock)

def main():
    lsock = socket.socket()
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

            # option = input("Enter 'all' to broadcast or index to send to one: ").strip()
            try:
                if MESSAGE_ALL:
                    msg_to_send = input("Message: ")
                    for conn in list(connections):
                        connections[conn].outb = msg_to_send.encode('utf-8')
                    print_active_connections()
                else:
                    option = input("Enter index to send of Pi: ").strip()
                    conn_index = int(option)
                    conn = list(connections.keys())[conn_index]
                    msg_to_send = input("Message: ")
                    connections[conn].outb = msg_to_send.encode('utf-8')
                    print_active_connections()
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()

if __name__ == "__main__":
    main()
