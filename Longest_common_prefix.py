'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
import unittest

class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            print("==> No strings to check")
            return ""
        min_len = min(len(str) for str in strs)
        if min_len == 0:
            print("==> Some strings are empty")
            return ""
        same_prefix = ""
        columns_count = 0
        for columns in zip(*strs):
            if columns_count > min_len:
                if len(same_prefix) > 0:
                    print("==> Same prefix found! {}".format(same_prefix))
                return same_prefix
            if self.verify_elements_same_in_set(columns) is False:
                if len(same_prefix) > 0:
                    print("==> Same prefix found: {}".format(same_prefix))
                else:
                    print("==> No common prefix")
                return same_prefix
            same_prefix = same_prefix + columns[0]
            columns_count += 1
        print("==> Same prefix: {}".format(same_prefix))
        return same_prefix

    def verify_elements_same_in_set(self, array):
        # print("Verify set {}".format(array))
        result = False
        ch_to_check = array[0]
        for i in range(1, len(array)):
            if array[i] != ch_to_check:
                return result
        return True


class TestSolution(unittest.TestCase):
    def test_case_few_strings(self):
        print("\n*** TC: Few first characters are the same")
        strs = ["flower", "flow", "flight"]
        result = Solution().longest_common_prefix(strs)
        expected = "fl"
        self.assertEqual(result, expected)

    def test_case_one_string_empty(self):
        print("\n*** TC: One string is empty")
        strs = ["flower", "", "flight"]
        result = Solution().longest_common_prefix(strs)
        expected = ""
        self.assertEqual(result, expected)

    def test_case_all_strings_have_different_characters(self):
        print("\n*** TC: All strings have different characters")
        strs = ["dog","racecar","car"]
        result = Solution().longest_common_prefix(strs)
        expected = ""
        self.assertEqual(result, expected)

    def test_case_all_strings_are_same(self):
        print("\n*** TC: All strings are the same")
        strs = ["car","car","car"]
        result = Solution().longest_common_prefix(strs)
        expected = "car"
        self.assertEqual(result, expected)

    def test_case_same_root(self):
        print("\n*** TC: Strings have the same root")
        strs = ["payment","payless","pay", "pays"]
        result = Solution().longest_common_prefix(strs)
        expected = "pay"
        self.assertEqual(result, expected)