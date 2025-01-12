import numpy as np

A = np.array (
    [
            [1,2,3],
            [4,5,6],
            [7,8,9]
    ]
)

def find_matrix_shape(matrix):
    return matrix.shape

find_matrix_shape(A) #Test