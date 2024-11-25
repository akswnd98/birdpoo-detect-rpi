import cv2
import numpy as np
import ultralytics
from picamera2 import Picamera2

X_CAM_RES = 1920
Y_CAM_RES = 1080
X_SCALE = 15000.0
Y_SCALE = 15000.0

def init_picam (picam):
    picam_config = picam.create_still_configuration(main={'size': (1920, 1080), 'format': 'RGB888'})
    picam.configure(picam_config)
    picam.start()

def capture (picam):
    return picam.capture_array('main')

def get_birdpoo_center_pos (model, frame):
    results = model(frame)
    results[0].save()
    first_result = results[0].boxes.data.numpy()
    center_poses = (first_result[:, 0: 2] + first_result[:, 2: 4]) / 2
    center_poses[: 0] -= X_CAM_RES / 2
    center_poses[: 1] -= Y_CAM_RES / 2
    center_poses[:, 0] = center_poses[:, 0] / 1080 * Y_SCALE
    center_poses[:, 1] = center_poses[:, 1] / 1080 * X_SCALE
    return center_poses


