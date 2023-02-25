import json
from typing import List


class Announcement:
    '''A route announcement received from BGP routers, also used to represent rows in the forwarding table.'''
    def __init__(self, network, netmask, peer, localpref, ASPath: List[int], selfOrigin, origin) -> None:
        self.network = network
        self.netmask = netmask
        self.peer = peer
        self.localpref = localpref
        self.ASPath = ASPath
        self.selfOrigin = selfOrigin
        self.origin = origin
    def __str__(self) -> str:
        return json.dumps({"peer": self.peer, "netmask": self.netmask, "network": self.network})
    def __repr__(self) -> str:
        return self.__str__()
    def getOriginLevel(self):
        '''Gets the origin of this announcement as an integer, with higher priority origins receiving higher values.'''
        if self.origin == "IGP":
            return 2
        elif self.origin == "EGP":
            return 1
        elif self.origin == "UNK":
            return 0
        else:
            return -1