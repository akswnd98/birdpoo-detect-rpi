import time
import cv2
import numpy as np
import ultralytics
from picamera2 import Picamera2

if __name__ == '__main__':
    picam = Picamera2()
    picam_config = picam.create_still_configuration(main={'size': (1920, 1080), 'format': 'RGB888'})
    picam.configure(picam_config)
    picam.start()
    time.sleep(0.1)
    model = ultralytics.YOLO('./best.pt')
    model.to('cpu')
    array = picam.capture_array('main')
    results = model(array)
    for i, result in enumerate(results):
        result.save(f'result{i}.jpg')
    print(array.shape)
