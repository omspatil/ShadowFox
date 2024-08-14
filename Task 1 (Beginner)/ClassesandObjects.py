class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = False

    def get_info(self):
        return (f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Super Power: {self.super_power}, Weapon: {self.weapon}")
    
    def is_leader(self):
        return self.leader

    def set_leader(self):
        self.leader = True

# Creating instances for each superhero
captain_america = Avenger("Captain America", 100, "Male", "Super strength", "Shield")
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")

# Setting Captain America as the leader
captain_america.set_leader()

# List of Avengers
super_heroes = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# Displaying information about each superhero
for hero in super_heroes:
    print(hero.get_info())
    print(f"Is Leader: {hero.is_leader()}")
    print()
