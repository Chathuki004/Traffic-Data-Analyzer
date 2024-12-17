#Author:H.M.Chathuki Lawanya
#Date:09/12/2024
#Student ID:20240769

# Task A
import csv #Used for handling csv files (Reference: https://docs.python.org/3/library/csv.html)

# List of files with csv datasets with traffic data collected on three specific dates
file_names = ['traffic_data15062024.csv', 'traffic_data21062024.csv', 'traffic_data16062024.csv']

# Asks the user to enter a valid day
# Handles errors with try-except
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

#Asks the user to enter a valid month
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

#Asks the user to enter a valid year
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
    return f"{day:02d}/{month:02d}/{year}"
'''Asks the user if they want to load another file and
 checks if they answer "Y" or "N".'''

"""
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
def validate_continue_input():
    while True:
        repeat = input("Do you want to select another data file for a different date? Y/N > ")
        if repeat.lower() == 'y':
            return True
        elif repeat.lower() == 'n':
            return False
        else:
            print("Please enter 'Y' or 'N'.")

def validate_file_exists(date):
    file_name = f"traffic_data{date.replace('/', '')}.csv"
    if file_name in file_names:
        return file_name
    else:
        print(f"Error: No CSV file found for the date {date}. Please try another date.")
        return None
 
def process_csv_data(file_name, date):
    '''Reads the data from CSV files 
    and processes it based on the user-specified date'''
    # Initialize variables for counts
    truck_count = 0
    electric_vehicle_count = 0
    two_wheeled_count = 0
    bus_count = 0
    straight_count = 0
    bicycle_count = 0
    over_speed_count = 0
    total_vehicles_elm = 0
    vehicle_count_elm_rabbit_junction = 0
    vehicle_count_hanley_westway_junction = 0
    scooter_count = 0
    hourly_counts = [0] * 24  
    total_count = 0
    scooter_percentage = 0
    truck_percentage = 0
    average_bicycles_per_hour = 0
    rainy_hours = []  

    try:
        with open(file_name, mode="r") as file:
            lines = file.readlines()
            header = lines[0].strip().split(',')  
            data = [line.strip().split(',') for line in lines[1:]]  

            for row in data:
                #Total number of vehicles
                if row[1] == date:  
                    total_count += 1

                    # Truck count
                    if row[8].lower() == 'truck':
                        truck_count += 1

                    # Electric vehicle count
                    if row[9].lower() == 'true':
                        electric_vehicle_count += 1

                    # Two-wheeled vehicle count
                    if row[8].lower() in ['bike', 'motorcycle', 'scooter']:
                        two_wheeled_count += 1

                    # Buses heading north
                    if row[0].lower() == "elm avenue/rabbit road" and row[4].lower() == "n" and row[8].lower() == "buss":
                        bus_count += 1

                    # Straight travel
                    if row[3].lower() == row[4].lower():
                        straight_count += 1

                    # Bicycle count
                    if row[8].lower() == 'bicycle':
                        bicycle_count += 1

                    # Over-speeding count
                    if int(row[7]) > int(row[6]):  
                        over_speed_count += 1

                    # Junction vehicle counts
                    if row[0].lower() == 'elm avenue/rabbit road':
                        vehicle_count_elm_rabbit_junction += 1

                    if row[0].lower() == 'hanley highway/westway':
                        vehicle_count_hanley_westway_junction += 1

                    # Scooters at Elm Avenue/Rabbit Road
                    if row[0].lower() == "elm avenue/rabbit road":
                        total_vehicles_elm += 1
                        if row[8].lower() == 'scooter':
                            scooter_count += 1

                    # Hourly counts for Hanley Highway/Westway
                    if row[0].lower() == 'hanley highway/westway':
                        hour = int(row[2].split(':')[0])  
                        hourly_counts[hour] += 1

                    # Rain hours
                    if row[5].lower() in ['light rain', 'heavy rain']:
                        hour = row[2].split(":")[0]  
                        if hour not in rainy_hours:
                            rainy_hours.append(hour)

        # Percentage calculations
        scooter_percentage = round((scooter_count / total_vehicles_elm * 100)) if total_vehicles_elm > 0 else 0
        truck_percentage = round((truck_count / total_count * 100)) if total_count > 0 else 0
        peak_vehicle_count = max(hourly_counts)
        average_bicycles_per_hour = round(bicycle_count / 24)
        peak_hour_times = [
            f"Between {hour}:00 and {hour+1}:00" for hour, count in enumerate(hourly_counts) if count == peak_vehicle_count
        ]

    except Exception as e:
        print(f"An unexpected error occurred with file '{file_name}': {e}")

    # Prepare results
    results = [
        f"***************************",
        f"Data file selected is {file_name}",
        f"***************************",
        f"The total number of vehicles recorded for this date is {total_count}.",
        f"The total number of trucks recorded for this date is {truck_count}.",
        f"The total number of electric vehicles for this date is {electric_vehicle_count}.",
        f"The total number of two-wheeled vehicles for this date is {two_wheeled_count}.",
        f"The total number of Buses leaving Elm Avenue/Rabbit Road heading North is {bus_count}.",
        f"The total number of Vehicles through both junctions not turning left or right is {straight_count}.",
        f"The percentage of total vehicles recorded that are trucks for this date is {truck_percentage}%.",
        f"The average number of Bikes per hour for this date is {average_bicycles_per_hour}.",
        f"The total number of Vehicles recorded as over the speed limit for this date is {over_speed_count}.",
        f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {vehicle_count_elm_rabbit_junction}.",
        f"The total number of vehicles recorded through Hanley Highway/Westway junction is {vehicle_count_hanley_westway_junction}.",
        f"{scooter_percentage}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.",
        f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_vehicle_count}.",
        f"The most vehicles through Hanley Highway/Westway were recorded {', '.join(peak_hour_times)}.",
        f"The number of hours of rain for this date is {len(rainy_hours)}."
    ]
#Task C
    # Save results to a file
    #Saves the processed outcomes to a text file and appends if the program loops.
    results_file = "results.txt"
    with open(results_file, "a") as file:
        for result in results:
            file.write(result + "\n")

    return results

# Main loop
while True:
    date = get_valid_date_string()
    file_name = validate_file_exists(date)
    if file_name:  # Only process data if the file exists
        results = process_csv_data(file_name, date)
        for result in results:
            print(result)

    if not validate_continue_input():
        print("End of run")
        break
# if you have been contracted to do this assignment please do not remove this line