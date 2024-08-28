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
            ap = AccessPoint(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), data[6], data[7], bool(data[8]), bool(data[9]), bool(data[10]), int(data[11]), int(data[12]), int(data[13]))
            access_points.append(ap)
        elif len(data) == 13:
            ap = AccessPoint(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), data[6], data[7], bool(data[8]), bool(data[9]), bool(data[10]), int(data[11]), int(data[12]))
            access_points.append(ap)
    elif line_call == "CLIENT":
        if len(data) == 10:
            client = Client(data[1], int(data[2]), int(data[3]), data[4], data[5], bool(data[6]), bool(data[7]), bool(data[8]), int(data[9]))
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
        dict: containing the {key: value} where key is the str({access point} {frequency}) and value is the rssi
    """
    temp_dict = {}
    client_rssi = client.get_min_rssi()
    for ap in access_points:
        ap_rssi = ap.calc_rssi(client.get_x(), client.get_y(), frequency)
        # If the frequency is beyond client spec, we will ignore it.
        if ap_rssi < client_rssi:
            if ap_rssi is not False:
                ap_rssi = abs(ap_rssi)
                name = f"{ap.get_name()} {frequency}"
                if ap.min_rssi is False:
                    temp_dict[name] = ap_rssi
                else:
                    if ap_rssi < ap.min_rssi:
                        temp_dict[name] = ap_rssi
    return temp_dict

def parse_access_points(client, access_points):
    if client.get_frequency() == '2.4':
        ap_rssi = iterate_frequencies(client, access_points, 2400)
    elif client.get_frequency() == '5':
        ap_rssi = iterate_frequencies(client, access_points, 5000)
    elif client.get_frequency() == '2.4/5':
        temp24 = iterate_frequencies(client, access_points, 2400)
        temp50 = iterate_frequencies(client, access_points, 5000)
        ap_rssi = {**temp24, **temp50}
    
    print(ap_rssi)

def run_simulation(simulation, access_points):
    for item in simulation:
        if type(item) == Client:
            parse_access_points(item, access_points)     
        else:
            pass

run_simulation(simulation, access_points)