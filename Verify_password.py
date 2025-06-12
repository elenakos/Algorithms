'''
Create a method that returns Yes or No based on whether a password is strong:
- The length is at least 8 characters
- It contains special characters like ~!@#$%^&*()_+{}[]
- It contains at least one number
- There are lower case and uppercase letters
'''

import unittest

class Password():
    def __init__(self, password):
        self.password = password
        self.isStrong = False

    def verify_password(self):
        print("Verifying this password: {}".format(self.password))
        result = self.is_password_long_enough() and self.is_password_containing_special_characters() and self.is_password_containing_digits() and self.is_password_containing_lowercase_uppercase_letters()
        if result:
            print("==> Password is strong")
            self.isStrong = True
            return "Yes"
        else:
            print("==> Password is weak")
            return "No"

    def is_password_long_enough(self):
        print("Verify Password length")
        if len(self.password) < 8:
            return False
        else:
            return True

    def is_password_containing_special_characters(self):
        print("Verify Password contains special characters")
        special_chard = "~!@#$%^&*()_+{}[]"
        for char in self.password:
            if char in special_chard:
                return True
        return False

    def is_password_containing_digits(self):
        print("Verify Password contains numbers")
        for char in self.password:
            if char.isdigit():
                return True
        return False

    def is_password_containing_lowercase_uppercase_letters(self):
        print("Verify Password contains lowercase letters")
        lower = False
        capital = False
        for char in self.password:
            if char.islower():
                lower = True
            if char.isupper():
                capital = True
        return lower and capital



class TestSolution(unittest.TestCase):
    def test_password_is_short(self):
        print("\n*** TC: Password is short ***")
        password = Password("hello")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_special_chars(self):
        print("\n*** TC: Password without special chars ***")
        password = Password("HelloWorld")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_digit(self):
        print("\n*** TC: Password without a digit ***")
        password = Password("HelloWorld!")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_upper_char(self):
        print("\n*** TC: Password without an upper case character ***")
        password = Password("wonderful12#")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_char(self):
        print("\n*** TC: Password without any upper/lower case character ***")
        password = Password("12345!@#$#")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_no_lowercase_char(self):
        print("\n*** TC: Password without any lower case character ***")
        password = Password("MONEY12!@$")
        actual = password.verify_password()
        expected = "No"
        self.assertEqual(actual, expected)

    def test_password_is_strong(self):
        print("\n*** TC: Password with all requirements ***")
        password = Password("Foobar123$")
        actual = password.verify_password()
        expected = "Yes"
        self.assertEqual(actual, expected)