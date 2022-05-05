from multiprocessing.connection import wait
from threading import Thread
import time
from comms import comms
from time import sleep
from commands import commands



comm = comms()
cmd = commands()
m_flag = False


def master():
    while True:
        print(cmd.CommandID)
        print(comm.read_string("CommandID"))
        while comm.notified[0]:
            if cmd.CommandID == comm.read_string("CommandID"):
                m_flag = True
            else:
                m_flag = False
                
            


def comms_thread():
    while m_flag:
        while comm.notified[0]:
            print(comm.read_command("CommandID"))
            sleep(1)
    
    
    

if __name__ == "__main__":
    masterthread = Thread(target = master, args = ())
    commsthread = Thread(target = comms_thread, args = ())
    masterthread.start()
    commsthread.start()
    print("thread started")
    
    