import random

# Number of times to roll the die
num_rolls = 20

# Initialize counters
count_6 = 0
count_1 = 0
consecutive_6s = 0
previous_roll = None

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)
    print(f"Roll: {roll}")
    
    # Count the number of times 6 is rolled
    if roll == 6:
        count_6 += 1
    
    # Count the number of times 1 is rolled
    if roll == 1:
        count_1 += 1
    
    # Count consecutive 6s
    if roll == 6 and previous_roll == 6:
        consecutive_6s += 1
    
    previous_roll = roll

# Print the results
print(f"Number of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s in a row: {consecutive_6s}")
