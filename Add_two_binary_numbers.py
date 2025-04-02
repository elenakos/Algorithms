'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

import unittest
from sys import maxsize


class Solution(object):
    def add_two_binary_numbers(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        print("\nFind a binary sum of two binary numbers: {} and {}".format(a, b))
        sum_string = ""
        carryover = 0

        # traverse strings from back, add each pair of values and keep track of carryover if needed
        array1 = list(a)
        array2 = list(b)
        len1 = len(array1)
        len2 = len(array2)
        min_len = min(len1, len2)
        max_len = max(len1, len2)

        # Slice arrays from the end to get them the same length
        arr1 = array1[-min_len:]
        arr2 = array2[-min_len:]

        for i in range(min_len-1, -1, -1):
            if arr1[i] != "0" and arr1[i] != "1" :
                print("==> Wrong character in the first number: {}".format(arr1[i]))
                return 0
            if arr2[i] != "0" and  arr2[i] != "1":
                print("==> Wrong character in the second number: {}".format(arr2[i]))
                return 0
            if int(arr1[i]) + int(arr2[i]) == 0:
                if carryover == 1:
                    sum_string = "1" + sum_string
                    carryover = 0
                else:
                    sum_string += "0"
            elif int(arr1[i]) + int(arr2[i]) == 1:
                if carryover == 1:
                    sum_string = "0" + sum_string
                    carryover = 0
                else:
                    sum_string = "1" + sum_string
            else: # 1+1 = 2
                if carryover == 1:
                    sum_string = "1" + sum_string
                    carryover = 1
                else:
                    sum_string = "0" + sum_string
                    carryover = 1

        # Same length strings:
        if len1 == len2:
            if carryover == 1:
                sum_string = "1" + sum_string
            print("==> Final string: {}".format(sum_string))
            return sum_string

        # Add the rest of the longer number to the sum
        if min_len == len1: # the first string is shorter, so add the rest of the second string
            #print("--> the first string is shorter, so add the rest of the second string")
            if carryover == 0:
                rest = b[:min_len]
                sum_string = rest + sum_string
            else:
                rest = self.add_one_to_binary_number(b[:(max_len - min_len)])
                sum_string = rest + sum_string
        else:
            #print("--> the first string is longer, so add the rest of it")
            if carryover == 0:
                rest = a[:min_len]
                sum_string = rest + sum_string
            else:
                rest = self.add_one_to_binary_number(a[:(max_len - min_len)])
                sum_string = rest + sum_string
        print("==> Final string: {}".format(sum_string))
        return sum_string

    def add_one_to_binary_number(self, number_string):
        resulting_string = ""
        carryover = 1
        for i in range(len(number_string)-1, -1, -1):
            if number_string[i] == "1":
                if carryover == 1:
                    resulting_string = "0" + resulting_string
                    carryover = 1
                else:
                    resulting_string = "1" + resulting_string
                    carryover = 0
            if number_string[i] == "0":
                if carryover == 1:
                    resulting_string = "1" + resulting_string
                    carryover = 0
                else:
                    resulting_string = "0" + resulting_string
                    carryover = 0
        if carryover == 1:
            resulting_string = "1" + resulting_string
        return resulting_string


class TestSolution(unittest.TestCase):
    def test_valid_values_without_carryover(self):
        a = "11"
        b = "0"
        expected = "11"
        actual = Solution().add_two_binary_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_valid_values_with_carryover(self):
        a = "10"
        b = "10"
        expected = "100"
        actual = Solution().add_two_binary_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_valid_values_with_carryover_1(self):
        a = "111110"
        b = "11"
        expected = "1000001"
        actual = Solution().add_two_binary_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_valid_values_with_carryover_2(self):
        a = "1110"
        b = "111110"
        expected = "1001100"
        actual = Solution().add_two_binary_numbers(a, b)
        self.assertEqual(expected, actual)

    def test_invalid_chars(self):
        a = "1a"
        b = "b"
        expected = "0"
        actual = Solution().add_two_binary_numbers(a, b)
        self.assertEqual(expected, str(actual))

