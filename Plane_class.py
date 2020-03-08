from Vehicle_class import *
class plane(Vehicle):
    def __init__(self, n_passengers, size_cargo, type):
        super().__init__(n_passengers, size_cargo)
        self.type = type

    def fly(self):
        return 'Take off'

    def land(self):
        return 'landing'