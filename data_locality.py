import time
import numpy as np

N = 500
A = np.random.rand(N, N)
B = np.random.rand(N, N)
C = np.zeros((N, N))

def basic_matrix_multiply(A, B, C):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

start_time = time.time()
basic_matrix_multiply(A, B, C)
print(f"Basic Matrix Multiplication Time: {time.time() - start_time:.6f} seconds")

def optimized_matrix_multiply(A, B, C):
    BT = B.T  # Transpose matrix B to access rows instead of columns
    for i in range(N):
        for j in range(N):
            C[i][j] = np.dot(A[i, :], BT[j, :])

start_time = time.time()
optimized_matrix_multiply(A, B, C)
print(f"Optimized Matrix Multiplication Time: {time.time() - start_time:.6f} seconds")
