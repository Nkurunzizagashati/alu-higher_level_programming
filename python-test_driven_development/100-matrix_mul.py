#!/usr/bin/python3
# a function that multiplies 2 matrices
"""
    define function 'matrix_mul'
"""


def matrix_mul(m_a, m_b):
    """
        this function will multiply twa matrices, m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not all(len(row) == len(m_b) for row in m_a):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix_b = []
    for a in range(len(m_b[0])):
        n = []
        for b in range(len(m_b)):
                n.append(m_b[b][a])
        new_matrix_b.append(n)
    new_matrix = []
    for row_a in m_a:
        # row in the new_matrix_b are columns in m_b
        n_row = []
        for row_b in new_matrix_b:
            product = 0
            for i in range(len(new_matrix_b)):
                product += row_a[i] * row_b[i]
            n_row.append(product)
        new_matrix.append(n_row)
    return new_matrix
