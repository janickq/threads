#!/usr/bin/env python
# coding: utf-8
"""
Object Detection (On Pi Camera) From TF2 Saved Model
=====================================
"""
from inspect import FrameInfo
from time import sleep
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
# import pathlib
import tensorflow as tf
import cv2
import argparse
from threading import Thread
from WOB import WOB
# from cam2 import cam2
from cam import cam
# from detector import detector
# from comms import comms
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

# comm = comms
# src = cv2.imread("test_img/testimg1.jpg")

stream = cam(resolution=(640,480),framerate=30).start()

# detection = detector.detect
# frame = stream.read()
# cv2.namedWindow("test")
print('Running inference for PiCamera')
img_counter = 0
# cap = cam2
while True:
  # cap.capture
  # ret, frame = stream.read()
  # if not ret:
  #     print("failed to grab frame")
  #     break
  # cv2.imshow("test", frame)
  frame = stream.read()
  cv2.imshow("frame",frame)
  # print(stream.read())
  cv2.waitKey(1)


    # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
  frame = stream.read()
  frame = WOB.process_image(frame)
  # comm.writeStr('info', 'test')
  
  # print(comms.read_command)
  # image, item, count = detection(frame)
    
  # if count <= 12:
  #   image = cv2.resize(image,(600,600))
  #   cv2.imshow('Object Counter', image)
  #   print('no board found')
  #   comms.writeStr('info', 'no board found')
  # else:
  #   # image, max_area = getWOB(frame)
  #   image, max_area = WOB.getWOB(frame)
  #   cv2.imshow('result', cv2.resize(image,(600,600)))
  #   deliver, ret = WOB.sort_grid(image,item)
  #   image = cv2.resize(image,(600,600))
  #   # cv2.putText (image,'Total Detections : ' + str(count),(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(70,235,52),2,cv2.LINE_AA)
  #   cv2.imshow('Object Counter', image)
  #   print("max area:", max_area)
    
  #   comms.writeStrArray("Deliver", str(deliver))
  #   comms.writeStrArray("Return", str(ret))
  #   comms.writeStr('max area:', max_area)

  # if cv2.waitKey(1) == ord('q'):
  #     break

cv2.destroyAllWindows()
print("Done")
