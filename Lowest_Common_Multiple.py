'''
The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
This solution includes three algorithms to find the LCM
Example:
LCM for 4 and 6 is 12
'''

import unittest

class Solution:
    def findLCM(self, a, b):
        print("Find LCM for {} and {}".format(a, b))
        if a == 0 or b == 0:
            print("=> One of the values is 0")
            return 0

        for l in range(1, a * b + 1):
            if l % a == 0 and l % b == 0:
                print("=> Least common multiple of {} and {} is {}".format(a, b, l))
                return l
        return None

    def findLCM_better_algorithm(self, a, b):
        print("Find LCM for {} and {} with less iterations".format(a, b))
        if a == 0 or b == 0:
            print("=> One of the values is 0")
            return 0

        max_value = max(a, b)
        min_value = min(a, b)

        for i in range(max_value, a*b + 1, max_value):
            if i%min_value == 0:
                print("=> Least common multiple of {} and {} is {}".format(a, b, i))
                return i

    def findLCM_best(self, a, b):
        print("Find LCM for {} and {} using GCD".format(a, b))
        if a == 0 or b == 0:
            print("=> One of the values is 0")
            return 0
        minV = min(a, b)
        maxV = max(a, b)
        gcd = self.findGCD(minV, maxV)
        lcd = minV * int((maxV/gcd))
        print("=> Least common multiple of {} and {} is {}".format(a, b, lcd))
        return lcd


    def findGCD(self, a, b):
       if type(a) != int or type(b) != int:
           return  None
       if b == 0 or a == 0:
           return None
       # Work with the remainders
       minV = min(a, b)
       maxV = max(a, b)
       remainder = 1
       while remainder != 0:
            remainder = maxV%minV
            maxV = minV
            minV = remainder
       return maxV

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
        actual = Solution().findLCM_better_algorithm(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_best(self):
        a = 4
        b = 6
        expected = 12
        actual = Solution().findLCM_best(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_better2(self):
        a = 15
        b = 20
        expected = 60
        actual = Solution().findLCM_better_algorithm(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_better3(self):
        a = 11
        b = 17
        expected = 187
        actual = Solution().findLCM_better_algorithm(a, b)
        self.assertEqual(expected, actual)

    def test_valid_numbers_best2(self):
        a = 11
        b = 22
        expected = 22
        actual = Solution().findLCM_best(a, b)
        self.assertEqual(expected, actual)