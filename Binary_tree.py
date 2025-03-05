'''
This file contains implementations of basic operations with binary trees:
- traverse, delete, insert, search, height calculation
'''

import unittest

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, righ=None):
         self.val = val
         self.left = left
         self.right = righ

class BinaryTree():
    def __init__(self):
        self.root = None

    def create_binary_tree_from_array(self, array):
        if not array:
            return []

        self.root = TreeNode(array[0])
        nodes = [self.root]
        i = 1
        while i < len(array):
            parent = nodes.pop(0)
            if i < len(array):
                if array[i] is not None:
                    parent.left = TreeNode(array[i])
                    nodes.append(parent.left)
                i += 1
            if i < len(array):
                if array[i] is not None:
                    parent.right = TreeNode(array[i])
                    nodes.append(parent.right)
                i += 1
        return self.root


    def travers_tree(self, node, result=[]):
        if node:
            self.travers_tree(node.left, result)
            print(node.val, " ")
            result.append(node.val)
            self.travers_tree(node.right, result)


    def return_root_to_leaf_path(self):
        print("Return all leaf paths")


class TestBinaryTree(unittest.TestCase):
    def test_travers_tree(self):
        print("\n*** TC: Test traversing a tree")
        '''
           1
          / \
         2   3
          \
           5
        '''
        arr = [1, 2, 3, None, 5]
        binary_tree = BinaryTree()
        root = TreeNode()
        root = binary_tree.create_binary_tree_from_array(arr)
        result = []
        binary_tree.travers_tree(root, result)
        expected = [2, 5, 1, 3]
        self.assertEqual(result, expected)

    def test_create_binary_tree_from_array(self):
        print("\n*** TC: Test creating a binary tree")
        '''
              1
             / \
            2   3
           / \   \
          4   5   6
        '''
        arr = [1, 2, 3, 4, 5, None, 6]
        binary_tree = BinaryTree()
        root = TreeNode()
        root = binary_tree.create_binary_tree_from_array(arr)
        result = []
        binary_tree.travers_tree(root, result)
        expected = [4, 2, 5, 1, 3, 6]
        self.assertEqual(result, expected)
