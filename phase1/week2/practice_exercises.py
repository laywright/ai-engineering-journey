# EXERCISE 1 — String manipulation
# You have a list of raw sensor readings from a device
readings = [
    "TEMP:45.2C",
    "TEMP:38.7C",
    "TEMP:52.1C",
    "TEMP:41.0C",
    "TEMP:60.3C"
]

# Task A: Extract just the numbers as floats
temperatures = [float(r.replace("TEMP:", "").replace("C", "")) for r in readings]
print(temperatures)
# Expected: [45.2, 38.7, 52.1, 41.0, 60.3]
# Hint: use .replace() and .split()

# Task B: Find the highest temperature
# Expected: 60.3
highest_temp = max(float(reading.replace("TEMP:", "").replace("C", "")) for reading in readings)
print(highest_temp)
# Task C: Find all readings above 50 degrees
# Expected: [52.1, 60.3]
above_50 = [float(reading.replace("TEMP:", "").replace("C", "")) for reading in readings if float(reading.replace("TEMP:", "").replace("C", "")) > 50]
print(above_50)

# EXERCISE 2 — Nested data structures
fleet = [
    {"bus": "bus_01", "route": "A1", "passengers": 45, "battery": 87},
    {"bus": "bus_02", "route": "B2", "passengers": 12, "battery": 23},
    {"bus": "bus_03", "route": "A1", "passengers": 38, "battery": 65},
    {"bus": "bus_04", "route": "C3", "passengers": 67, "battery": 12},
    {"bus": "bus_05", "route": "B2", "passengers": 29, "battery": 90},
]

# Task A: Get a list of all buses on route "A1"
# Expected: ["bus_01", "bus_03"]
route_a1_buses = [bus["bus"] for bus in fleet if bus["route"] == "A1"]
print(route_a1_buses)
# Task B: Get the total number of passengers across all buses
total_passengers = sum(bus["passengers"] for bus in fleet)
print(total_passengers)
# Task C: Get a list of dictionaries containing only buses
#         with battery below 30% AND more than 20 passengers
for bus in fleet:
    if bus["battery"] < 30 and bus["passengers"] > 20:
        print(bus)
# Task D: Find the bus with the highest battery level
#         Expected: {"bus": "bus_05", ...}
best_bus = max(fleet, key=lambda bus: bus["battery"])
print(best_bus)