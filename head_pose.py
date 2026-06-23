import cv2
import numpy as np
from config import POSE_POINTS

def get_head_pose(landmarks, w, h):
    img_pts = np.array([[landmarks[i].x*w, landmarks[i].y*h] for i in POSE_POINTS],
                       dtype=np.float64)

    model = np.array([
        (-30,30,30),(30,30,30),(0,0,0),
        (-40,-30,30),(40,-30,30),(0,-60,30)
    ], dtype=np.float64)

    cam = np.array([[w,0,w/2],[0,w,h/2],[0,0,1]])
    dist = np.zeros((4,1))

    _, rvec, _ = cv2.solvePnP(model, img_pts, cam, dist)
    R,_ = cv2.Rodrigues(rvec)
    return R

def correct_gaze(gaze, R):
    return R @ gaze
