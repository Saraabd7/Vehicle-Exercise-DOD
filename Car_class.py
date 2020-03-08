# import my vehicle class

# define car class here and make it inherit from vehicle


#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk
# import my vehicle class

# Define car class here and make it inherit from vehicle


# characteristic:
# brand
# horse_power
# max_speed

# Methods:
# park
# honk

from Vehicle_class import Vehicle

class Car(Vehicle):
    def __init__(self, n_passengers, size_cargo, brand, horse_power, max_speed):
        super().__init__(n_passengers, size_cargo)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed

# methods :
# park
# honk
    def park(self):
        return 'parking'

    def honk(self):
        return 'beeeeep beeep '