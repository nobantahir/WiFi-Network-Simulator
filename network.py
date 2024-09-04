from log import Bin
class Network(Bin):
    def __init__(self, x: int, y: int, standard: str, frequency: str, support11k: str, support11v: str, support11r: str, min_rssi = None):
        super().__init__()
        self.x = x
        self.y = y
        self.standard = standard
        self.frequency = frequency
        
        if support11k.upper() == "TRUE":
            self.support11k = True
        elif support11k.upper() == "FALSE":
            self.support11k = False
        if support11v.upper() == "TRUE":
            self.support11v = True
        elif support11v.upper() == "FALSE":
            self.support11v = False
        if support11r.upper() == "TRUE":
            self.support11r = True
        elif support11r.upper() == "FALSE":
            self.support11r = False

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
    
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
    
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
        