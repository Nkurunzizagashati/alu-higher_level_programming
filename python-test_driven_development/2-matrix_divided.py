#!/usr/bin/python3
# a function that divides all elements of a matrix
"""
    define function 'matrix_divided'
"""


def matrix_divided(matrix, div):
    """
        this function will devide all elements of a matrix
        I will use map function to do this
    """
    new_matrix = []
    y = 0
    p = len(matrix)
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    while y < p:
        new_matrix.append(list(map(lambda x: round((x/div), 2), matrix[y])))
        y += 1
    return new_matrix
