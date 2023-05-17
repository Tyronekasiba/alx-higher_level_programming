#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list): a 2-dimensional list of integers

    Returns:
        list: a new matrix, same size as the input matrix, with each value being the square of the input value
"""
    # Create a new matrix with the same dimensions as the input matrix
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Use lambda function to compute the square of each value and store the result in the new matrix
    square = lambda x: x ** 2
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = square(matrix[i][j])

    return result
