import csv

# Function to validate day
def get_valid_day():
    while True:
        try:
            day = int(input("Enter the day of the survey (dd): "))
            if 1 <= day <= 31:
                return day
            else:
                print("Day must be between 1 and 31.")
        except ValueError:
            print("Please enter a valid integer.")

# Function to validate month
def validate_month():
    while True:
        try:
            month = int(input("Enter the month of the survey (MM): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Please enter a valid integer.")

# Function to validate year
def validate_year():
    while True:
        try:
            year = int(input("Enter the year of the survey (YYYY): "))
            if 2000 <= year <= 2024:
                return year
            else:
                print("Year must be between 2000 and 2024.")
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_date_string():
    day = get_valid_day()
    month = validate_month()
    year = validate_year()
    return f"{year}-{month:02d}-{day:02d}"

# Example usage
date = get_valid_date_string()

file_names = ['traffic_data15062024.csv', 'traffic_data21062024.csv', 'traffic_data16062024.csv']
 # Replace with your CSV file names

# List to store all data
data = []

# Process each file
for file_name in file_names:
    try:
        with open(file_name, mode="r") as file:
            lines = file.readlines()  # Read all lines from the file
            header = lines[0].strip().split(',')  # Split the first line for the header
            data = [line.strip().split(',') for line in lines[1:]]  # Split the remaining lines into rows

            data.append(data)  # Store the data for further access
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred with file '{file_name}': {e}")

# Total number of vehicles
total_count = len(data)

# Total number of trucks for the given date
truck_count = 0
for row in data:
    if row[0] == date and row[1].lower() == 'truck':
        truck_count += 1

# Count of electric vehicles for the given date
electric_vehicle_count = 0
for row in data:
    if row[0] == date and row[2].lower() == 'true':
        electric_vehicle_count += 1

# Count of two-wheeled vehicles for the given date
two_wheeled_count = 0
for row in data:
    if row[0] == date and row[1].lower() in ['bike', 'motorbike', 'scooter']:
        two_wheeled_count += 1

# Total number of busses for the given date at the specified junction and direction
bus_count = 0
for row in data:
    if row[0] == date and row[3].lower() == 'elm avenue/rabbit road' and row[4].lower() == 'north':
        bus_count += 1

# Count of vehicles going straight for the given date
straight_count = 0
for row in data:
    if row[0] == date and row[4].lower() == 'straight':
        straight_count += 1

# Truck percentage for the given date
if total_count == 0:
    truck_percentage = 0
else:
    truck_percentage = (truck_count / total_count) * 100

# Average bicycles per hour for the given date
bicycle_count = 0
for row in data:
    if row[0] == date and row[1].lower() == 'bicycle':
        bicycle_count += 1

average_bicycles_per_hour = round(bicycle_count / 24)

# Count of vehicles over the speed limit for the given date

over_speed_count = 0
for row in data:
    if row[0] == date and int(row[5]) > speed_limit:
        over_speed_count += 1

vehicle_count_elm_rabbit_junction = 0
for row in data:
    if row[0] == date and row[3].lower() == 'elm avenue/rabbit road':
        vehicle_count_elm_rabbit_junction += 1

vehicle_count_hanley_westway_junction = 0
for row in data:
    if row[0] == date and row[3].lower() == 'Hanley Highway/Westway':
        vehicle_count_elm_rabbit_junction += 1

total_vehicles = 0
scooter_count = 0

# Iterate over each row in the data
for row in data:
    # Check if the Date matches the selected date
    if row[0] == date:
        # Check if the junction matches Elm Avenue/Rabbit Road
        if row[3].lower() == "elm avenue/rabbit road":
            total_vehicles += 1
            # Check if the VehicleType is 'scooter'
            if row[1].lower() == 'scooter':
                scooter_count += 1

hourly_counts = [0] * 24  # Assuming there are 24 hours in a day

# Iterate over each row in the data
for row in data:
    # Check if the Date matches the selected date and the junction matches Hanley Highway/Westway
    if row[0] == date and row[3].lower() == 'Hanley Highway/Westway':
        hour = int(row[1].split(':')[0])  # Extract the hour from the timestamp
        hourly_counts[hour] += 1

# Find the peak hour (the hour with the maximum count)
peak_hour = hourly_counts.index(max(hourly_counts))
peak_vehicle_count = max(hourly_counts)


# Initialize a list with 24 False values, one for each hour
rain_hours = [False] * 24

# Iterate over each row in the data
for row in data:
    if row[0] == date and "rain" in row[4].lower():  # Check for the selected date and rain in weather condition
        hour = int(row[1].split(':')[0])  # Extract the hour from the timestamp
        rain_hours[hour] = True  # Mark that hour as rained

# Calculate the total number of hours with rain
total_rain_hours = sum(rain_hours)  # Summing True values gives the count of hours
results 
# Save results to a file
file_name = "results.txt"
with open(file_name, "a") as file:  # Open in append mode
    for result in results:
        file.write(result + "\n")  # Write each result to the file

# Display results in the shell
for result in results:
    print(result)
     
   
    
