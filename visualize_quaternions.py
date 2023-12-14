from vpython import *
from time import *
import numpy as np
import math
from reader2 import run_data

scene.range = 5
scene.background = color.black
toRad = 2 * np.pi / 360
toDeg = 1 / toRad
scene.forward = vector(-1, -1, -1)

scene.width = 1200
scene.height = 1080

xarrow = arrow(length=2, shaftwidth=.1, color=color.red, axis=vector(1, 0, 0))
yarrow = arrow(length=2, shaftwidth=.1, color=color.green, axis=vector(0, 1, 0))
zarrow = arrow(length=4, shaftwidth=.1, color=color.blue, axis=vector(0, 0, 1))

frontArrow = arrow(length=4, shaftwidth=.1, color=color.purple, axis=vector(1, 0, 0))
upArrow = arrow(length=1, shaftwidth=.1, color=color.magenta, axis=vector(0, 1, 0))
sideArrow = arrow(length=2, shaftwidth=.1, color=color.orange, axis=vector(0, 0, 1))

bBoard = box(length=6, width=2, height=.2, opacity=.8, pos=vector(0, 0, 0,))
myObj = compound([bBoard])

run_data_list = run_data()

while 1:
    for run_data in run_data_list:
        try:
            q0 = float(run_data.quaternion_w)
            q1 = float(run_data.quaternion_x)
            q2 = float(run_data.quaternion_y)
            q3 = float(run_data.quaternion_z)

            roll = math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2))
            pitch = math.asin(2 * (q0 * q2 - q3 * q1))
            yaw = math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)) - np.pi / 2

            k = vector(cos(yaw) * cos(pitch), sin(pitch), sin(yaw) * cos(pitch))
            y = vector(0, 1, 0)
            s = cross(k, y)
            v = cross(s, k)
            vrot = v * cos(roll) + cross(k, v) * sin(roll)

            frontArrow.axis = k
            sideArrow.axis = cross(k, vrot)
            upArrow.axis = vrot
            myObj.axis = k
            myObj.up = vrot
            sideArrow.length = 2
            frontArrow.length = 4
            upArrow.length = 1

            rate(1 / 0.01)

        except Exception as e:
            print(f"Error processing data: {e}")

