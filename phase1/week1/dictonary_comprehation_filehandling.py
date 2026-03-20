# Dictionary comprehensions practice
bus_data = {
    "bus_01": 87, "bus_02": 23, "bus_03": 65,
    "bus_04": 12, "bus_05": 90, "bus_06": 45
}

# Task A: buses above 50%
safe = {bus: level for bus, level in bus_data.items() if level > 50}
print(safe)

# Task B: battery levels as strings with % sign
percentage = {bus: str(level) + "%" for bus, level in bus_data.items()}
print(percentage)

# Task C: critical buses with emergency charge
emergency_charge = {bus: level*2 for bus, level in bus_data.items() if level < 30}
print(emergency_charge)

# Exercise 2A and 2B — write then read
bus_report = {"bus_01": 87, "bus_02": 23, "bus_03": 65}

with open("fleet_report.txt", "w") as f:
    for bus, level in bus_report.items():
        f.write(f"{bus}: {level}%\n")

with open("fleet_report.txt", "r") as f:
    for line in f:
        print(line.strip())

# Exercise 2C — reusable function
def write_fleet_report(data, filename):
    with open(filename, "w") as f:
        for bus, level in data.items():
            f.write(f"{bus}: {level}%\n")
write_fleet_report(bus_report, "fleet_report_v2.txt")
print("fleet_report_v2.txt written successfully")