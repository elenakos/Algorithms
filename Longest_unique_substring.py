'''
Given a string s, find the length of the longest substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

import unittest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        print("\nFind the longest substring without repeating characters {}".format(s))

        if len(s) == 0:
            print("==> This string is empty")
            return 0

        allUniqueString = []
        allLength = []
        for i in range(len(s)):
            currentUnigueSubstring = ""
            for j in range( i, len(s)):
                if s[j] not in currentUnigueSubstring:
                    currentUnigueSubstring += s[j]
                else:
                    break
                if currentUnigueSubstring not in allUniqueString:
                    allUniqueString.append(currentUnigueSubstring)
                    allLength.append(len(currentUnigueSubstring))
        print("==> Unique strings: {}".format(allUniqueString))
        print("==> Length of longest substring: {}".format(max(allLength)))
        return max(allLength)


class TestSolution(unittest.TestCase):
    def test_should_return_three(self):
        stringToTest = "abcabcbb"
        result = Solution().lengthOfLongestSubstring(stringToTest)
        self.assertEqual(3, result)


    def test_should_return_nine(self):
        stringToTest = "1236547899787"
        result = Solution().lengthOfLongestSubstring(stringToTest)
        self.assertEqual(9, result)

    def test_empty_string(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)

    def test_one_char(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("a"), 1)

    def test_same_characters_in_a_string(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("BBBBBBBBBBBBB"), 1)