class Network:
    def __init__(self, x: int, y: int, support11k: bool, support11v: bool, support11r: bool, min_rssi = None):
        self.x = x
        self.y = y
        self.support11k = support11k
        self.support11v = support11v
        self.support11r = support11r
        if min_rssi is not None:
            self.min_rssi = min_rssi
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_support_11k(self):
        return self.support11k
    
    def get_support_11v(self):
        return self.support11v
    
    def get_support_11r(self):
        return self.support11r
    
    def get_min_rssi(self):
        return self.min_rssi
        