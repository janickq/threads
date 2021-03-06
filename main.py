#imports
from multiprocessing.connection import wait
from threading import Thread
from comms import comms
from time import sleep
from command import command
from detector2 import detector2
# from cam import cam
from WOB import WOB
import cv2
from cam2 import cam2
from cam import cam

#initialize objects
stream = cam((1200,1200))
detector = detector2("models/model320.tflite", "models/labels.txt")
comm = comms()
cmd = command()
m_flag = False


#misc functions
def cmd_sync(args):
    pass


def get_workorder(args):
    pass


#program threads
def master(args):
    global m_flag
    while True:
        print(comm.read_string("CommandID"))
        if comm.notified[0]:
            if cmd.CommandID >= comm.read_string("CommandID"):
                m_flag = True
            else:
                m_flag = False
            sleep(1)
        else:
            print('waiting for connection...')
            sleep(1)


def command_thread(args):#commands
    pass


def comms_thread(args):
    global m_flag
    while True:
        if m_flag:
            print("comm_thread active")
            sleep(1)

    
def detector_thread(args):
    global deliver, ret
    global m_flag
    while True:
        if m_flag:
            # img = cam2.capture()
            # img = cv2.imread("imgs/image4 (2).jpg")
            img = stream.read()
            # img = cv2.resize(img,(640,480))
            # cv2.imshow("stream", img)
            result, max_area = WOB.getWOB(img)
            # cv2.imshow('img', img)
            # cv2.waitKey(1)
            detected, items, count = detector.run(result)
            print("detector running")
            deliver, ret = WOB.sort_grid(detected, items)

            cv2.imshow("detector", detected)
            cv2.waitKey(1)
            
        else:
            print("cam offline")
            sleep(1)
            
            
# def cam(args):
#     while True:
        
#         print(img.shape)
#         cv2.imshow("raspistill capture", cv2.resize(img, (640,480)))
#         cv2.waitKey(1)
#         # sleep(1)
    



if __name__ == "__main__":

    #create threads
    masterthread = Thread(target = master, args = (10, ))
    commsthread = Thread(target = comms_thread, args = (10, ))
    cmdthread = Thread(target = command_thread, args = (10, ))
    detectorthread = Thread(target = detector_thread, args = (10, ))
    # camthread = Thread(target = cam, args = (10, ))
    
    #start threads
    masterthread.start()
    # detectorthread.start()
    commsthread.start()
    # camthread.start()
    print("thread started")

    #end threads
    masterthread.join()
    # camthread.join()
    commsthread.join()
    
    
    