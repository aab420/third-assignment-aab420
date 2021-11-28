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