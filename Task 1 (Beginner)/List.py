# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Task 1: Calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)
print()

# Task 2: Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)
print()

# Task 3: Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)
print()

# Task 4: Aquaman and Flash are having conflicts, and you need to separate them. 
# Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("After separating Aquaman and Flash with Green Lantern:", justice_league)
print()

# Task 5: Replace the existing list with the new members.
new_justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_justice_league
print("New Justice League:", justice_league)
print()

# Task 6: Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Sorted Justice League:", justice_league)
print()

# BONUS: Predict the new leader
new_leader = justice_league[0]
print("New leader of the Justice League:", new_leader)
print()
