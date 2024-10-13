import matplotlib.pyplot as plt
import numpy as np

# Function to visualize matrix with access patterns
def plot_matrix_access(matrix_A, matrix_B, title, row_access_A=True, row_access_B=True):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot Matrix A
    axes[0].matshow(matrix_A, cmap='Blues', alpha=0.3)
    for i in range(matrix_A.shape[0]):
        for j in range(matrix_A.shape[1]):
            axes[0].text(x=j, y=i, s=matrix_A[i, j], va='center', ha='center')

    if row_access_A:
        for i in range(matrix_A.shape[0]):
            for j in range(matrix_A.shape[1] - 1):
                axes[0].arrow(j, i, 0.8, 0, head_width=0.2, head_length=0.1, fc='blue', ec='blue')
    else:
        for j in range(matrix_A.shape[1]):
            for i in range(matrix_A.shape[0] - 1):
                axes[0].arrow(j, i, 0, 0.8, head_width=0.2, head_length=0.1, fc='red', ec='red')

    axes[0].set_title("Matrix A Access Pattern")

    # Plot Matrix B
    axes[1].matshow(matrix_B, cmap='Greens', alpha=0.3)
    for i in range(matrix_B.shape[0]):
        for j in range(matrix_B.shape[1]):
            axes[1].text(x=j, y=i, s=matrix_B[i, j], va='center', ha='center')

    if row_access_B:
        for i in range(matrix_B.shape[0]):
            for j in range(matrix_B.shape[1] - 1):
                axes[1].arrow(j, i, 0.8, 0, head_width=0.2, head_length=0.1, fc='blue', ec='blue')
    else:
        for j in range(matrix_B.shape[1]):
            for i in range(matrix_B.shape[0] - 1):
                axes[1].arrow(j, i, 0, 0.8, head_width=0.2, head_length=0.1, fc='red', ec='red')

    axes[1].set_title("Matrix B Access Pattern")

    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

# Example matrices A and B
matrix_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Plot Non-Optimized Access Pattern (Row-wise for A, Column-wise for B)
plot_matrix_access(matrix_A, matrix_B, 
                   "Non-Optimized Access: Row-wise for A, Column-wise for B", 
                   row_access_A=True, row_access_B=False)

# Plot Optimized Access Pattern (Row-wise for both A and B)
plot_matrix_access(matrix_A, matrix_B.T, 
                   "Optimized Access: Row-wise for Both A and B", 
                   row_access_A=True, row_access_B=True)
