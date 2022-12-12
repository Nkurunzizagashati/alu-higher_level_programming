#!/usr/bin/python3
# a test file for a function that returns the maximum
# integer using unittest
"""
    import 'unittest' module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    define function 'c_max_int'
"""


class c_max_int(unittest.TestCase):
    """
        this class will test whether the max_int
        function works properly
    """
    def test_max(self):
        """
            in case a list is ordered
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """
            in case our list is unordered
        """
        self.assertEqual(max_integer([2, 1, 5, 8, 6]), 8)

    def test_max_at_beginning(self):
        """
            in case the maximum int is at the beginning
        """
        self.assertEqual(max_integer([8, 6, 5, 4, 3]), 8)

    def test_maxin_string_list(self):
        """
            in case our list contains string
        """
        self.assertEqual(max_integer(['fab', 'gas', 'sad']), 'sad')

    def test_max_emptylist(self):
        """
            in case our list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_max_emptystring(self):
        """
            in case we have an empty string
        """
        self.assertEqual(max_integer(''), None)
        
    def test_max_string(self):
        """
            in case we have a string
        """
        self.assertEqual(max_integer('fabrice'), 'r')

    def test_max_list_with_1_element(self):
        """
            in case our list contains only one element
        """
        self.assertEqual(max_integer([2]), 2)

if __name__ == '__main__':
    unittest.main()
