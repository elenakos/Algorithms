'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

import unittest

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print("\nFind sets of three that sums to 0 {}".format(nums))
        results = []
        if len(nums) < 3:
            print("==> The given array is too short")
            return results
        nums.sort()
        print("--> Sorted list: {}".format(nums))

        # Navigate through the sorted array to find a set of three elements that sums to 0
        # Keep track of three indices
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    print("==> Found {}-{}-{}".format(i, j, k))
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        print("*** Debug: {}-{}-{}".format(nums[j], j, k))
                        j += 1

        return results



class TestSolution(unittest.TestCase):
    def test_case_two_solutions(self):
        array = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]
        actual = Solution().threeSum(array)
        self.assertEqual(expected, actual)

    def test_only_three_elements_no_solution(self):
        array = [0,1,1]
        expected = []
        actual = Solution().threeSum(array)
        self.assertEqual(expected, actual)

    def test_three_zero_elements_same_solution(self):
        array = [0, 0, 0]
        expected = [[0, 0, 0]]
        actual = Solution().threeSum(array)
        self.assertEqual(expected, actual)

    def test_array_too_short_no_solution(self):
        array = [0, 2]
        expected = []
        actual = Solution().threeSum(array)
        self.assertEqual(expected, actual)