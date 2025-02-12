'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

'''

import unittest

from urllib3 import ProxyManager


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        print("\nConvert this Roman string to an integer {}.".format(s))
        if len(s) == 0:
            print("The string is empty")
            return 0
        # Define a conversion dictionary
        romanToIntegers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        totalInteger = 0
        for i in range(len(s)):
            if s[i] not in romanToIntegers:
                print("--> The character is not a roman number: {}".format(s[i]))
                return 0
            if (i + 1 < len(s)) and s[i+1] not in romanToIntegers:
                print("--> The character is not a roman number: {}".format(s[i+1]))
                return 0
            if i + 1 < len(s) and romanToIntegers[s[i]] < romanToIntegers[s[i + 1]]:
                totalInteger -= romanToIntegers[s[i]]
            else:
                totalInteger += romanToIntegers[s[i]]
        print(" ==> {} translates to {}.".format(s, totalInteger))
        return totalInteger

class TestSolution(unittest.TestCase):
    def test_X_should_return_10(self):
        s = "X"
        expected = 10
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_XII_should_return_12(self):
        s = "XII"
        expected = 12
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_IV_should_return_4(self):
        s = "IV"
        expected = 4
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_IX_should_return_9(self):
        s = "IX"
        expected = 9
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_XL_should_return_40(self):
        s = "XL"
        expected = 40
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)


    def test_CM_should_return_900(self):
        s = "CM"
        expected = 900
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_not_a_roman_char_first_should_return_0(self):
        s = "ACL"
        expected = 0
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)

    def test_not_a_roman_char_last_should_return_0(self):
        s = "CMF"
        expected = 0
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)