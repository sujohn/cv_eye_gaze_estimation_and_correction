import cv2
import mediapipe as mp
import numpy as np

from config import *
from utils import *
from gaze_estimation import *
from head_pose import *
from kalman_filter import *
from visualization import *

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

kf = init_kalman()
iris_color = (0,255,0)

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame,1)
    raw = frame.copy()

    h,w,_ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face_mesh.process(rgb)

    if res.multi_face_landmarks:
        lm = res.multi_face_landmarks[0].landmark

        li = center(get_pts(lm, LEFT_IRIS,w,h))
        ri = center(get_pts(lm, RIGHT_IRIS,w,h))
        le = center(get_pts(lm, LEFT_EYE,w,h))
        re = center(get_pts(lm, RIGHT_EYE,w,h))

        li,ri,le,re = to_3D(li,w,h),to_3D(ri,w,h),to_3D(le,w,h),to_3D(re,w,h)

        gaze = compute_gaze(le,li,re,ri)

        # HEAD POSE CORRECTION
        R = get_head_pose(lm,w,h)
        gaze = correct_gaze(gaze,R)

        # ADAPTIVE KALMAN
        gaze = adaptive_kalman(kf,gaze)
        gaze = normalize(gaze)

        # VISUALS
        draw_hud(frame,gaze)
        draw_arrow(frame,le,gaze)
        draw_arrow(frame,re,gaze)

        mask_eye(frame,lm,LEFT_EYE,w,h)
        mask_eye(frame,lm,RIGHT_EYE,w,h)

        for p in get_pts(lm, LEFT_IRIS,w,h):
            cv2.circle(frame,(int(p[0]),int(p[1])),2,iris_color,-1)

        for p in get_pts(lm, RIGHT_IRIS,w,h):
            cv2.circle(frame,(int(p[0]),int(p[1])),2,iris_color,-1)

    combined = np.hstack((raw, frame))
    cv2.imshow("Original | Processed", combined)

    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord('c'):
        iris_color = random_color()

cap.release()
cv2.destroyAllWindows()
