'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''

import unittest

class Solution(object):
    def matrix_spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        # Find the size of the matrix
        m = len(matrix)
        n = len(matrix[0])
        size = m * n

        result = []
        top = 0
        bottom = m-1
        left = 0
        right = n-1

        # start navigating through the matrix: right, down, left, up
        while top <= bottom and left <= right:
            # go right
            for column in range(left, right):
                result.append(matrix[top][column])
            # go down
            for row in range(top, bottom):
                result.append(matrix[row][right])
            # go left
            for column in range(right, left, -1):
                result.append(matrix[bottom][column])
            # go up
            for row in range(bottom, top, -1):
                if len(result) == size:
                    break
                result.append(matrix[row][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # what's left
        if len(result) < size:
            # fix the indexes
            left -= 1
            top -= 1
            right += 1
            bottom += 1
            for col in range(left, right+1):
                for row in range(top, bottom+1):
                    result.append(matrix[col][row])

        return result

class TestSolution(unittest.TestCase):
    def test_case_3_by_3(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        actual = Solution().matrix_spiral_order(matrix)
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(expected, actual)

    def test_case_4_by_3(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        actual = Solution().matrix_spiral_order(matrix)
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(expected, actual)

    def test_case_6_by_4(self):
        matrix = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24]]
        actual = Solution().matrix_spiral_order(matrix)
        expected = [1, 2, 3, 4, 5, 6, 12, 18, 24, 23, 22, 21, 20, 19, 13, 7, 8, 9, 10, 11, 17, 16, 15, 14]
        self.assertEqual(expected, actual)

    def test_case_3_by_5(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9],[10, 11, 12],[13, 14, 15]]
        actual = Solution().matrix_spiral_order(matrix)
        expected = [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]
        self.assertEqual(expected, actual)

    def test_case_4_by_7(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28]]
        actual = Solution().matrix_spiral_order(matrix)
        expected = [1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 27, 26, 25, 21, 17, 13, 9, 5, 6, 7, 11, 15, 19, 23, 22, 18, 14, 10]
        self.assertEqual(expected, actual)