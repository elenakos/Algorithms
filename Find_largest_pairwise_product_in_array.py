'''
Find a max pairwise product ina give array of positive numbers
Example 1:
Input: nums = [1,3,5,0]
Output: 15 as a product of two biggest numbers of 3 and 5
'''

import unittest

class Solution:
    def maxPairwiseProduct(self, nums):
        print("\nReturn a max product of elements in an array: {}".format(nums))
        if len(nums) == 0:
            print("==> The list is empty")
            return 0
        if len(nums) == 1:
            print("==> Too short")
            return nums[0]
        # Navigate through the array and find two biggest numbers
        maxValueIndex1 = -1
        maxValueIndex2 = -1

        for i in range(len(nums)):
            if nums[i] > nums[maxValueIndex1] or maxValueIndex1 == -1:
                maxValueIndex1 = i
            if (nums[i] >= nums[maxValueIndex2] or maxValueIndex2 == -1) and i != maxValueIndex1:
                maxValueIndex2 = i

        print("==> Two largest numbers are {} and {} with indexes {} and {}".format(nums[maxValueIndex1], nums[maxValueIndex2], maxValueIndex1, maxValueIndex2))
        return nums[maxValueIndex1] * nums[maxValueIndex2]


class TestSolution(unittest.TestCase):
    def test_case_biggest_element_first(self):
        array = [4, 2, 3, 1]
        expected = 12
        actual = Solution().maxPairwiseProduct(array)
        self.assertEqual(expected, actual)

    def test_case_empty(self):
        array = []
        expected = 0
        actual = Solution().maxPairwiseProduct(array)
        self.assertEqual(expected, actual)

    def test_case_one_element(self):
        array = [1]
        expected = 1
        actual = Solution().maxPairwiseProduct(array)
        self.assertEqual(expected, actual)

    def test_case_same_elements(self):
        array = [1, 5, 3, 4, 5]
        expected = 25
        actual = Solution().maxPairwiseProduct(array)
        self.assertEqual(expected, actual)

    def test_case_random_order(self):
        array = [1, 5, 3, 4, 0]
        expected = 20
        actual = Solution().maxPairwiseProduct(array)
        self.assertEqual(expected, actual)