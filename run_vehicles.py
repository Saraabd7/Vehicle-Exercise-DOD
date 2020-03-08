# import all the classes

# create 2 vehicle instances

# call methods and attributes to test



# create 2 car instances
# make car accelerate and make them break
# make car honk and park


# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land



from Car_class import Car
from Plane_class import plane
from Vehicle_class import Vehicle

# create 2 vehicle instances
vehicle1 = Vehicle(8, 12)
vehicle2 = Vehicle(5, 9)

# call methods and attributes to test
print("Testing Vehicle acceleration - expected result 'Vroom'' ")
vehicle1.accelerate()
vehicle2.accelerate()

print("Testing Vehicle breaking - expected result 'Slow down'")
vehicle1.car_break()
vehicle2.car_break()

print("Testing Vehicle with Passengers = 8 and Cargo = 12. Expected result: 8, 12")
print(vehicle1.n_passengers)
print(vehicle1.size_cargo)

print("Testing Vehicle with Passengers = 5 and Cargo = 7. Expected result: 5, 9")
print(vehicle2.n_passengers)
print(vehicle2.size_cargo)

# create 2 car instances
# make car accelerate and make them break
# make car honk and park
car1 = Car(8, 12, 'Rover', 50, 150)
car2 = Car(5, 7, 'Mercedes-Benz G-Class', 20, 100)


print(car1.accelerate())
print(car2.accelerate())

print(car1.car_break())
print(car2.car_break())

print(car1.honk())
print(car2.honk())

print(car1.park())
print(car2.park())


# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land
plane1 = plane(550, 550, 'Airbus')
plane2 = plane(400, 400, 'Boeing')

print(plane1.accelerate())
print(plane2.accelerate())

print(plane1.car_break())
print(plane2.car_break())

print(plane1.fly())
print(plane2.fly())

print(plane1.land())
print(plane2.land())