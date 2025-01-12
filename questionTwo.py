import numpy as np

A = np.array (
    [
            [1,2,3],
            [4,5,6],
            [7,8,9]
    ]
)
B = np.array (
    [
            [1,2,3],
            [4,5,6],
            [7,8,9]
    ]
)
def compute_cross_product(arr1, arr2):
    return arr1 @ arr2

compute_cross_product(A, B) #test