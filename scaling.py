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
    ser = serial.Serial('/dev/ttyACM0', 115200)
    model = ultralytics.YOLO('./birdpoo-n.pt')
    time.sleep(1)
    model.to('cpu')

    start_time = time.time()
    frame = utils.capture(picam)
    cv2.imwrite('raw_image.png', frame)
    
    results = utils.get_birdpoo_center_pos(model, frame)

    end_time = time.time()

    print(f'results: {results[0]}')
    print(f'time consumption: {end_time - start_time}')

    ser.write(f'{results[0][1]},{results[0][0]}\n'.encode())
    ser.close()
    
