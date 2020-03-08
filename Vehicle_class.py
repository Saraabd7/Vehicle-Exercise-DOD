# Define vehicle class here

#C haracterists:
# n_passengers
# size_cargo

# Methods :
# accelerate
# break

class Vehicle():

    def __init__(self, n_passengers, size_cargo):
        self.n_passengers = n_passengers
        self.size_cargo = size_cargo

    def accelerate(self):
        return 'vroom'

    def car_break(self):
        return 'Slow down'