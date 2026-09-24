import numpy as np


def solve_for_k():
    # Coefficients of the LHS
    A = np.array([[2, 3], [4, 6]])

    # Iterate through potential integer values of k to check consistency
    for k in range(-100, 100):
        b = np.array([[6], [3 * k]])
        augmented = np.hstack((A, b))

        # Check if rank(A) == rank([A|b])
        if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(augmented):
            return k


k_val = solve_for_k()
print(f"The value of k is: {k_val}")

