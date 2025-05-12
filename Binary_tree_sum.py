'''
Given an array [root value, direction (L/R), child value, direction (L/R), child value]
Verify if a tree has a sum of root+child that equals to a specific number
   10
  /  \
 20  30

'''

import unittest
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class BinaryTreeSmall(object):
    def __init__(self):
        self.root = None
        self.definedNode = {}

    def build_the_tree(self, arr):
        print("Let's build a tree")
        if arr is None:
            self.root = None

        self.root = TreeNode(arr[0])
        self.definedNode[arr[0]] = arr[0]
        for i in range(1, len(arr), 2):
            if arr[i] == "L":
                left_child = TreeNode(arr[i+1])
                self.root.left = left_child
                self.definedNode[arr[i+1]] = left_child
            if arr[i] == "R":
                right_child = TreeNode(arr[i+1])
                self.root.right = right_child
                self.definedNode[arr[i+1]] = right_child


    def check_sum(self, sum):
        print("Let's check the sum of nodes")
        if self.root is None:
            return 0
        if self.root.left is not None:
            if self.root.val + self.root.left.val == sum:
                print("==> The solution is on the left")
                return 1
        if self.root.right is not None:
            if self.root.val + self.root.right.val == sum:
                print("==> The solution is on the right")
                return 1
        print("==> There is no solution")
        return 0

class TestSolution(unittest.TestCase):
    def test_left(self):
        print("\n*** TC: The solution is on the left side of the tree")
        arr = [10, "L", 20, "R", 30]
        binary_tree = BinaryTreeSmall()
        binary_tree.build_the_tree(arr)
        sum = 30
        expected = 1
        actual = binary_tree.check_sum(sum)
        self.assertEqual(expected, actual)

    def test_right(self):
        print("\n*** TC: The solution is on the right side of the tree")
        arr = [10, "L", 20, "R", 30]
        binary_tree = BinaryTreeSmall()
        binary_tree.build_the_tree(arr)
        sum = 40
        expected = 1
        actual = binary_tree.check_sum(sum)
        self.assertEqual(expected, actual)

    def test_no_solution(self):
        print("\n*** TC: No solution")
        arr = [10, "L", 20, "R", 30]
        binary_tree = BinaryTreeSmall()
        binary_tree.build_the_tree(arr)
        sum = 50
        expected = 0
        actual = binary_tree.check_sum(sum)
        self.assertEqual(expected, actual)