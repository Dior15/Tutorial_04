import numpy as np

def det(A, n):
    # Recursive computation of the determinant. Input: n X n array A. Out: determinant of A (float).
    if n==2:                                            # For 2x2 matrix, use definition.
        detA = A[0,0]*A[1,1] - A[0,1]*A[1,0]
    else:                                               # For larger matrices, compute recursively.
        detA = 0                                        # Initialize the determinant.
        for k in range(0,n):                            # Cofactor expansion.
            B = np.delete(A, k, 0)                      # Delete i-th row.
            B = np.delete(B, 0, 1)                      # Delete first column.
            detA += (-1)**k * A[k,0] * det(B, n-1)      # Recursive call.
    return detA

A = np.array([[5,3,5],[1,6,2],[7,7,3]])
print(det(A, 3))

print(np.linalg.det(A))