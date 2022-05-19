import numpy as np
from numpy.typing import NDArray

def PCA(matrix: list[list[float]], number_of_components: int):
    matrix: NDArray = np.asarray(matrix)

    matrix = matrix - np.mean(matrix, axis = 0)

    covariance_matrix = np.cov(matrix, rowvar=False, bias=True)
    eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
    eigenvector_subset = sorted_eigenvectors[:,0:number_of_components]

    reduced_matrix = np.dot(eigenvector_subset.transpose(), matrix.transpose()).transpose()

    return reduced_matrix

    # variable_mean = [0]*len(matrix[0])
    # for row in range(len(matrix)):
    #     for col in range(len(matrix[row])):
    #         variable_mean[col] += matrix[row][col]
    # for i in range(len(variable_mean)):
    #     variable_mean[i] /= len(matrix)

    # for row in range(len(matrix)):
    #     for col in range(len(matrix[row])):
    #         matrix[row][col] -= variable_mean[col]

    # covariance_matrix: list[list[float]] = [0]*len(matrix[0])
    # for i in range(len(covariance_matrix)):
    #     for j in range(i, len(covariance_matrix)):

    #         l: list[float] = []
    #         for row in len(matrix):
    #             l.append(matrix[row][i]*matrix[row][j])
    #         mean = sum(l)/len(l)

    #         covariance_matrix[i].append(mean-variable_mean[i]*variable_mean[j])
    #         covariance_matrix[j].append(mean-variable_mean[i]*variable_mean[j])
