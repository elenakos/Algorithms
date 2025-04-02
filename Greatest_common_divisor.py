'''
Find the greatest common divisor of two given positive integers.

Example:
GCD for 10 and 20 is 10
'''

import unittest

class Solution:
    def findGCD(self, a, b):
       if type(a) != int or type(b) != int:
           return  None
       if b == 0 or a == 0:
           return None

       gcd = 1
       for i in range(2, min(a, b) + 1):
           if a % i == 0 and b % i == 0:
               gcd = i
       return gcd

    def findGCD_better_algorithm(self, a, b):
       if type(a) != int or type(b) != int:
           return  None
       if b == 0 or a == 0:
           return None
       # Work with the remainders
       minV = min(a, b)
       maxV = max(a, b)
       remainder = 1
       while remainder != 0:
            print("*** {} - {}".format(maxV, minV))
            remainder = maxV%minV
            maxV = minV
            minV = remainder
       return maxV

class TestSolution(unittest.TestCase):

    def test_case_1_better(self):
        a = 10
        b = 20
        expected = 10
        actual = Solution().findGCD_better_algorithm(a, b)
        self.assertEqual(expected, actual)

    def test_case_large_numbers_better(self):
        a = 3918848
        b = 1653264
        expected = 61232
        actual = Solution().findGCD_better_algorithm(a, b)
        self.assertEqual(expected, actual)

    def test_case_no_gcd_better(self):
        a = 11
        b = 17
        expected = 1
        actual = Solution().findGCD_better_algorithm(a, b)

    def test_case_1(self):
        a = 10
        b = 20
        expected = 10
        actual = Solution().findGCD(a, b)
        self.assertEqual(expected, actual)

    def test_case_0(self):
        a = 0
        b = 20
        expected = None
        actual = Solution().findGCD(a, b)
        self.assertEqual(expected, actual)

    def test_case_no_gcd(self):
        a = 11
        b = 17
        expected = 1
        actual = Solution().findGCD(a, b)

    def test_case_letters(self):
        a = "A"
        b = 17
        expected = None
        actual = Solution().findGCD(a, b)
        self.assertEqual(expected, actual)

    def test_case_large_numbers(self):
        a = 3918848
        b = 1653264
        expected = 61232
        actual = Solution().findGCD(a, b)
        self.assertEqual(expected, actual)