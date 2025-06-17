'''
A positive integer is considered uniform if all of its digits are equal. For example,
222 is uniform, while 223 is not.
Given two positive integers A and B, determine the number of uniform integers between
A and B, inclusive.

The uniform integers between 75 and 300 are 77, 88, 99, 111, 222
There are 9 uniform integers between 1 and 9

'''
import unittest

class UniformInteger:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.uniform_integers = []

    def generate_uniform_integers(self):
        #print("Generating Uniform Integers")
        min_len = len(str(self.A))
        max_len = len(str(self.B))
        for n in range(min_len, max_len+1):
            number_to_add = int('1' * (n))
            if number_to_add >= self.A and number_to_add <= self.B:
                self.uniform_integers.append(number_to_add)
            current = number_to_add
            for i in range(2, 10):
                current = current + number_to_add
                if self.A <= current <= self.B:
                    self.uniform_integers.append(current)
        print("==> {}".format(self.uniform_integers))
        return len(self.uniform_integers)


class TestUniformInteger(unittest.TestCase):
    def test_from_1_to_9(self):
        print("\n*** TC: Testing from1_to_9")
        range = UniformInteger(1, 9)
        actual = range.generate_uniform_integers()
        expected = 9
        self.assertEqual(actual, expected)

    def test_from_15_to_300(self):
        print("\n*** TC: Testing from 15_to_300")
        range = UniformInteger(15, 300)
        actual = range.generate_uniform_integers()
        expected = 10
        self.assertEqual(actual, expected)

    def test_from_32_to_1000(self):
        print("\n*** TC: Testing from 32_to_1000")
        range = UniformInteger(32, 1000)
        actual = range.generate_uniform_integers()
        expected = 16
        self.assertEqual(actual, expected)

    def test_from_999999999999_to_999999999999(self):
        print("\n*** TC: Testing from 999999999999_to_999999999999")
        range = UniformInteger(999999999999, 999999999999)
        actual = range.generate_uniform_integers()
        expected = 1
        self.assertEqual(actual, expected)