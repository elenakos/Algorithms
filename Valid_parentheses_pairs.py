'''
Given a string s containing the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

There are two implementations:
- the first defined  two lists for open/closed parenthesis
- and the second is using a dictionary for open/closed parenthesis
'''

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print("\nChecking if '{}' is valid ".format(s))
        # Define parentheses
        open = ['(', '{',  '[']
        close = [')', '}', ']']
        if len(s) == 0:
            print("==> The string is empty")
            return False

        # Define a stack to keep track of parentheses
        brackets_stack = []
        for char in s:
            if char in open:
                brackets_stack.append(char)
            if char in close:
                if len(brackets_stack) == 0:
                    print("==> No matching open bracket: {}".format(char))
                    return False
                previous_bracket = brackets_stack.pop()
                previous_open_index = open.index(previous_bracket)
                if previous_open_index != close.index(char):
                    print("==> No match for {}".format(char))
                    return False
        if len(brackets_stack) != 0:
            print("==> Not all brackets were closed")
            return False
        print("==> All matching brackets were closed")
        return True

    def is_valid_using_dictionary(self, s):
        print("\nChecking if '{}' is valid using dictionary ".format(s))
        if len(s) == 0:
            print("==> The string is empty")
            return False
        # define a dictionary
        pair = {"(": ")", "{" : "}", "[" : "]"}
        brackets_stack = []
        for ch in s:
            if ch in pair.keys():
                brackets_stack.append(ch)
            if ch in pair.values():
                # check if the last element in brackets_stack is the kay for this value
                if len(brackets_stack) == 0:
                    print("==> No prior open brackets at all")
                    return False
                last_bracket = brackets_stack.pop()
                if pair[last_bracket] != ch:
                    print("==> No matching open bracket: {}".format(ch))
                    return False
        if len(brackets_stack) != 0:
            print("==> Not all brackets were closed")
            return False
        print("==> All matching brackets were closed")
        return True


class TestSolution(unittest.TestCase):
    def test_case_valid(self):
        s = "()"
        expected = True
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_valid_using_dict(self):
        s = "()"
        expected = True
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_open(self):
        s = "("
        expected = False
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_open_using_dict(self):
        s = "("
        expected = False
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_close(self):
        s = ")"
        expected = False
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_close_using_dict(self):
        s = ")"
        expected = False
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_empty(self):
        s = ""
        expected = False
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_empty_using_dict(self):
        s = ""
        expected = False
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_valid_no_brackets(self):
        s = "Hello"
        expected = True
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_valid_no_brackets_using_dict(self):
        s = "Hello"
        expected = True
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_valid_all_brackets(self):
        s = "Hello ({[]})"
        expected = True
        actual = Solution().isValid(s)
        self.assertEqual(expected, actual)

    def test_case_invalid_valid_all_brackets_using_dict(self):
        s = "Hello ({[]})"
        expected = True
        actual = Solution().is_valid_using_dictionary(s)
        self.assertEqual(expected, actual)