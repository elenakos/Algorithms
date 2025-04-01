'''
array1 = [1, 2, 3]
array2 = [1, 4, 5, 6]
merged_list  = [1, 1, 2, 3, 4, 5, 6]
'''

import unittest

class Solution():
    def merge_two_lists(self, list1, list2):
        if len(list1) == 0:
            return list2
        if len(list2) == 0:
            return list1

        # Define a merged list and counters
        len1 = len(list1)
        len2 = len(list2)
        merged_list = []
        counter1 = 0
        counter2 = 0
        while counter1 < len1 and counter2 < len2:
            if list1[counter1] == list2[counter2]:
                merged_list.append(list1[counter1])
                counter1 += 1
                merged_list.append(list2[counter2])
                counter2 += 1
            elif list1[counter1] < list2[counter2]:
                merged_list.append(list1[counter1])
                counter1 += 1
            else:
                merged_list.append(list2[counter2])
                counter2 += 1

         # Add the end of the longer array to the end of the merged list
        if counter1 == len1:
            merged_list.extend(list2[counter2:])
        if counter2 == len2:
            merged_list.extend(list1[counter1:])

        return merged_list


class TestSolution(unittest.TestCase):
    def test_case_first_array_is_shorted(self):
        array1 = [1, 2, 3]
        array2 = [1, 4, 5, 6]
        expected = [1, 1, 2, 3, 4, 5, 6]
        actual = Solution().merge_two_lists(array1, array2)
        self.assertEqual(expected, actual)

    def test_case_second_array_is_shorter(self):
        array1 = [1, 5, 6, 7]
        array2 = [1, 2]
        expected = [1, 1, 2, 5, 6, 7]
        actual = Solution().merge_two_lists(array1, array2)
        self.assertEqual(expected, actual)

    def test_case_arrays_not_overlapping(self):
        array1 = [1, 5, 6, 7]
        array2 = [10, 20]
        expected = [1, 5, 6, 7, 10, 20]
        actual = Solution().merge_two_lists(array1, array2)
        self.assertEqual(expected, actual)

    def test_case_one_array_empty(self):
        array1 = []
        array2 = [10, 20]
        expected = [10, 20]
        actual = Solution().merge_two_lists(array1, array2)
        self.assertEqual(expected, actual)

    def test_case_second_array_empty(self):
        array1 = [15]
        array2 = []
        expected = [15]
        actual = Solution().merge_two_lists(array1, array2)
        self.assertEqual(expected, actual)