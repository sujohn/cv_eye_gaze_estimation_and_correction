import cv2
import numpy as np

def init_kalman():
    kf = cv2.KalmanFilter(6,3)

    kf.transitionMatrix = np.array([
        [1,0,0,1,0,0],
        [0,1,0,0,1,0],
        [0,0,1,0,0,1],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1]
    ], np.float32)

    kf.measurementMatrix = np.array([
        [1,0,0,0,0,0],
        [0,1,0,0,1,0],
        [0,0,1,0,0,0]
    ], np.float32)

    kf.processNoiseCov = np.eye(6, dtype=np.float32)*0.01
    kf.measurementNoiseCov = np.eye(3, dtype=np.float32)*0.1

    return kf

def adaptive_kalman(kf, gaze):
    measured = np.array([[gaze[0]],[gaze[1]],[gaze[2]]], np.float32)

    pred = kf.predict()
    innovation = measured - (kf.measurementMatrix @ pred)
    error = np.linalg.norm(innovation)

    if error < 0.05:
        kf.processNoiseCov *= 0.8
    elif error > 0.15:
        kf.processNoiseCov *= 1.2

    est = kf.correct(measured)
    return est[:3].flatten()
