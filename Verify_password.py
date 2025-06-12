'''
Create a method that returns Yes or No based on whether a password is strong:
- The length is at least 8 characters
- It contains special characters like ~!@#$%^&*()_+{}[]
- It contains at least one number
- There are lower case and uppercase letters
'''

import unittest

class Solution():

    def verifyPassword(self, password):
        print("Verifying this password: {}".format(password))
        result = self.is_password_long_enough(password) and self.is_passowrd_contains_special_characters(password) and self.is_password_contains_numbers(password) and self.is_password_contains_lowercase_letters(password)
        if result:
            print("==> Password is strong")
            return "Yes"
        else:
            print("==> Password is weak")
            return "No"

    def is_password_long_enough(self, password):
        print("Verify Password length")
        if len(password) < 8:
            return False
        else:
            return True

    def is_passowrd_contains_special_characters(self, password):
        print("Verify Password contains special characters")
        special_chard = "~!@#$%^&*()_+{}[]"
        for char in password:
            if char in special_chard:
                return True
        return False

    def is_password_contains_numbers(self, password):
        print("Verify Password contains numbers")
        for char in password:
            if char.isdigit():
                return True
        return False

    def is_password_contains_lowercase_letters(self, password):
        print("Verify Password contains lowercase letters")
        lower = False
        capital = False
        for char in password:
            if char.islower():
                lower = True
            if char.isupper():
                capital = True
        return lower and capital



class TestSolution(unittest.TestCase):
    def test_password_is_short(self):
        print("\n*** TC: Password is short ***")
        password = "hello"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_special_chars(self):
        print("\n*** TC: Password without special chars ***")
        password = "HelloWorld"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_digit(self):
        print("\n*** TC: Password without a digit ***")
        password = "HelloWorld!"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_upper_char(self):
        print("\n*** TC: Password without an upper case character ***")
        password = "wonderful12#"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_char(self):
        print("\n*** TC: Password without any upper/lower case character ***")
        password = "12345!@#$#"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_lowercase_char(self):
        print("\n*** TC: Password without any lower case character ***")
        password = "MONEY12!@$"
        actual = Solution().verifyPassword(password)
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_is_strong(self):
        print("\n*** TC: Password with all requirements ***")
        password = "Foobar123$"
        actual = Solution().verifyPassword(password)
        expected = "Yes"
        self.assertEqual(actual, expected)