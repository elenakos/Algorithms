'''
Given a string, verify if a string is a palindrome
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
ignoring case, punctuation, and spaces.
Examples:
    level
    Madam, I'm Adam.
    9009
'''

import unittest

class Palindrome:
    def is_palindrome(self, s):
        if len(str(s)) == 0:
            print("==> A string is empty")
            return False

        # Clean a string from any empty spaces and punctuations
        clean_string = self.remove_spaces_and_punctuation(str(s))

        # navigate from both sides of the string and compare characters
        left = 0
        right = len(clean_string) - 1
        while left < right:
            if clean_string[left] != clean_string[right]:
                print("==> Characters are not the same: {} abd {}".format(clean_string[left], clean_string[right]))
                return False
            left += 1
            right -= 1
        print("==> is a palindrome!")
        return True

    def remove_spaces_and_punctuation(self, s):
        #print("Removing spaces and punctuation")
        clean_string = ""
        for ch in s:
            if ch.isalnum():
                clean_string += ch.lower()
        return clean_string

class SolutionTest(unittest.TestCase):
    def test_is_palindrome_one_word(self):
        print("\n*** TC: Check if <level> is a palindrome>")
        s = "level"
        expected = True
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)

    def test_is_palindrome_one_expression(self):
        print("\n*** TC: Check if <Madam, I'm Adam.> is a palindrome>")
        s = "Madam, I'm Adam."
        expected = True
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)

    def test_is_palindrome_numbers(self):
        print("\n*** TC: Check if <9009> is a palindrome>")
        s = 9009
        expected = True
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)

    def test_is_palindrome_empty(self):
        print("\n*** TC: Check if <> is a palindrome>")
        s = ""
        expected = False
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)

    def test_is_palindrome_one_character(self):
        print("\n*** TC: Check if <A> is a palindrome>")
        s = "A"
        expected = True
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)

    def test_is_palindrome_expression_with_accent(self):
        print("\n*** TC: Check if <No 'x' in Nixon.> is a palindrome>")
        s = "No 'x' in Nixon."
        expected = True
        actual = Palindrome().is_palindrome(s)
        self.assertEqual(expected, actual)