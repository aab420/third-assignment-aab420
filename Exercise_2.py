'''
Write a program to create a Numpy vector with values ranging 
from 15 to 55 and print all values except the first one and the last one.

Weight: 1
'''

# Is this what it is asking for? 

import numpy as np

a = np.random.randint(15,55)
b = np.random.randint(15,55)

vector = np.array([(a),(b)])

print(vector)

all_values = np.arange(15,55)
print(all_values[1:-1])
