from log import Bin

class AccessController(Bin):
    def __init__(self, access_points = []):
        super().__init__()
        self.access_points = access_points
        self.in_range = {}
        self.allocation = {}
    
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
