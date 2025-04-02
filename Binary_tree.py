'''
This file contains implementations of basic operations with binary trees:
- traverse, delete, insert, search, height calculation
'''

import unittest

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class BinaryTree():
    def __init__(self):
        self.root = None

    def create_binary_tree_from_array(self, array):
        '''
        The first element (index 0) becomes the root node.
        The next two elements (indices 1 and 2) become the left and right children of the root.
        The following elements (indices 3, 4, 5, 6) become the left and right children of the second level nodes, and so on.
        '''
        print("Creating a binary tree from array")
        if not array:
            return []

        self.root = TreeNode(array[0])
        nodes = [self.root]
        # Start with the children
        i = 1
        while i < len(array):
            parent = nodes.pop(0)
            if i < len(array):
                # Go left
                if array[i] is not None:
                    parent.left = TreeNode(array[i])
                    nodes.append(parent.left)
                i += 1
            if i < len(array):
                # Go right
                if array[i] is not None:
                    parent.right = TreeNode(array[i])
                    nodes.append(parent.right)
                i += 1
        return self.root


    def travers_tree(self, node, result=[]):
        '''
        - Visit the left subtree.
        - Visit the root node.
        - Visit the right subtree.
        '''
        #print("Traversing a binary tree - recursively - depth-first")
        if node:
            self.travers_tree(node.left, result)
            #print(node.val, " ")
            result.append(node.val)
            self.travers_tree(node.right, result)

    def find_element_in_tree(self, node, val):
        #print("Find an element in a binary tree")
        if not node:
            return False
        if node.val == val:
            return True
        return self.find_element_in_tree(node.left, val) or self.find_element_in_tree(node.right, val)


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

    def test_traverse_binary_tree_from_array_four_levels(self):
        print("\n*** TC: Test creating a binary tree - 4 levels")
        '''
                 1
                / \
               2   3
              / \   \
             4   5   7
            /   /
           8   10
        '''
        arr =  [1, 2, 3, 4, 5, None, 7, 8, None, 10]
        binary_tree = BinaryTree()
        root = TreeNode()
        root = binary_tree.create_binary_tree_from_array(arr)
        result = []
        binary_tree.travers_tree(root, result)
        expected = [8, 4, 2, 10, 5, 1, 3, 7]
        self.assertEqual(result, expected)

    def test_find_element_in_tree(self):
        print("\n*** TC: Test find an element in a binary tree")
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
        expected = True
        actual = binary_tree.find_element_in_tree(root, 3)
        self.assertEqual(actual, expected)