import socket

HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 44700  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            msg_to_send = input("send a message:")
            conn.sendall(str.encode(msg_to_send))
            msg_received = conn.recv(1024).decode('utf-8')
            if msg_received == 'quit':
                break
