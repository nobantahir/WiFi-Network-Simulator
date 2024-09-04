from network import Network
from log import Bin

class Client(Network):
    def __init__(self, name: str, x: int, y: int, standard: str, frequency: str,  support11k: str, support11v: str, support11r: str, min_rssi: int):
        super().__init__(x, y, standard, frequency, support11k, support11v, support11r, min_rssi)
        self.log = Bin("client", name)
        self.name = name
        self.ap_scores = {}
        self.ap = None
        self.ap_frequency = None
        self.ap_rssi = None

    def __str__(self):
        return self.log.__str__()
    
    def get_name(self):
        return self.name
    
    def get_ap(self):
        return self.ap
    
    def set_ap(self, ap):
        self.ap = ap
    
    def get_ap_frequency(self):
        return self.ap_frequency
    
    def set_ap_frequency(self, frequency):
        self.ap_frequency = frequency

    def remove_ap(self):
        self.ap = None
    
    def get_ap_rssi(self):
        return self.ap_rssi
    
    def set_ap_rssi(self, ap_rssi):
        self.ap_rssi = ap_rssi