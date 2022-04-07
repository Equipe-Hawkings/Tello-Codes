''' Código utilizado para iniciar a stream da camêra do tello.
Objetiva-se por meio do código, evitar erros devido ao atraso do ínicio da stream
que pode causar problemas durante o primeiro voo de um sistema
    Portanto, antes de voar com o Tello pela primeira vez após ligar o computador,
executa-se este código'''

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