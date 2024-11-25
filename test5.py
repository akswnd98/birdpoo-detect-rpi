import time
import cv2
import numpy as np
import ultralytics
from picamera2 import Picamera2
import utils
import struct
import serial

if __name__ == '__main__':
    picam = Picamera2()
    utils.init_picam(picam)

    frame = utils.capture(picam)
    cv2.imwrite('raw_image.png', frame)
    print(frame.shape)
    
