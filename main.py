from multiprocessing.connection import wait
from threading import Thread
from comms import comms
from time import sleep
from commands import commands



comm = comms()
cmd = commands()
m_flag = False

def master(args):
    global m_flag
    while True:
        while comm.notified[0]:
            print(cmd.CommandID)
            print(comm.read_string("CommandID"))
            
            if cmd.CommandID == comm.read_string("CommandID"):
                m_flag = True
            else:
                m_flag = False
            print(m_flag)
            sleep(0.5)
                
            


def comms_thread(args):
    global m_flag
    while True:
        while m_flag:
            while comm.notified[0]:
                print("comm_thread active")
                sleep(1)
    
    
    

if __name__ == "__main__":
    masterthread = Thread(target = master, args = (10, ))
    commsthread = Thread(target = comms_thread, args = (10, ))
    masterthread.start()
    
    commsthread.start()
    masterthread.join()
    masterthread.join()
    print("thread started")
    
    