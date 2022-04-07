#!/usr/bin/env python3

import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from djitellopy import Tello
import cv2.aruco as aruco
import time
import numpy as np


# define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}


def bateria():
	print("Nível da bateria do Michel:")
	print(tello.get_state_field('bat'))




tello = Tello()
tello.connect(False)
tello.streamon()
imagem = tello.get_frame_read()
tello.takeoff()
time.sleep(2)
tello.move_up(50)

while(1):

	bateria()
	aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
	arucoParams = cv2.aruco.DetectorParameters_create()
	(corners, ids, rejected) = cv2.aruco.detectMarkers(imagem.frame, aruco_dict,parameters=arucoParams)
	aruco.drawDetectedMarkers(imagem.frame, corners, ids)
	cv2.imshow("Image", imagem.frame)
	key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	if (ids == 24):
		tello.flip_back()

	elif (ids == 0):
		tello.rotate_counter_clockwise(360)
    
	elif (ids == 1):
		tello.land()
	
	elif (ids == 2):
		tello.curve_xyz_speed(70, 70, 0, 140, 0, 0, 50)
		time.sleep(1)
		tello.curve_xyz_speed(-70, -70, 0, -140, 0, 0, 50)
