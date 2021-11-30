'''
Using the vehicle class that you created in the previous exercises, create 200 objects vehicle.
50 of them will be electric cars, 50 of them will be non electric cars. 50 of them will be electric trucks and
50 of them will be non electric trucks. The attribute velocity will be initialised randomly (with a positive number).

Write a function that takes as arguments a list of vehicles and a positive real number t (that represents time). The function will output the average 
emission for each category of vehicles (so, 4 averages, electric and non electric cars and trucks).

Notice that the velocity of each vehicle is expressed in terms of x and y component and you need to compute the total distance travelled.

hint: divide this exercise in subproblems and write appropriate functions for each subproblem

Weight: 3
'''
import numpy as np

class Vehicle:

    def __init__(self, type, velocity, colour, electric):
        self.type = str(type)
        self.velocity = np.array(velocity) 
        self.colour = str(colour)
        self.electric = bool(electric)


# doesn't work
    def update_tuple(self, new_velocity):
        list_velocity = list(self.velocity)
        list_velocity[0] = new_velocity[0]
        list_velocity[1] = new_velocity[1]
        self.velocity = tuple(list_velocity)

    def info(self):
        print(f"This vehicle is a {self.colour} {self.type} travelling at a velocity of {self.velocity}. It is electric: {self.electric}.")
    
    def emissions(self, distance):
        
        if self.electric == True and self.type == "Car":
          emissions = 1* distance
        elif self.electric == True and self.type == "Truck":
          emissions = 5*(distance)
        elif self.electric == False and self.type == "Car":
          emissions = 10* distance
        else:
          emissions = 50* distance
        return float(emissions)

electric_cars = [Vehicle("Car", (np.random.randint(0,100), np.random.randint(0,100)), "colour", True) for i in range(50)] 
electric_trucks = [Vehicle("Truck", (np.random.randint(0,100), np.random.randint(0,100)), "colour", True) for i in range(50)]
non_electric_cars = [Vehicle("Car", (np.random.randint(0,100), np.random.randint(0,100)), "colour", False) for i in range(50)]
non_electric_trucks = [Vehicle("Truck", (np.random.randint(0,100), np.random.randint(0,100)), "colour", False) for i in range(50)]


def average_emissions(list_objects, t):
    emissions = []
    for i in list_objects:
        distance = ((i.velocity[0]**2 + i.velocity[1]**2)**0.5) * t
        emis = i.emissions(distance)
        emissions.append(emis)
    sum_emissions = 0

    for i in emissions:
        sum_emissions = sum_emissions + i
        average = sum_emissions/50
    return average


print(f"Electric Cars emissions: {average_emissions(electric_cars, 5)}")
print(f"Electric Trucks emissions: {average_emissions(electric_trucks, 5)}")
print(f"Non-electric Trucks emissions: {average_emissions(non_electric_trucks, 5)}")
print(f"Non-electric Cars emissions: {average_emissions(non_electric_cars, 5)}")

