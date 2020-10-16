#!/usr/bin/env python

import numpy as np
"""
Funcion que convierte de matriz homografica a pose
"""

def homography_to_pose(H,fx,fy,cx,cy):

    R20 = H[2,0]
    R21 = H[2,1]
    Tz = H[2,2]
    R00 = (H[0,0] - cx*R20)/fx
    R01 = (H[0,1] - cx*R21)/fx
    Tx = (H[0,2] - cx*Tz)/fx
    R10 = (H[1,0] - cy*R20)/fy
    R11 = (H[1,1] - cy*R21)/fy
    Ty = (H[1,2] - cy*Tz)/fy

    length1 = np.sqrt(R00*R00 + R10*R10 + R20*R20)
    length2 = np.sqrt(R01*R01 + R11*R11 + R21*R21)
    s = 1.0 / np.sqrt(length1 * length2)

    if (Tz > 0):
        s *= -1

    R20 *= s
    R21 *= s
    Tz  *= s
    R00 *= s
    R01 *= s
    Tx  *= s
    R10 *= s
    R11 *= s
    Ty  *= s

    R02 = R10*R21 - R20*R11
    R12 = R20*R01 - R00*R21
    R22 = R00*R11 - R10*R01

    return np.array([[R00, R01, R02, Tx],
                     [R10, R11, R12, Ty],
                     [R20, R21, R22, Tz],
                     [0, 0, 0, 1]
                     ])

H = np.random.rand(3,3)
fx = 220.2460
fy = 238.67758
cx = 0
cy = 0

pose = homography_to_pose(H, fx, fy, cx, cy)

print(H)
print(pose)
