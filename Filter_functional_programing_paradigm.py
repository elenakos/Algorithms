'''
Given an array, filter element by even or odd numbers using functional programming paradigm.
Example:
    [10, 11, 12, 13, 14, 15] --> [10, 12, 14]
'''
from unittest import result


def filter_array_normal_way(array, trigger="even"):
    if len(array) < 1:
        return []
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            if trigger == "even":
                result.append(array[i])
        else:
            if trigger == "odd":
                result.append(array[i])
    return result

# ---------------------------------------------------------
def filter_array_functional(array, operation):
    if len(array) < 1:
        return []
    result = []
    for i in range(len(array)):
        if operation(array[i]):
            result.append(array[i])
    return result


def is_even(element):
    return element % 2 == 0

def is_odd(element):
    return element % 2 == 1

def is_numeric(element):
    return isinstance(element, int) or isinstance(element, float)

def is_alphabetic(element):
    return str(element).isalpha()

import unittest

class TestFilter(unittest.TestCase):
    def test_filter_array_normal_way_even(self):
        print("\nTC: Testing filter_array_normal_way - even")
        arr = [10, 11, 12, 13, 14, 15]
        expected = [10, 12, 14]
        actual = filter_array_normal_way(arr)
        self.assertEqual(expected, actual)

    def test_filter_array_normal_way_odd(self):
        print("\nTC: Testing filter_array_normal_way - odd")
        arr = [10, 11, 12, 13, 14, 15]
        expected = [11, 13, 15]
        actual = filter_array_normal_way(arr, "odd")
        self.assertEqual(expected, actual)

    # -----------------------
    # Functional
    # -----------------------
    def test_filter_array_functional_even(self):
        print("\nTC: Testing filter_array_functional - even")
        arr = [10, 11, 12, 13, 14, 15]
        expected = [10, 12, 14]
        actual = filter_array_functional(arr, is_even)
        self.assertEqual(expected, actual)

    def test_filter_array_functional_odd(self):
        print("\nTC: Testing filter_array_functional - odd")
        arr = [10, 11, 12, 13, 14, 15]
        expected = [11, 13, 15]
        actual = filter_array_functional(arr, is_odd)
        self.assertEqual(expected, actual)

    def test_filter_array_functional_numeric(self):
        print("\nTC: Testing filter_array_functional - numeric")
        arr = [10, 11, "Hello", 13, 14, 15]
        expected = [10, 11, 13, 14, 15]
        actual = filter_array_functional(arr, is_numeric)
        self.assertEqual(expected, actual)

    def test_filter_array_functional_letters(self):
        print("\nTC: Testing filter_array_functional - letters")
        arr = [10, 11, "Hello", 13, "World!", 15]
        expected = ['Hello']
        actual = filter_array_functional(arr, is_alphabetic)
        self.assertEqual(expected, actual)