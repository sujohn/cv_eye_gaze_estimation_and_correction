import numpy as np
from utils import normalize

def compute_gaze(le, li, re, ri):
    g_left = normalize(li - le)
    g_right = normalize(ri - re)
    return normalize((g_left + g_right) / 2)
