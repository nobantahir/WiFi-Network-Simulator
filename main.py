import math


test_power = 50
test_frequency = 5000
test_distance = 10

print("Distance loss: ", 20 * math.log10(test_distance))
print("Frequency loss: ", 20 * math.log10(test_frequency))


calc_rssi = test_power - (20 * math.log10(test_distance)) - (20 * math.log10(test_frequency)) - 32.44

print(calc_rssi)

def acceptable_input(zero):
    assert zero in ["AP", "CLIENT", "MOVE"], "Error, input does not match expected."
def parse_line(line):
    data = line.strip("\n").split(' ')
    acceptable_input(data[0])
    print(data, " length: ", len(data))
    


# Main is the Access Controller

print("Enter Simulation File")
#sim = input()
sim = "C:\\Users\\noban\\Desktop\\P3\\sim.txt"
with open(sim, 'r') as sim_file:
    for line in sim_file:
        parse_line(line)