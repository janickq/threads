from networktables import NetworkTables
from threading import Thread
import threading




class comms:
    
    connection = False
    
    def __init__(self):
        self.cond = threading.Condition()
        self.notified = [False]
        self.sd = NetworkTables.getTable("SmartDashboard")
        NetworkTables.initialize(server='10.86.0.2')
        NetworkTables.addConnectionListener(self.connectionListener, immediateNotify=True)

                
    
    def connectionListener(self, connected, info):
        print(info, '; Connected=%s' % connected)
        with self.cond:
            self.notified[0] = True
            self.cond.notify()
        print("Connected!")
    
    def send_command(self, command):
        self.sd.putstring(command)
        
    def read_string(self, str):
        return self.sd.getString(str, defaultValue = 0)
    
    def read_number(self, num):
        return self.sd.getNumber(num, defaultValue = -1)
    
    def read_bool(self, bool):
        return self.sd.getBool(bool, defaultValue = None)
        
    def read_command(self, command):
        print(self.sd.getNumber(command, defaultValue = 2))
        return self.sd.getAutoUpdateValue(command, defaultValue = 1)
  
        
    def read_pos(self):
        pass
    
    def writeStr(self, str1, str2):
        self.sd.putString(str1, str2)
        
    def writeStrArray(self, str1, str2):
        self.sd.putStringArray(str1, str2)
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
       
       
        
  