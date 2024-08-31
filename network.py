class Network:
    def __init__(self, x: int, y: int, standard: str, frequency: str, support11k: bool, support11v: bool, support11r: bool, min_rssi = None):
        self.x = x
        self.y = y
        self.standard = standard
        self.frequency = frequency
        self.support11k = support11k
        self.support11v = support11v
        self.support11r = support11r
        if min_rssi is None:
            self.min_rssi = False
        else:
            self.min_rssi = min_rssi
            
        self.step = 1
        self.log = ""
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_standard(self):
        return int(self.standard[-1])
    
    def get_frequency(self):
        temp_frequencies = self.frequency.split('/')
        frequencies = [int(x.replace(".", "")) * 1000 if len(x) == 1 else int(x.replace(".", "")) * 100 for x in temp_frequencies]
        
        return frequencies


    def get_support_11k(self):
        return self.support11k
    
    def get_support_11v(self):
        return self.support11v
    
    def get_support_11r(self):
        return self.support11r
    
    def get_min_rssi(self):
        return self.min_rssi
        