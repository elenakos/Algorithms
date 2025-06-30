'''
Given a string s, find the length of the longest substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

import unittest

class Solution(object):

    def length_of_longest_unique_substring_sliding_door(self, s):
        print("\nFind the longest substring without repeating characters - using a sliding door approach {}".format(s))
        if len(s) == 0:
            print("==> This string is empty")
            return 0

        all_unique_strings = []
        max_length = 0
        left = 0
        right = 0
        current_unique_string = ""
        while right < len(s):
            if s[right] not in current_unique_string:
                current_unique_string += s[right]
                right = right + 1
            else:
                max_length = max(max_length, len(current_unique_string))
                all_unique_strings.append(current_unique_string)
                current_unique_string = ""
                left += 1
                right = left
        max_length = max(max_length, len(current_unique_string))
        all_unique_strings.append(current_unique_string)
        print("==> Unique strings: {}".format(all_unique_strings))
        print("==> Length of longest substring without repeating characters: {}".format(max_length))
        return max_length



    def length_of_longest_unique_substring(self, s):
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
        result = Solution().length_of_longest_unique_substring(stringToTest)
        self.assertEqual(3, result)

    def test_should_return_three_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door("abcabcbb"), 3)

    def test_should_return_nine(self):
        stringToTest = "1236547899787"
        result = Solution().length_of_longest_unique_substring(stringToTest)
        self.assertEqual(9, result)

    def test_should_return_nine_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door("1236547899787"), 9)

    def test_empty_string(self):
        self.assertEqual(Solution().length_of_longest_unique_substring(""), 0)

    def test_empty_string_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door(""), 0)

    def test_one_char(self):
        self.assertEqual(Solution().length_of_longest_unique_substring("a"), 1)

    def test_one_char_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door("a"), 1)

    def test_same_characters_in_a_string(self):
        self.assertEqual(Solution().length_of_longest_unique_substring("BBBBBBBBBBBBB"), 1)

    def test_same_characters_in_a_string_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door("BBBBBBBBBBBBB"), 1)

    def test_longest_at_end(self):
        self.assertEqual(Solution().length_of_longest_unique_substring("ddef"), 3)

    def test_longest_at_end_in_a_string_using_sliding_door(self):
        self.assertEqual(Solution().length_of_longest_unique_substring_sliding_door("ddef"), 3)