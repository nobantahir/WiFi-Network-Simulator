from network import Network

class AccessPoint(Network):
    def __init__(self, x: int, y: int, support11k: bool, support11v: bool, support11r: bool, min_rssi = None):
        super().__init__(x, y, support11k, support11v, support11r, min_rssi)
        