'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''

import unittest

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)

class TestSolution(unittest.TestCase):
    def test_case_target_exists(self):
        nums = [1,3,5,6]
        target = 5
        expected = 2
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(actual, expected)

    def test_case_target_to_insert_in_the_middle(self):
        nums = [1,3,5,6]
        target = 2
        expected = 1
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(actual, expected)

    def test_case_target_to_insert_in_at_the_end(self):
        nums = [1,3,5,6]
        target = 7
        expected = 4
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(actual, expected)

    def test_case_target_to_insert_at_the_beginning(self):
        nums = [1,3,5,6]
        target = 0
        expected = 0
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(actual, expected)