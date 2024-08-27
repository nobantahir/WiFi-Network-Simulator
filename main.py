import math
from ap import AccessPoint
from client import Client

test_power = 50
test_frequency = 5000
test_distance = 10

calc_rssi = test_power - (20 * math.log10(test_distance)) - (20 * math.log10(test_frequency)) - 32.44

#print(calc_rssi)

def acceptable_input(zero):
    assert zero in ["AP", "CLIENT", "MOVE"], "Error, input does not match expected."
    return zero

def parse_line(line):
    data = line.strip("\n").split(' ')
    line_call = acceptable_input(data[0])
    if line_call == "AP":
        if len(data) == 14:
            ap = AccessPoint(data[1], int(data[2]), int(data[3]), int(data[4]), int(data[5]), data[6], data[7], bool(data[8]), bool(data[9]), bool(data[10]), int(data[11]), int(data[12]), int(calc_rssi))
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

print(f"Number of Access Points: {len(access_points)}")
print(access_points)
print(clients)
print(moves)

print(simulation)
print(simulation[0].get_frequency())