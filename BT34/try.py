import numpy as np


def compute_ref(matrix):
    """Computes Row Echelon Form (REF) using Gaussian Elimination."""
    ref = matrix.astype(float).copy()
    rows, cols = ref.shape
    pivot_row = 0

    for col in range(cols):
        if pivot_row >= rows:
            break

        # Find maximum pivot element in current column
        max_idx = np.argmax(np.abs(ref[pivot_row:, col])) + pivot_row
        if np.isclose(ref[max_idx, col], 0):
            continue

        # Swap rows and normalize pivot row
        ref[[pivot_row, max_idx]] = ref[[max_idx, pivot_row]]
        ref[pivot_row] /= ref[pivot_row, col]

        # Eliminate entries below pivot
        for r in range(pivot_row + 1, rows):
            ref[r] -= ref[r, col] * ref[pivot_row]

        pivot_row += 1

    return ref


# Define system components
A = np.array([[2, 3], [4, 6]])

# 1. Use np.linalg.solve on a valid linearly independent sub-system
# To solve 2x + 3y = 6, we can set x = 0 to get a specific solution point
A_sub = np.array([[2, 3], [1, 0]])  # 2x + 3y = 6 and x = 0
b_sub = np.array([6, 0])
xy_solution = np.linalg.solve(A_sub, b_sub)

# 2. Find k using the solved (x, y) point in 4x + 6y = 3k
x_val, y_val = xy_solution
k_val = int((4 * x_val + 6 * y_val) / 3)

# 3. Construct the full Augmented Matrix using np.block
b = np.array([[6], [3 * k_val]])
augmented = np.block([A, b])

# 4. Calculate Row Echelon Form
ref_matrix = compute_ref(augmented)

print(f"Solved (x, y) point : {xy_solution}")
print(f"Consistent value of k: {k_val}\n")

print("Augmented Matrix constructed with np.block:")
print(augmented)

print("\nRow Echelon Form (REF):")
print(ref_matrix)

