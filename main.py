import math
from ap import AccessPoint
from client import Client

access_points = []
clients = []
moves = []
simulation = []


def acceptable_input(zero):
    assert zero in ["AP", "CLIENT", "MOVE"], "Error, input does not match expected."
    return zero


def parse_line(line):
    # If the line is blank we don't have to parse it.
    if line.isspace():
        pass
    else:
        data = line.strip("\n").split(' ')
        line_call = acceptable_input(data[0])
        if line_call == "AP":
            if len(data) == 14:
                ap = AccessPoint(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), data[6], data[7], (data[8]), (data[9]), (data[10]), int(data[11]), int(data[12]), int(data[13]))
                access_points.append(ap)
            elif len(data) == 13:
                ap = AccessPoint(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), data[6], data[7], (data[8]), (data[9]), (data[10]), int(data[11]), int(data[12]))
                access_points.append(ap)
        elif line_call == "CLIENT":
            if len(data) == 10:
                client = Client(data[1], int(data[2]), int(data[3]), data[4], data[5], (data[6]), (data[7]), (data[8]), int(data[9]))
                clients.append(client)
                simulation.append(client)
        elif line_call == "MOVE":
            if len(data) == 4:
                move = (data[1], int(data[2]), int(data[3]))
                moves.append(move)
                simulation.append(move)


# Main is the Access Controller

#print("Enter Simulation File")
#sim = input()
sim = "C:\\Users\\noban\\Desktop\\P3\\sim.txt"
with open(sim, 'r') as sim_file:
    for line in sim_file:
        parse_line(line)


def iterate_frequencies(client, access_points, frequency):
    """This function will iterate over access points based on frequencies available and 
    add them to a dictionary if it is possible for them to be connected to. If the rssi is false
    then the client is out of the access points range.

    Args:
        client (object): the client object
        access_points (list of objects): a list of access points
        frequency (int): an int representing the frequency

    Returns:
        dict: containing the {key: value} where key is tuple (access point, frequency) and value is the rssi
    """
    temp_dict = {}
    client_rssi = client.get_min_rssi()
    for ap in access_points:
        ap_rssi = ap.calc_rssi(client.get_x(), client.get_y(), frequency)
        # If the rssi is beyond client spec, we will ignore it.
        if ap_rssi < client_rssi:
            if ap_rssi is not False:
                ap_rssi = abs(ap_rssi)
                name = (ap, frequency)
                if ap.min_rssi is False:
                    temp_dict[name] = ap_rssi
                else:
                    if ap_rssi < ap.min_rssi:
                        temp_dict[name] = ap_rssi

    return temp_dict


def dict_max(pairs):
    """This function will find the maximum value(s) in a dictionary and return them in a list.
    """
    max_value = max(pairs.values())
    access_points = [k for k, v in pairs.items() if v == max_value]
    
    return access_points


def check_standard(client_standard, access_points):
    """This function will check if the client's standard is supported by any access point.
    """
    compatiable = []
    for ap in access_points:
        if ap[0].get_standard() >= client_standard:
            compatiable.append(ap)
    if len(compatiable) != 0:
        return compatiable
    return False

def check_power(access_points):
    """This function will check access point power levels.
    """
    power_score = {}
    for ap in access_points:
        power_score[ap] = ap[0].get_power_level()
    
    return power_score

def same_ap(access_points):
    first_ap = access_points[0][0]
    same = True
    for ap in access_points:
        if ap[0] != first_ap:
            same = False
    if same:
        return True
    return False


def single_ap(access_points):
    if len(access_points) == 1:
        return access_points[0][0]
    else:
        return False

def check_roaming(k, v, r, access_points):
    roaming = {}
    for ap in access_points:
            roaming[ap] = 0
            
    for ap in access_points:
        if k and ap[0].get_support_11k():
            roaming[ap] += 1
        if v and ap[0].get_support_11v():
            roaming[ap] += 1
        if r and ap[0].get_support_11r():
            roaming[ap] += 1
    
    return roaming
    
def check_ap_limit(access_points):
    new_list = []
    for ap in access_points:
        if ap[0].capacity():
            new_list.append(ap)
    if len(new_list) == 0:
        return False
    
    return new_list

def check_channel(access_points):
    channels = {}
    acceptable = [11,6,1]
    for ap in access_points:
        if ap[0].get_channel() in acceptable:
            channels[ap] = ap[0].get_channel()
    if len(channels) == 0:
        return False
    return channels


