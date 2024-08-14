# Total number of jumping jacks to complete
total_jumping_jacks = 100
# Number of jumping jacks per set
set_size = 10
# Initialize the count of completed jumping jacks
completed_jumping_jacks = 0

# Perform the workout routine
while completed_jumping_jacks < total_jumping_jacks:
    # Ask to perform a set of jumping jacks
    print(f"Perform {set_size} jumping jacks.")
    completed_jumping_jacks += set_size
    
    # Check if the workout is complete
    if completed_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
    
    # Ask if tired
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    # If tired, ask if they want to skip the remaining sets
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
    else:
        # Display the number of remaining jumping jacks
        remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining_jumping_jacks} jumping jacks remaining.")
