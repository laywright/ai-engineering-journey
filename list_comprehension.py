cities = ["berlin", "nairobi", "mombasa"]
upper = [city.upper() for city in cities]
# ['BERLIN', 'NAIROBI', 'MOMBASA']
print (upper)

# You have bus route data as a list of dictionaries
routes = [
    {"route": "A1", "distance_km": 42, "active": True},
    {"route": "B2", "distance_km": 18, "active": False},
    {"route": "C3", "distance_km": 67, "active": True},
    {"route": "D4", "distance_km": 29, "active": False},
]

# Task 1: Use a list comprehension to get only active routes
active_routes = [route for route in routes if route["active"]]
print (active_routes)
# Task 2: Use a list comprehension to get route names where distance > 30km
long_distance = [route["route"] for route in routes if route ["distance_km"] > 30]
print (long_distance)
# Task 3: Calculate total distance of active routes only — one line
total_distance_for_active_routes = sum(route["distance_km"] for route in routes if route["active"])
print(total_distance_for_active_routes)
# Task 4: Get a list of dictionaries with only active routes
# AND rename the "distance_km" key to "km" in each one
# Expected output: [{"route": "A1", "km": 42}, {"route": "C3", "km": 67}]
# Task 4: Active routes with renamed key
clean_routes = [
    {"route": route["route"], "km": route["distance_km"]}
    for route in routes
    if route["active"]
]

print(clean_routes)
# Output: [{'route': 'A1', 'km': 42}, {'route': 'C3', 'km': 67}]

# EXERCISE 1
# You have a list of bus battery levels (percentages)

batteries = [87, 23, 65, 12, 90, 45, 78, 8, 55, 100]
# Task A: Create a list of batteries that are below 20% (critical level)
critical_level = [battery for battery in batteries if battery < 20]
print(critical_level)
# Task B: Create a list of battery levels doubled (simulating a charge boost)
charge_boost = [battery*2 for battery in batteries]
print(charge_boost)
# Task C: Create a list of ONLY the batteries above 50%, but divide each by 100
#         so they become decimals (e.g. 87 becomes 0.87)
battery_health = [battery/100 for battery in batteries if battery > 50]
print(battery_health)

# EXERCISE 2
# You have a list of route names
routes = ["Route_A1", "Route_B2", "route_c3", "ROUTE_D4", "route_e5"]

# Task: Create a new list where ALL route names are uppercase
# Expected:['ROUTE_A1', 'ROUTE_B2', 'ROUTE_C3', 'ROUTE_D4', 'ROUTE_E5']
routes_upper = [route.upper() for route in routes]
print(routes_upper)

# EXERCISE 3
# You have charging times in minutes
charging_times = [120, 45, 200, 30, 180, 90, 15, 240]

# Task A: Get only the charging times that are longer than 1 hour (60 mins)
long_charging_times = [charging_time for charging_time in charging_times if charging_time >60]
print(long_charging_times)
# Task B: Convert those long charging times from minutes to hours (divide by 60)
#         Do it in ONE list comprehension
long_charging_times = [charging_time/60 for charging_time in charging_times if charging_time >60]
print(long_charging_times)