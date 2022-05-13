from cam import cam
import cv2
from time import sleep

pictaker = cam((1200,1200))
sleep(5)
for i in range(5):
    img = pictaker.read()
    cv2.imwrite("imgs/image"+str(i)+".jpg", img)
    sleep(2)
    