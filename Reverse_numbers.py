'''
Given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k.
If a day's value is a beautiful number, it is a beautiful day.
Return the number of beautiful days in the range.

Sample Input
[20 23]
k = 6

Sample Output
2

Explanation:
Day 20 is beautiful because the following evaluates to a whole number: |20-2|/6 = 18/6 = 3

'''

import unittest

class Solution:
    def find_beautiful_days(self, array, k):
        #print("Find days |i - reverse(i)| is evenly divisible by {}".format(k))
        beautiful_days = []
        for i in range(len(array)):
            if not isinstance(array[i], int):
                continue
            if self.is_day_beautiful(array[i], k):
                beautiful_days.append(array[i])
        return len(beautiful_days)

    def is_day_beautiful(self, number, k):
        #print("Check if |i - reverse(i)| is evenly divisible by k.")
        result = False
        number_string = str(number)
        reverse_number_string = number_string[::-1]
        if int(reverse_number_string[0]) == 0:
            reverse_number_string = reverse_number_string[1:]
        reverse_number = int(reverse_number_string)
        result = abs(number - reverse_number) % k == 0
        return result


class SolveSolution(unittest.TestCase):
    def test_all_elements_are_beautiful(self):
        print("\n*** TC: All elements are beautiful days ***")
        arr = [20, 22]
        k = 6
        expected = 2
        actual = Solution().find_beautiful_days(arr, k)
        self.assertEqual(expected, actual)

    def test_one_element_is_beautiful(self):
        print("\n*** TC: One element is a beautiful day ***")
        arr = [20, 21]
        k = 6
        expected = 1
        actual = Solution().find_beautiful_days(arr, k)
        self.assertEqual(expected, actual)

    def test_one_element_same_as_reversed(self):
        print("\n*** TC: One element the same digits ***")
        arr = [20, 22222]
        k = 3
        expected = 2
        actual = Solution().find_beautiful_days(arr, k)
        self.assertEqual(expected, actual)

    def test_no_beautiful_day(self):
        print("\n*** TC: No beautiful days ***")
        arr = [30, 17, 23654]
        k = 5
        expected = 0
        actual = Solution().find_beautiful_days(arr, k)
        self.assertEqual(expected, actual)

    def test_one_element_id_word(self):
        print("\n*** TC: One element is a word ***")
        arr = [20, 23, "Hello!"]
        k = 3
        expected = 2
        actual = Solution().find_beautiful_days(arr, k)
        self.assertEqual(expected, actual)