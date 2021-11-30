'''
Write a class Vehicle, that takes in (via the constructor) the following attributes:

- type of the Vehicle (a string that can be either "Car" or "Truck")
- the velocity of the Vehicle (a tuple with two numbers, x and y)
- the color of the vehicle (a string)
- wheter or not the vehicle is electric (a boolean, True if it is an electric vehicle, False otherwise)

In the constructor argument, transform the tuple that you get as an input into a Numpy array.

Weight: 1
'''

import numpy as np

class Vehicle:

    def __init__(self, type, velocity, colour, electric):
        self.type = str(type)
        self.velocity = np.array(velocity) 
        self.colour = str(colour)
        self.electric = bool(electric)
        
    def info(self):
        print(f"This vehicle is a {self.colour} {self.type}. It travels at a velocity of {self.velocity}. It is electric: {self.electric}.")
        # To test this works

my_vehicle = Vehicle("Car", (3, 4), "black", True )
my_vehicle.info()

