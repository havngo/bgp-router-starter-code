import json
class TableRow:
    network = ""
    netmask = ""
    peer = ""
    localpref = ""
    ASPath = ""
    selfOrigin = ""
    origin = ""

    def __init__(self, msg, src):
        self.network = msg["network"]
        self.netmask = msg["netmask"]
        self.peer = src
        self.localpref = msg["localpref"]
        self.ASPath = msg["ASPath"]
        self.selfOrigin = msg["selfOrigin"]
        self.origin = msg["origin"]

    def getRow(self):
        msg = {
            "network": self.network,
            "netmask": self.netmask,
            "peer": self.peer,
            "localpref": self.localpref,
            "ASPath": self.ASPath,
            "selfOrigin": self.selfOrigin,
            "origin": self.origin
        }
        return msg
