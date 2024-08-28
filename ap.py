import math
from network import Network

class AccessPoint(Network):
    def __init__(self, name: str, x: int, y: int, channel: int, power_level: int, frequency: str, standard: str, support11k: bool, support11v: bool, support11r: bool, coverage_radius: int, device_limit: int, min_rssi = None):
        super().__init__(x, y, standard, frequency, support11k, support11v, support11r, min_rssi)
        self.name = name
        self.channel = channel
        self.power_level = power_level
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit
    
    def get_name(self):
        return self.name
    
    def get_channel(self):
        return self.channel
    
    def get_power_level(self):
        return self.power_level
    
    def get_coverage_radius(self):
        return self.coverage_radius
    
    def get_device_limit(self):
        return self.device_limit
    
    def calc_distance(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def calc_rssi(self, x, y, frequency):
        distance = self.calc_distance(x, y)
        print("Distance", distance, " Coverage Radius", self.get_coverage_radius())
        return self.power_level - (20 * math.log10(distance)) - (20 * math.log10(frequency)) - 32.44
