from typing import List


class Announcement:
    def __init__(self, network, netmask, peer, localpref, ASPath: List[int], selfOrigin, origin) -> None:
        self.network = network
        self.netmask = netmask
        self.peer = peer
        self.localpref = localpref
        self.ASPath = ASPath
        self.selfOrigin = selfOrigin
        self.origin = origin