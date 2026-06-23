import cv2
import math
import random

def draw_arrow(frame, pos, gaze):
    x,y = int(pos[0]), int(pos[1])
    end = (int(x+gaze[0]*120), int(y+gaze[1]*120))
    cv2.arrowedLine(frame,(x,y),end,(0,255,0),2)

def draw_hud(frame, gaze):
    yaw = math.degrees(math.atan2(gaze[0], gaze[2]))
    pitch = math.degrees(math.atan2(gaze[1], gaze[2]))

    cv2.putText(frame,f"Yaw: {yaw:.1f}",(20,40),0,0.7,(0,255,255),2)
    cv2.putText(frame,f"Pitch: {pitch:.1f}",(20,70),0,0.7,(0,255,255),2)

def mask_eye(frame, landmarks, indices, w, h):
    pts = []
    for i in indices:
        lm = landmarks[i]
        pts.append([int(lm.x*w), int(lm.y*h)])

    pts = np.array(pts)
    mask = np.zeros(frame.shape[:2], np.uint8)
    cv2.fillPoly(mask,[pts],255)

    blur = cv2.GaussianBlur(frame,(25,25),0)
    frame[mask==255] = blur[mask==255]

def random_color():
    import random
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
