from log import Bin

class AccessController():
    def __init__(self, access_points = []):
        self.log = Bin("ac", "access_controller")
        self.access_points = access_points
        self.in_range = {}
        self.allocation = {}
        
    def __str__(self):
        return self.log.__str__()
    
    def compare(self, ap, other):
        dist = ap.calc_distance(other.get_x(), other.get_y())
        rad = ap.get_coverage_radius()
        if dist <= rad:
            return True


    def allocate(self, access_point):
        temp = self.allocation
        moved = False
        if access_point not in self.allocation:
            if len(self.allocation) == 0:
                self.allocation[access_point] = access_point.get_channel()
            else:
                for allocated in temp:
                    if self.compare(access_point, allocated):
                        if access_point.get_channel() == allocated.get_channel():
                            temp = access_point.get_channel() + 1
                            if temp > 11:
                                m = f"{access_point.get_name()} has no channel to connect to."
                                self.log.write_log(m)
                                access_point.log.write_log(m)
                            access_point.set_channel(temp)
                            moved = True
                self.allocation[access_point] = access_point.get_channel()
        if moved:
            m = f"AC moved {access_point.get_name()} to channel {access_point.get_channel()}."
            self.log.write_log(m)
            access_point.log.write_log(m)
        else:
            m = f"AC accepts {access_point.get_name()} on channel {access_point.get_channel()}."
            self.log.write_log(m)
            access_point.log.write_log(m)

    def sort_access_points(self):
        for ap in self.access_points:
            self.allocate(ap)