def check_frequency(access_points):
    new_list = []
    fastest = max(access_points)[1]
    for ap in access_points:
        if ap[1] == fastest:
            new_list.append(ap)
    return new_list

def check_fast(access_points):
    new_list = []
    for ap in access_points:
        if ap[0].get_support_11r():
            new_list.append(ap)
    if len(new_list) == 0:
        return False
    return new_list

def get_connections(access_points):
    connections = {}
    for ap in access_points:
        connections[ap] = len(ap[0].get_devices())

    return connections
        
def final_connect(access_points):
    d = get_connections(access_points)
    return min(d, key = d.get)

def best_point(client, access_points):
    # Saving the clients specifications in local scope.
    # Standard, Frequency, 11k, 11v, 11r.
    standard = client.get_standard()
    k = client.get_support_11k()
    v = client.get_support_11v()
    r = client.get_support_11r()
    
    # Base case if one AP.   
    if single_ap(access_points):
        return single_ap(access_points)
    
    # Base case if no AP.
    if len(access_points) == 0:
        print("There are no access points.")
        return -1
    
    # 1. Filter for compatiable WiFi version.
    standard_met = check_standard(standard, access_points)
    if standard_met:
        # Check if only one ap meets standards.
        if single_ap(access_points):
            return single_ap(access_points)
        # 2. Filter for roaming standards.
        roaming = check_roaming(k, v, r, standard_met)
    else:
        roaming = check_roaming(k, v, r, access_points)
        
    # This will get the most compatible roaming standards.
    access_points = dict_max(roaming)
    # Check if only one ap meets standards.
    if single_ap(access_points):
        return single_ap(access_points)
    
    # 3. Filter for power level.
    access_points =  dict_max(check_power(access_points))
    # Check if only one ap meets standards.
    if single_ap(access_points):
        return single_ap(access_points)
    
    # 4. Filter for device limit.
    check_limit = check_ap_limit(access_points)
    if check_limit:
        access_points = check_limit
        # Check if only one ap meets standards.
        if single_ap(access_points):
            return single_ap(access_points)
    # Else all ap full.
    else:
        print("All access points are full.")
        return -1
    
    # 5. Filter for highest frequency.
    access_points = check_frequency(access_points)
    # Check if only one ap meets standards.
    if single_ap(access_points):
        return single_ap(access_points)
    
    # 6. Filter for best channels.
    check_best_ch = check_channel(access_points)
    if check_best_ch:
        access_points = dict_max(check_channel(check_best_ch))
        if single_ap(access_points):
            return single_ap(access_points)
    
    # 7. Filter for 802.11r.
    check_fast_con = check_fast(access_points)
    if check_fast_con:
        access_points = check_fast(access_points)
        # Check if only one ap meets standards.
        if single_ap(access_points):
            return single_ap(access_points)
    
    # All checks have been completed.
    # If there are any AP left, then we will connect to the AP with lowest connections.
    # If there are no AP then there are no suitable connections.
    if len(access_points) == 0:
        print("No suitable connections.")
        return -1
    
    if len(access_points) > 1:
        match = final_connect(access_points)
        return match
    

def parse_access_points(client, access_points):
    """This function will parse the access points for the client and return a dictionary
    with the key as the str({access point} {frequency}) and value as the rssi.

    Args:
        client (object): the client object
        access_points (list of objects): a list of access points
    Returns:
        dict: containing the {key: value} where key is the str({access point} {frequency}) and value is the rssi
    """
    if len(client.get_frequency()) == 1:
        ap_rssi = iterate_frequencies(client, access_points, int(client.get_frequency()[0]))
    else:
        ap_rssi_list = []
        for frequency in client.get_frequency():
            ap_rssi = iterate_frequencies(client, access_points, int(frequency))
            if len(ap_rssi) != 0:
                ap_rssi_list.append(ap_rssi)
        ap_rssi = {k: v for dictionary in ap_rssi_list for k, v in dictionary.items()}

    # access_points is filtered and aps that are not within rssi are removed from the list.
    access_points = [x for x in ap_rssi]

    print(best_point(client, access_points))
    


def run_simulation(simulation, access_points):
    for item in simulation:
        if type(item) == Client:
            parse_access_points(item, access_points)     
        else:
            pass

run_simulation(simulation, access_points)