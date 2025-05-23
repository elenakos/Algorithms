'''
Return the longest palindrome from a given string
Ignore empty spaces, capitalization, etc.
'''
import unittest
class LongestPalindrome:
    def find_longest_palindrome(self, s):
        if len(s) < 1:
           return ""
        print("Find the longest palindrome in: {}".format(s))
        # Clean the string
        working_string = self.clean_string(s)
        longest_palindrome = ""
        for i in range(len(working_string)):
            for j in range(i + 1, len(working_string)):
                current_string = working_string[i:j+1]
                if self.is_palindrome(current_string):
                    if len(current_string) > len(longest_palindrome):
                        longest_palindrome = current_string
                        if len(longest_palindrome) == len(working_string):
                            break
        print("==> Longest palindrome is: [{}]".format(longest_palindrome))
        return longest_palindrome

    def clean_string(self, s):
        print("Clean string")
        clean_string = ""
        for char in s:
            if char.isalnum():
                clean_string += char.lower()
        return clean_string

    def is_palindrome(self, s):
        #print("Check if a current string is palindrome")
        i = 0
        j = len(s) - 1
        while (i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    # ------------------------------
    # Another algorithm
    # ------------------------------

    def longest_palindrome_start_expanding(self, s):
        if len(s) < 1:
            return ""

        start = 0
        end = 0
        s = self.clean_string(s)
        for i in range (len(s)):
            len1 = self.expand_from_center(s, i, i)  # odd-length palindrome
            len2 = self.expand_from_center(s, i, i+1)
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + (max_len - 1) // 2
        return s[start:end+1]

    def expand_from_center(self, s, left, right):
        #print("-- Expanding from the center")
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1

class TestLongestPalindrome(unittest.TestCase):
    def test_the_entire_string_is_palindrome(self):
        print("\n*** TC: Test the entire string is palindrome")
        s = "level"
        expected = "level"
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)

    def test_the_entire_string_is_palindrome_need_clean(self):
        print("\n*** TC: Test the entire string is palindrome, but needs cleaning")
        s = "Madam, I'm Adam."
        expected = "madamimadam"
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)

    def test_partial_string_is_palindrome(self):
        print("\n*** TC: Test the partial string is palindrome")
        s = "Canal"
        expected = "ana"
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)

    def test_all_same_chars(self):
        print("\n*** TC: All characters are the same")
        c = "AAAaaaAAAaaa"
        expected = "aaaaaaaaaaaa"
        actual = LongestPalindrome().find_longest_palindrome(c)
        self.assertEqual(expected, actual)

    def test_all_different_chars(self):
        print("\n*** TC: All characters are different")
        s = "abcdefg"
        expected = ""
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)

    def test_longest_palindrome_at_the_start(self):
        print("\n*** TC: Longest palindrome at start")
        s = "2002Hello"
        expected = "2002"
        actual = LongestPalindrome().find_longest_palindrome(s)

    def test_short_palindrome_at_the_end(self):
        print("\n*** TC: Shortest palindrome at end")
        s = "Wonderful lol"
        expected = "lol"
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)

    # ----------------------------
    def test_the_entire_string_is_palindrome_need_clean_with_expand(self):
        print("\n*** TC: Test the entire string is palindrome, but needs cleaning - with an expand algorithm")
        s = "Madam, I'm Adam."
        expected = "madamimadam"
        actual = LongestPalindrome().longest_palindrome_start_expanding(s)
        self.assertEqual(expected, actual)

    def test_short_palindrome_at_the_end_with_expand(self):
        print("\n*** TC: Shortest palindrome at end - with an expand algorithm")
        s = "Wonderful lol"
        expected = "lol"
        actual = LongestPalindrome().find_longest_palindrome(s)
        self.assertEqual(expected, actual)