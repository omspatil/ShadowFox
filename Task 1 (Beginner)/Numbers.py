# Task 1: Formatted String
def format_number(number, format_spec):
    return format(number, format_spec)

formatted_string = format_number(145, 'o')
print("Formatted string:", formatted_string)
print()
# 'o' represents octal format

# Task 2: Area of Circular Pond
def calculate_pond_area(radius):
    pi = 3.14
    return pi * (radius ** 2)

radius = 84
pond_area = calculate_pond_area(radius)
print("Area of the pond:", pond_area)
print()

# Bonus Question
def calculate_water_amount(pond_area, water_per_square_meter):
    total_water = pond_area * water_per_square_meter
    return int(total_water)  # Removing decimal points

water_per_square_meter = 1.4
total_water = calculate_water_amount(pond_area, water_per_square_meter)
print("Total amount of water in the pond:", total_water)
print()

# Task 3: Calculate Speed
def calculate_speed(distance, time_minutes):
    time_seconds = time_minutes * 60  # Convert time to seconds
    speed = distance / time_seconds
    return int(speed)  # Removing decimal points

distance = 490
time_minutes = 7
speed = calculate_speed(distance, time_minutes)
print("Speed in meters per second:", speed)
print()
