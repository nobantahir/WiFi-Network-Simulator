from network import Network

class AccessPoint(Network):
    def __init__(self, name: str, x: int, y: int, channel: int, power_level: int, frequency: str, standard: str, support11k: bool, support11v: bool, support11r: bool, coverage_radius: int, device_limit: int, min_rssi = None):
        super().__init__(x, y, support11k, support11v, support11r, min_rssi)
        self.name = name
        self.channel = channel
        self.power_level = power_level
        self.frequency = frequency
        self.standard = standard
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit
        if self.min_rssi is not None:
            self.min_rssi = min_rssi