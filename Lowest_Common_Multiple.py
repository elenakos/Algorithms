'''
The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

'''

import unittest

class Solution:
    def findLCM(self, a, b):
        print("Find LCM for {} and {}".format(a, b))
        if a == 0 or b == 0:
            return 0

        for l in range(1, a * b + 1):
            if l % a == 0 and l % b == 0:
                return l
        return None

    def findLCM_better_algorithm(self, a, b):
        print("Find LCM for {} and {}".format(a, b))
        if a == 0 or b == 0:
            return 0

        max = max(a, b)
        min = min(a, b)

        for i in range(max, a*b + 1, max):
            if i%min == 0:
                return i

class TestSolution(unittest.TestCase):
    def test_valid_numbers(self):
        a = 4
        b = 6
        expected = 12
        actual = Solution().findLCM(a, b)
        self.assertEqual(expected, actual)

    def test_invalid_numbers(self):
        a = 0
        b = 33
        expected = 0
        actual = Solution().findLCM(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_better(self):
        a = 4
        b = 6
        expected = 12
        actual = Solution().findLCM(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_better2(self):
        a = 15
        b = 20
        expected = 60
        actual = Solution().findLCM(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_better3(self):
        a = 11
        b = 17
        expected = 60
        actual = Solution().findLCM(a, b)
        self.assertEqual(expected, actual)