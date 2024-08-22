import math


test_power = 100
test_frequency = 2.4
test_distance = 1

print("Distance loss: ", 20 * math.log10(test_distance))
print("Frequency loss: ", 20 * math.log10(test_frequency))


calc_rssi = test_power - (20 * math.log10(test_distance)) - (20 * math.log10(test_frequency)) - 32.44

print(calc_rssi)