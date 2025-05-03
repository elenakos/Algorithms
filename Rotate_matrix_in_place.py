'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
import unittest

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        if m != n:
            print("==> Cannot rotate matrix")
            return matrix
        # Rotate in place one square layer in a time; needs to be done only for a half of rows
        for i in range(m//2):
            for j in range(i, m-i-1):
                # Save the first
                temp = matrix[i][j]
                # Do the swap 4 times for each cell
                # From bottom-left -> all the way up
                matrix[i][j] = matrix[n-j-1][i]
                # From bottom-right -> all the way left
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                # From top-right all the way down
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                # Top-right gets a saved temp value
                matrix[j][n-i-1] = temp
        return matrix



class TestSolution(unittest.TestCase):
    def test_case_rotate_2_by_2_matrix(self):
        print("\n*** TC: Rotate 2x2 matrix")
        matrix = [[1,2],[3,4]]
        expect = [[3,1],[4,2]]
        actual = Solution().rotate(matrix)
        self.assertEqual(expect, actual)

    def test_case_rotate_3_by_3_matrix(self):
        print("\n*** TC: Rotate 3x3 matrix")
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expect = [[7,4,1],[8,5,2],[9,6,3]]
        actual = Solution().rotate(matrix)
        self.assertEqual(expect, actual)

    def test_case_rotate_4_by_4_matrix(self):
        print("\n*** TC: Rotate 4x4 matrix")
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expect = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        actual = Solution().rotate(matrix)
        self.assertEqual(expect, actual)

    def test_case_rotate_2_by_3_matrix(self):
        print("\n*** TC: Rotate 2x3 matrix, and it should not be able to rotate matrix")
        matrix = [[1,2],[4,5],[7,8]]
        expect = [[1,2],[4,5],[7,8]]
        actual = Solution().rotate(matrix)
        self.assertEqual(expect, actual)