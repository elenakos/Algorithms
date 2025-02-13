'''
Remove duplicates in a given array in-place
Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("Remove duplicates in-place from {} and return the number of unique elements".format(nums))
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        print("==> Final array with {} first unique number(s): {}".format(j, nums))
        return j

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected = 5
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)

    def test_case_all_same_values(self):
        nums = [0,0,0,0]
        expected = 1
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)

