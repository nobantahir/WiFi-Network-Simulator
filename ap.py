import math
from network import Network
from log import Bin

class AccessPoint(Network):
    def __init__(self, name: str, x: int, y: int, channel: int, power_level: int, frequency: str, standard: str, support11k: str, support11v: str, support11r: str, coverage_radius: int, device_limit: int, min_rssi = None):
        super().__init__(x, y, standard, frequency, support11k, support11v, support11r, min_rssi)
        self.log = Bin("ap", name)
        self.name = name
        self.channel = channel
        self.power_level = power_level
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit
        self.devices = []
    
    def get_name(self):
        return self.name
    
    def get_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        self.channel = channel

    def get_power_level(self):
        return self.power_level
    
    def get_coverage_radius(self):
        return self.coverage_radius
    
    def get_standard(self):
        return super().get_standard()

    def get_device_limit(self):
        return self.device_limit
    
    def get_devices(self):
        return self.devices
    
    def add_device(self, device):
        self.devices.append(device)
    
    def remove_device(self, device):
        if device in self.devices:
            self.devices.remove(device)
    
    def capacity(self):
        if len(self.devices) + 1 <= self.device_limit:
            return True
        return False
    
    def calc_distance(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def calc_rssi(self, x, y, frequency):
        # If the client is out of range it will return false.
        # Assume that it isn't possible for distance from device to ap is 0 because of math domain error.
        distance = self.calc_distance(x, y)
        if distance >= 0:
            distance = 1
        if distance < self.get_coverage_radius():
            return self.power_level - (20 * math.log10(distance)) - (20 * math.log10(frequency)) - 32.44
        else:
            return False
