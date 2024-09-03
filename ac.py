import pickle as bin
from ap import AccessPoint

class AccessController:
    def __init__(self, access_points = []):
        self.step = 1
        self.log = ""
        self.access_points = access_points
        self.in_range = {}
        self.allocation = {}

    def write_log(self, message):
        self.log += f"{message}\n"
 
    def dump(self):
        with open("access_controller.pkl", "wb") as binary_file:
            bin.dump(self.log, binary_file)

    def unbin(self):
        with open("access_controller.pkl", "rb") as binary_file:
            content = bin.load(binary_file)
        
        return content
            
    def __call__(self):
        print(self.unbin())
    
    def __str__(self):
        return self.unbin()
    
    
    def compare(self, ap, other):
        dist = ap.calc_distance(other.get_x(), other.get_y())
        rad = ap.get_coverage_radius()
        if dist <= rad:
            return True
            
    def allocate(self, access_point):
        temp = self.allocation
        if access_point not in self.allocation:
            if len(self.allocation) == 0:
                self.allocation[access_point] = access_point.get_channel()
            else:
                for allocated in temp:
                    if self.compare(access_point, allocated):
                        if access_point.get_channel() == allocated.get_channel():
                            temp = access_point.get_channel() + 1
                            if temp > 11:
                                print(f"{access_point.get_name()} has no channel to connect to.")
                            access_point.set_channel(temp)
                self.allocation[access_point] = access_point.get_channel()
        
    def sort_access_points(self):
        for ap in self.access_points:
            self.allocate(ap)
