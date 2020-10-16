#!/usr/bin/env python

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
    R10 = (H[1,1] - cy*R21)/fy
    Ty = (H[1,2] - cy*Tz)/fy
