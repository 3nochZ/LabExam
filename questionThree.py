import numpy as np

four2 = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
a, b, c = np.linalg.svd(four2)

def reconstruct_matrix(U, S, V):
    diagMat = np.zeros((four2.shape[0], four2.shape[1]))
    np.fill_diagonal(diagMat, b)

    reconst = a @ diagMat @ c
    return reconst

reconstruct_matrix(a, b, c) #Test
