import numpy as np

def calculate(list_array):
    if len(list_array) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list_array).reshape(3,3)
    row_mean = list(matrix.mean(axis=0))
    column_mean = list(matrix.mean(axis=1))
    flattened_mean = (matrix.mean())
    row_var = list(np.var(matrix, axis = 0))
    column_var = list(np.var(matrix, axis = 1))
    flattened_var = (np.var(matrix))
    row_std = list(np.std(matrix, axis = 0))
    column_std = list(np.std(matrix, axis = 1))
    flattened_std = np.std(matrix)
    row_max = list(np.max(matrix, axis = 0))
    column_max = list(np.max(matrix, axis = 1))
    flattened_max = np.max(matrix)
    row_min = list(np.min(matrix, axis = 0))
    column_min = list(np.min(matrix, axis = 1))
    flattened_min = np.min(matrix)
    row_sum = list(np.sum(matrix, axis = 0))
    column_sum = list(np.sum(matrix, axis = 1))
    flattened_sum = np.sum(matrix)
    calculations = {
        'mean': [row_mean, column_mean, flattened_mean],
        'variance': [row_var, column_var, flattened_var],
        'standard deviation': [row_std, column_std, flattened_std],
        'max': [row_max, column_max, flattened_max],
        'min': [row_min, column_min, flattened_min],
        'sum': [row_sum, column_sum, flattened_sum]
    }
        
        
    return calculations



