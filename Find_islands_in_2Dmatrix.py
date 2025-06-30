'''
Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent
to another cell if they are next to each either on the same row or column.
Note that two values of 1 are not part of the same island if they’re sharing only a mutual "corner" (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.
binaryMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]

Answer = 6
'''
def get_number_of_islands(binaryMatrix) -> int:
    r, c = len(binaryMatrix), len(binaryMatrix[0])
    print("\nFind a number of islands in {}x{} matrix".format(r, c))
    def dfs(row, col):
        if row < 0 or row >= r or col < 0 or col >= c or binaryMatrix[row][col] == 0:
            return
        # Replace the current element with 0 so no repeat searches will be done
        binaryMatrix[row][col] = 0
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)

    answer = 0
    for i in range(r):
        for j in range(c):
            if binaryMatrix[i][j] == 1:
                dfs(i, j)
                answer += 1
    print("==> Number of islands: {}".format(answer))
    return answer


import unittest

class TestSolution(unittest.TestCase):
    def test_5x5_matrix_6(self):
        binaryMatrix = [
            [0, 1, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(get_number_of_islands(binaryMatrix), 6)

    def test_5x5_matrix_5(self):
        binaryMatrix = [
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(get_number_of_islands(binaryMatrix), 5)

    def test_2x3_matrix_1(self):
        binaryMatrix = [
            [0,  0],
            [0,  1]
        ]
        self.assertEqual(get_number_of_islands(binaryMatrix), 1)

    def test_5x2_matrix_1(self):
        binaryMatrix = [
            [0, 1],
            [0, 1],
            [1, 0],
            [0, 0],
            [1, 1]
        ]
        self.assertEqual(get_number_of_islands(binaryMatrix), 3)

    def test_1x1_matrix_1(self):
        binaryMatrix = [
            [0]
        ]
        self.assertEqual(get_number_of_islands(binaryMatrix), 0)