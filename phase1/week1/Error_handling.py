try:
    with open("fleet_data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: fleet_data.txt not found. Check the file path.")
    
try:
    battery_level = int(input("Enter battery level: "))
    percentage = 100 / battery_level
except ValueError:
    print("Error: Please enter a number, not text.")
except ZeroDivisionError:
    print("Error: Battery level cannot be zero.")
    
    
# Write a function called read_fleet_report that:
# 1. Takes a filename as a parameter
# 2. Tries to open and read the file
# 3. If the file exists — prints each line cleanly
# 4. If the file does NOT exist — prints a helpful error message
#    (do not let the program crash)
# 5. Test it twice:
#    - Once with "fleet_report.txt" (exists)
#    - Once with "missing_file.txt" (does not exist)

def read_fleet_report(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: {filename} not found. Check the file path.")

# Now call it twice to test both cases
read_fleet_report("fleet_report.txt")   # this file exists
read_fleet_report("missing_file.txt")   # this file does not exist