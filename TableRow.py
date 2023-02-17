import json
class TableRow:
    network = ""
    netmask = ""
    peer = ""
    localpref = ""
    ASPath = ""
    selfOrigin = ""
    origin = ""
    msg = {}
    
    def __init__(self, msg):
        self.msg = {}
        self.network = msg["network"]
        self.netmask = msg["netmask"]
        self.peer = msg["peer"]
        self.localpref = msg["localpref"]
        self.ASPath = msg["ASPath"]
        self.selfOrigin = msg["selfOrigin"]
        self.origin = msg["origin"]
        
    def getRow(self):
        return json.dumps(self.msg)
        