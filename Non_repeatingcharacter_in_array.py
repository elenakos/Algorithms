'''
Implement an algorithm to find a non-repeating character in an array.
'''
import unittest

class Arrays:
    def __init__(self, arr):
        self.array = arr

    def find_non_repeating_char_in_array(self):
        print()
        stat = {}
        for i in self.array:
            if i in stat:
                stat[i] += 1
            else:
                stat[i] = 1

        result = []
        for k, v in stat.items():
            if v == 1:
                result.append(k)
        print(f'The non-repeating character is: {result}')
        return result


class TestArrays(unittest.TestCase):
    def test_one_unique_char_int(self):
        print("\n*** TC: One unique character in an array of integers ***")
        arr = Arrays([1, 1, 2, 1, 5, 2, 3, 3, 3])
        expected = [5]
        actual = arr.find_non_repeating_char_in_array()
        self.assertEqual(expected, actual)

    def test_one_unique_char_char(self):
        print("\n*** TC: One unique character in an array of characters ***")
        s = "mom"
        arr = Arrays(list(s))
        expected = ["o"]
        actual = arr.find_non_repeating_char_in_array()
        self.assertEqual(expected, actual)

    def test_one_unique_char_word(self):
        print("\n*** TC: One unique character in an array of words ***")
        s = "Hello World World"
        arr = Arrays(s.split())
        expected = ["Hello"]
        actual = arr.find_non_repeating_char_in_array()
        self.assertEqual(expected, actual)