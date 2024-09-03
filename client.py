from network import Network
from log import Bin

class Client(Network):
    def __init__(self, name: str, x: int, y: int, standard: str, frequency: str,  support11k: str, support11v: str, support11r: str, min_rssi: int):
        super().__init__(x, y, standard, frequency, support11k, support11v, support11r, min_rssi)
        self.name = name
        self.ap_scores = {}
        self.ap = None
        
    def get_name(self):
        return self.name
    
    def get_ap(self):
        return self.ap
    
    def set_ap(self, ap, frequency):
        self.ap = ap
        self.ap_frequency = frequency
    
    def remove_ap(self):
        self.ap = None
    
    def get_ap_scores(self):
        return self.ap_scores