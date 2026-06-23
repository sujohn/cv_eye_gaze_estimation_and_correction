import numpy as np

def get_pts(landmarks, indices, w, h):
    return np.array([[landmarks[i].x*w, landmarks[i].y*h, landmarks[i].z] for i in indices])

def center(pts):
    return np.mean(pts, axis=0)

def to_3D(p, w, h):
    return np.array([(p[0]-w/2)/w, (p[1]-h/2)/h, p[2]])

def normalize(v):
    n = np.linalg.norm(v)
    return v/n if n != 0 else v
