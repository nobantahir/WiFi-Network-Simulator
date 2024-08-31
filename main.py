import math
from ap import AccessPoint
from client import Client


def acceptable_input(zero):
    assert zero in ["AP", "CLIENT", "MOVE"], "Error, input does not match expected."
    return zero


def parse_line(line):
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

# use if variable is False for min rssi  

access_points = []
clients = []
moves = []
simulation = []
# Main is the Access Controller

#print("Enter Simulation File")
#sim = input()
sim = "C:\\Users\\noban\\Desktop\\P3\\sim.txt"
with open(sim, 'r') as sim_file:
    for line in sim_file:
        parse_line(line)

#print(f"Number of Access Points: {len(access_points)}")
#print(access_points)


#print(simulation)
#print(simulation[0].get_frequency())
#print(access_points[0].calc_rssi(simulation[0].get_x(), simulation[0].get_y(), 2400))

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
        # If the frequency is beyond client spec, we will ignore it.
        if ap_rssi < client_rssi:
            if ap_rssi is not False:
                ap_rssi = abs(ap_rssi)
                name = (ap, frequency) #(f"{ap.get_name()} {frequency}")
                if ap.min_rssi is False:
                    temp_dict[name] = ap_rssi
                else:
                    if ap_rssi < ap.min_rssi:
                        temp_dict[name] = ap_rssi
    return temp_dict

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

def best_point(client, access_points):
    # Standard, Frequency, 11k, 11v, 11r
    standard = client.get_standard()
    k = client.get_support_11k()
    v = client.get_support_11v()
    r = client.get_support_11r()
    
    standard_met = check_standard(standard, access_points)
    if standard_met:
        print(standard_met)
    else:
        pass
    
    roaming = {}
    
    for ap in standard_met:
        roaming[ap] = 0
    print(roaming)
    
    for ap in standard_met:
        #print(ap[0].get_support_11k())
        
        if k and ap[0].get_support_11k():
            roaming[ap] += 1
        if v and ap[0].get_support_11v():
            roaming[ap] += 1
            
        #if r and ap[0].get_support_11r():
            #roaming[ap] += 1
            
    print(roaming)
    
    
    

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

    best_point(client, access_points)
    


def run_simulation(simulation, access_points):
    for item in simulation:
        if type(item) == Client:
            parse_access_points(item, access_points)     
        else:
            pass

run_simulation(simulation, access_points)