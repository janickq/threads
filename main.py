from multiprocessing.connection import wait
import numpy as np 
from threading import Thread
import time
from comms import comms
from time import sleep

comm = comms()


def comms_thread():
    while True:
        while comm.notified[0]:
            for i in range(10):
                print(comm.read_command("CommandID"))
                sleep(1)
    
    
    

if __name__ == "__main__":
    commsthread = Thread(target = comms_thread, args = ())
    commsthread.start()
    print("thread started")
    
    