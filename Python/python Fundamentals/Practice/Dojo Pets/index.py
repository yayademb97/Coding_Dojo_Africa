class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
        	
    #!=== Constructor =======
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        print(f"This is Ninja information {self.first_name} {self.last_name} with {self.treats} and {self.pet_food}")
        
        
# implement the following methods:
    #!=== Methods =======
# walk() - walks the ninja's pet invoking the pet play() method
    def walks(self):
        print(f"{self.first_name} walks their pet.")
        self.pet.play()
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feeds(self):
        print(f"{self.first_name} baths their pet.")
        self.pet.eats()
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} baths their pet.")
        self.pet.noise()

class Pet:
# implement __init__( name , type , tricks ):
    
    #!=== Constructor =======
    def __init__(self, name , type , tricks, energy= 100, health= 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
        print(f"This is our pet information: {self.name}, type: {self.type} and tricks: {self.tricks}")
# implement the following methods:
    #!=== Methods =======
# sleep() - increases the pets energy by 25
    def sleep(self):
        print(f"{self.name} sleeps.")
        self.energie += 25
        print(f"{self.name} sleeping and his energy is: {self.energy}")

# eat() - increases the pet's energy by 5 & health by 10
    def eats(self):
        print(f"{self.name} eats.")
        self.energy += 5
        self.health +- 10
        print(f"{self.name} eating and his energy is: {self.energy} and his health is: {self.health}")
# play() - increases the pet's health by 5
    def play(self):
        print(f"{self.name} plays.")
        self.health += 5
        print(f"{self.name} increases health by: {self.health}")
# noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} make a noise.")

ninja_1 = Ninja("Radhouen", "Trabelsi", "Biscuits", "Croquettes", Pet("Fluffy", "Dog", "Fetch"))


ninja_1.walks()
ninja_1.feeds()
ninja_1.bathe()