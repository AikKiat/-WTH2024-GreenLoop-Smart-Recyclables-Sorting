import serial
import time

# Replace 'COM3' with your Arduino's serial port (e.g., '/dev/ttyUSB0' for Linux/macOS)
arduino = serial.Serial(port='COM8', baudrate=115200, timeout=1)

time.sleep(2)  # Give the connection time to establish

def send_data(data):
    arduino.write(f"{data}\n".encode())  # Send data as bytes
    time.sleep(0.1)
    response = arduino.readline().decode().strip()  # Read the Arduino's response
    return response

print(send_data("Hello, Arduino!"))
