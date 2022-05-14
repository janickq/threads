import subprocess
import cv2
from time import sleep


class cam2:
    
    @staticmethod
    def capture():
        cmd = "raspistill -q 100 -o testimg.jpg"
        subprocess.call(cmd, shell=True)
        return cv2.imread("testimg.jpg")