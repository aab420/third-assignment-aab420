'''
Use the Vehicle class of the previous exercise (6). Add the following methods to the class:

- a method that takes as argument a tuple of two numbers and updates the velocity of the car to the input argument.
- a method that prints all the attributes of the car
- a method called "emissions". This method takes as argument a number (the distance travelled) and returns
  the amount of emissions produced by the Vehicle for that distance. If the vehicle is a non electric car
  the method will return 10 * distance, if the vehicle is a non electric truck, the  method will return 50 * distance. 
  If the vehicle is an electric car, the method will return 1 * distance and if the vehicle is an electric truck,
  the method will return 5 * distance. 

Weight: 2
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
        self.velocity = new_velocity
        print(self.velocity)

    def info(self):
        print(f"This vehicle is a {self.colour} {self.type} travelling at a velocity of {self.velocity}. It is electric: {self.electric}.")
    
    def emmisions(self, distance):
        if self.electric == True and self.type == "Car":
          emissions = 1* distance
        elif self.electric == True and self.type == "Truck":
          emissions = 5*(distance)
        elif self.electric == False and self.type == "Car":
          emissions = 10* distance
        else:
          emissions = 50* distance
        return print(emissions)


my_vehicle = Vehicle("Truck", (6, 7), "black", False )
new_velocity = (8,9)
my_vehicle.update_tuple(new_velocity)
my_vehicle.emmisions(8)
my_vehicle.info()
