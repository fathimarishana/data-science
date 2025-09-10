import numpy as np

# Step 1: Get matrix size from user
n = int(input("Enter the size of the square matrix (n x n): "))

# Step 2: Get matrix elements from user
print(f"Enter the {n * n} elements row-wise (space-separated):")
elements = list(map(float, input().split()))

# Validate input length
if len(elements) != n * n:
    print("Error: Incorrect number of elements.")
    exit()

# Step 3: Create matrix A
A = np.array(elements).reshape(n, n)

print("\nOriginal Matrix A:")
print(A)

# Step 4: Perform SVD
U, S, VT = np.linalg.svd(A)

print("\nMatrix U:")
print(U)

print("\nSingular values:")
print(S)

print("\nMatrix VT (V Transpose):")
print(VT)

# Step 5: Create full S matrix with shape (n x n)
S_matrix = np.zeros((n, n))
np.fill_diagonal(S_matrix, S)

 # Step 6: Reconstruct the original matrix
A_reconstructed = U @ S_matrix @ VT

print("\nReconstructed Matrix A:")
print(A_reconstructed)

# Step 7: Check for reconstruction accuracy
if np.allclose(A, A_reconstructed):
    print("\nReconstruction successful (within numerical precision).")
else:
    print("\nReconstruction failed.")

                                                                                                                                                    1,1           Top

