from comms import comms

class commands:
    
    def __init__(self):
        self.CommandID = 0.0
        self.CommandName = ""

    def sendcommand(self, command):
        comms.writeStr(command)
        self.CommandID = self.CommandID + 1;
        
    
    