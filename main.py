from multiprocessing.connection import wait
from threading import Thread
from comms import comms
from time import sleep
from commands import commands
from detector2 import detector2
from cam import cam
import cv2

stream = cam()
detector = detector2("models/model.tflite", "models/labels.txt")
comm = comms()
cmd = commands()
m_flag = False

#master thread
def master(args):
    global m_flag
    while True:
        if comm.notified[0]:
            if cmd.CommandID == comm.read_string("CommandID"):
                m_flag = True
            else:
                m_flag = False
            sleep(1)
        else:
            print('waiting for connection...')
            sleep(5)


def command_thread(args):#commands
    pass


def comms_thread(args):
    global m_flag
    while True:
        if m_flag:
            print("comm_thread active")
            sleep(1)
    
def detector_thread(args):
    global m_flag
    while True:
        if m_flag:
            img = stream.read()
            # cv2.imshow('img', img)
            # cv2.waitKey(1)
            detected = detector.run(img)
            print("detector running")
            cv2.imshow("detector", detected)
            cv2.waitKey(1)
            sleep(1)
            
        else:
            print("cam offline")
            sleep(1)
    



if __name__ == "__main__":

    #create threads
    masterthread = Thread(target = master, args = (10, ))
    commsthread = Thread(target = comms_thread, args = (10, ))
    cmdthread = Thread(target = command_thread, args = (10, ))
    detectorthread = Thread(target = detector_thread, args = (10, ))

    #start threads
    masterthread.start()
    detectorthread.start()
    commsthread.start()
    print("thread started")

    #end threads
    masterthread.join()
    camthread.join()
    commsthread.join()
    
    
    