'''
In machine learning, it's often important to add "padding" to a matrix, meaning
adding rows and columns of zeros around a given matrix. For instance consider the following matrix:

    | 5 1 |
    | 7 1 |

Adding a 1-padding to this matrix means turning it into:

    | 0 0 0 0 |
    | 0 5 1 0 |
    | 0 7 1 0 |
    | 0 0 0 0 |

While a 2-padding to this matrix means turning it into:

    | 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 |
    | 0 0 5 1 0 0 |
    | 0 0 7 1 0 0 |
    | 0 0 0 0 0 0 |
    | 0 0 0 0 0 0 |


Write a function that takes as arguments a NumPy matrix, M and a positive integer, n. 
The function returns the matrix M with a n-padding.
Provide examples to showcase that the functions works.
Don't use the function np.pad() of Numpy or equivalent functions to solve this exercise.

Weight: 2
'''
import numpy as np
np_matrix1 = np.array([(5,1), (7,2)])
np_matrix2 = np.array([(1,2), (3,4)])
pos_int = abs(int(input("Input your pad width: ")))

def pad(m,n): 
    dimensions = np.shape(m)
    rows = dimensions[0] + (2*n)
    columns = dimensions[1] + (2*n)
    newmatrix = np.zeros((rows,columns))
    newmatrix[n:n+dimensions[0], n:n+dimensions[1]] = m
    return newmatrix

ans1 = pad(np_matrix1, pos_int)
print("Padded Matrix 1: ")
print(ans1)

ans2 = pad(np_matrix2, pos_int)
print("Padded Matrix 2: ")
print(ans2) 



"""
# This function works FOR A 4x4 Matrix ONLY - but not the most efficient or dynamic
def pad(matrix, n):
    a = np.zeros((2*(n)+ 2, 2*(n)+ 2))
    a[n,n] = matrix[0,0]
    a[n,n+1] = matrix[0,1]
    a[n+1,n] = matrix[1,0]
    a[n+1,n+1] = matrix[1,1]
    return a
    
"""