'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
'''

import  unittest

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        resultRows = self.verifyRowsValid(board)
        resultColumns = self.verifyColumnsValid(board)
        resultsSquare = self.verifyBoxsValid(board)
        return resultRows and resultColumns and resultsSquare

    def verifyRowsValid(self, board):
        print("Verify rows")
        for row in board:
            if len(row) != 9:
                return False
            if not self.verifySet(row):
                return False
        print("==> Rows are OK!")
        return True


    def verifyColumnsValid(self, board):
        print("Verify columns")
        for columns in zip(*board):
            if len(columns) != 9:
                return False
            if not self.verifySet(columns):
                return False
        print("==> Columns are OK!")
        return True


    def verifyBoxsValid(self, board):
        print("Verify boxs")
        square = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        square.append(board[k][l])
                if not self.verifySet(square):
                    return False
                square = []
        print("==> Squares are OK!")
        return True


    def verifySet(self, array):
        print("Verify set {}".format(array))
        uniqueNumbers = []
        for i in range(len(array)):
            if array[i] == ".":
                continue
            if not (1 <= int(array[i]) <= 9):
                print("===> !!! Not a correct number! ", int(array[i]))
                return False
            if array[i] in uniqueNumbers:
                print("===> !!! Duplicate! ", int(array[i]))
                return False
            else:
                uniqueNumbers.append(array[i])
        print("===> Set is OK!")
        return True


class TestSudoku(unittest.TestCase):
    def test_case_valid(self):
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        expected = True
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_case_dup_in_square(self):
        board = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        expected = False
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_case_duplicate_in_row(self):
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".","1","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        expected = False
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)