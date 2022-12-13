#!/usr/bin/python3
# a function that multiplies 2 matrices by using the module NumPy
"""
    define function 'lazy_matrix_mul' using numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        this function will multiply matrices using numpy
    """
    X = np.array(m_a)
    Y = np.array(m_b)
    return X.dot(Y)
