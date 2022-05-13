from cam import cam
import cv2
from time import sleep

pictaker = cam((2000,2000))

for i in range(5):
    img = pictaker.read()
    cv2.imwrite("imgs/image"+i+".jpg", img)
    sleep(2)
    