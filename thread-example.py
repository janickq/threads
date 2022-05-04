from threading import Thread
from time import sleep
from objtest import objtest

test = objtest()

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(0.1)
        
def obj_threading1(arg):
    for i in range(arg):
        x = test.increment_obj1(2)
        print(x)
        sleep(0.1)

def obj_threading2(arg):
    for i in range(arg):
        y = test.multiply_obj2(2)
        print(y)
        sleep(0.1)
        

if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread2 = Thread(target = obj_threading1, args = (10, ))
    thread3 = Thread(target = obj_threading2, args = (10, ))
    thread.start()
    thread.join()
    thread2.start()
    thread2.join()
    thread3.start()
    thread3.join()
    print("thread finished...exiting")