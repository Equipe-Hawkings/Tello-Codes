import cv2
from djitellopy import Tello


tello = Tello()
tello.connect(False)
tello.streamon()
imagem = tello.get_frame_read()
while(1):
    cv2.imshow("Image", imagem.frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
	    break