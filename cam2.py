import subprocess
import cv2
from time import sleep


class cam2:
    
    @staticmethod
    def capture():
        cmd = "raspistill -q 100 -w 3000 -h 3000 -o testimg.jpg"
        subprocess.call(cmd, shell=True)
        img = cv2.imread("testimg.jpg")
        return cv2.resize(img, (1200,1200))