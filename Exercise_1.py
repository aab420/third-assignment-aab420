'''
Write a function that takes as arguments a numpy array, v and a tuple of two numbers a and b (with b >= a).
the function will return a Numpy array that contains all the values in v that are in the interval [a,b] (notice the inclusion).

example: input1 = np.array([1,2,3,4,5,6]), input2 = (1,5), output = np.array([1,2,3,4,5])
Provide examples to showcase that the functions works.

Weight: 1
'''
import numpy as np
input_array = np.array([1,2,3,4,5,6])
input_tuple = (1,5)
output_list = []

def intersection(array, tuple):
    for i in array:
        if i >= tuple[0] and i <= tuple[1] :
            output_list.append(i)
        else:
            continue
        output_array = np.array(output_list)
        
    return output_array
    
ans = intersection(input_array, input_tuple)
print(ans)