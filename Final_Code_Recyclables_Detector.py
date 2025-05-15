import cv2 
import os 
import time 
import threading 
import tensorflow as tf 
import keras.utils as ku 
import numpy as np 
import serial
import time
 
def folder_is_empty(folder_path): 
    return len(os.listdir(folder_path)) == 0 
 
 
def predict_image(image):  #use (image, ser) for INTEGRATION WITH ARUINO / ESP 32
    model = tf.keras.models.load_model("Trained Models/model_saved.h5") 
    labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'} 
 
    img = ku.load_img(image, target_size=(300, 300)) 
    img = ku.img_to_array(img, dtype=np.uint8) 
    img = np.array(img) / 255.0 
    prediction = model.predict(img[np.newaxis, ...]) 
 
    print("Probability:", np.max(prediction[0], axis=-1)) 
    predicted_class = labels[np.argmax(prediction[0], axis=-1)] 
    print("Classified:", predicted_class, '\n') 
    ser.write((predicted_class).encode())
 
 
def display(video_capture): 
    """ 
    Thread function to display the video feed. 
    """ 
    while True: 
        ret, frame = video_capture.read() 
        if ret: 
            cv2.imshow("frame1", frame) 
        # Break on user pressing 'q' 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            video_capture.release() 
            cv2.destroyAllWindows() 
            break 
        time.sleep(0.01)  # Small sleep to prevent excessive CPU usage 
 
 
def capture_images(video_capture, output_folder, interval_seconds, max_images, port, baud_rate): 
    ###
    #UNCOMMENT FOR INTEGRATION WITH ARDUINO /ESP 32
    # ser = serial.Serial(port=port, baudrate=baud_rate,timeout=1) 
    # print(f"Connected to {PORT} at {BAUD_RATE} baud.")
    ###

    time.sleep(2)

    # Wait for the ESP32 to initialize
    """ 
    Thread function to capture images from a webcam. 
    """ 
    os.makedirs(output_folder, exist_ok=True) 
    print("Starting image capture. Press 'q' to quit.") 
 
    image_count = 0 
    start_time = time.time()
 
    while image_count < max_images: 
      #  response = ser.readline().decode().strip()  # Read response from ESP32 Uncomment for integration with Arduino / ESP 32
        if response:
            print(f"ESP32 says: {response}")

        if time.time() - start_time >= interval_seconds: 
            ret, frame = video_capture.read() 
            if ret: 
                image_path = os.path.join(output_folder, f"image_{image_count:03d}.jpg") 
                cv2.imwrite(image_path, frame) 
                print(f"Saved: {image_path}") 
 
                # Run prediction in a separate thread to prevent blocking 
                threading.Thread(target=predict_image, args=(image_path,ser)).start() 
 
                image_count += 1 
                start_time = time.time() 
        # Break on user pressing 'q' 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
        time.sleep(0.01)  # Small sleep to prevent excessive CPU usage 

###
#UNCOMMENT FOR INTEGRATION WITH ARDUINO / ESP32
# Update these variables based on your setup
# PORT = "COM5"  # Replace with the port your ESP32 is connected to (e.g., "COM3" on Windows, "/dev/ttyUSB0" on Linux)
# BAUD_RATE = 115200  # Match the baud rate set in your ESP32 code
###

# Main script 
if __name__ == "__main__": 

    # Parameters 
    output_folder = "Collection" 
    interval_seconds = 5 
    max_images = 30
 
    # Initialize VideoCapture objects 
    video_capture1 = cv2.VideoCapture(0)  #Set to 1, 2 or 3 for external cameras. Uses default integrated camera
    video_capture2 = cv2.VideoCapture(0) 
 
    # Create threads 
    display_thread = threading.Thread(target=display, args=(video_capture1,)) 
    capture_thread = threading.Thread(target=capture_images, args=(video_capture1, output_folder, interval_seconds, max_images, PORT, BAUD_RATE)) 
 
    # Start threads 
    display_thread.start() 
    capture_thread.start() 
 
    # Wait for threads to finish 
    display_thread.join() 
    capture_thread.join()