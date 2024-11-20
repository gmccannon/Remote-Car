"""
Camera.py

Description:
This script tests the image capture using the Raspberry Pi Camera and saves it to a file. 

Features:
- Initializes the Picamera2 instance.
- Captures an image and saves it to the specified filename.

Usage:
1. Ensure the Raspberry Pi Camera is properly connected to the Raspberry Pi.
2. Install the Picamera2 library.
3. Run the script to capture an image and save it as `image.jpg`.

Dependencies:
- Picamera2 library

Usage:
    1. Instantiate the `Camera` class: 
      `picam2 = Picamera2()`
    2. Take a photo and save it 
      picam2.start_and_capture_file("image.jpg")

Output:
- The captured image is saved as `image.jpg` in the current directory.
"""

from picamera2 import Picamera2

picam2 = Picamera2()

picam2.start_and_capture_file("image.jpg")
