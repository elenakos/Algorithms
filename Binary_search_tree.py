'''
Properties of a Binary Search Tree:
- Each node has at most two children: A node can have zero, one, or two children.
- Ordering property:
   - The value of the left child of a node is less than the value of the node itself.
   - The value of the right child of a node is greater than the value of the node itself.
- No duplicate values: Typically, a BST does not contain duplicate values.

The key advantage of a BST is that it allows for efficient searching, insertion, and deletion of data.

'''

import unittest

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def all_none(lst):
    return all(x is None for x in lst)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def sorted_array_to_BST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        # Find a middle element to be a root/node
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        # Keep creating left and right subtrees
        node.left = self.sorted_array_to_BST(nums[:mid])
        node.right = self.sorted_array_to_BST(nums[mid + 1:])

        return node

    def traverse_BST(self,  node, result):
        if node:
            # keep going left  then right
            self.traverse_BST(node.left, result)
            result.append(node.val)
            self.traverse_BST(node.right, result)

    def search_BST(self, root, target):
        if root is None:
            print("==> No more nodes to check left")
            return False

        if root.val == target:
            print("==> A value is found")
            return True
        elif target < root.val:
            return self.search_BST(root.left, target)
        else:
            return self.search_BST(root.right, target)

    def insert_value_into_binary_search_tree(self, root, value):
           if not root:
               # Create a new node if a tree is missing
               return TreeNode(value)
           if value < root.val:
               # Search-insert on the left (smaller) subtree
               root.left = self.insert_value_into_binary_search_tree(root.left, value)
           elif value > root.val:
               # Search-insert on the right (larger) subtree
               root.right = self.insert_value_into_binary_search_tree(root.right, value)
           else:
               # Deal with a duplicate - let's add it to the left
               root.left = self.insert_value_into_binary_search_tree(root.left, root.val)
               pass

           return root

    def create_array_from_BST(self, root):
        # Create an array that can be used to construct a binary tree
        # including None for missing "children"
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            # current level size and all its elements
            level_size = len(queue)
            current_level_nodes = []
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    current_level_nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    current_level_nodes.append(None)
                    queue.append(None)
                    queue.append(None)

            # Remove None from the end
            while current_level_nodes and current_level_nodes[-1] is None:
                current_level_nodes.pop()
            result.extend(current_level_nodes)
            if all_none(current_level_nodes):
                break
        return result


class TestBinarySearchTree(unittest.TestCase):
    def test_create_bst_from_array_and_traverse_it(self):
        print("\n*** TC: Test creating a BST from an array and then traversing it")
        """
               0
              / \
            -3   9
            /   /
        -10    5
        """
        nums = [-10, -3, 0, 5, 9]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        result = []
        bst.traverse_BST(root, result)
        expected = [-10, -3, 0, 5, 9]
        self.assertEqual(expected, result)

    def test_create_an_array_from_bst(self):
        print("\n*** TC: Test creating an array from a BST - 3 levels")
        """
               0
              / \
            -3   9
            /   /
        -10    5
        """
        nums = [-10, -3, 0, 5, 9]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        actual = bst.create_array_from_BST(root)
        expected = [0,-3,9,-10, None,5]
        self.assertEqual(expected, actual)

    def test_create_an_array_from_bst_short(self):
        print("\n*** TC: Test creating an array from a BST - just 2 elements")
        """
               3
              /
             1
        """
        nums = [1,3]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        actual = bst.create_array_from_BST(root)
        expected = [3, 1]
        self.assertEqual(expected, actual)

    def test_search_and_find(self):
        print("\n*** TC: Search and find a node in a BST")
        """
        """
        nums = [-25, -10, -5, -3, -1, 0, 5, 6, 9, 1, 17, 23]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        actual = bst.search_BST(root, 5)
        expected = True
        self.assertEqual(expected, actual)

    def test_search_and_do_not_find(self):
        print("\n*** TC: Search and find a node in a BST")
        """
        """
        nums = [-25, -10, -5, -3, -1, 0, 5, 6, 9, 1, 17, 23]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        actual = bst.search_BST(root, 33)
        expected = False
        self.assertEqual(expected, actual)

    def test_insert_a_new_node(self):
        print("\n*** TC: Insert a new node in a BST")
        """
        """
        nums = [-25, -10, -5, -3, -1, 0, 5, 6, 9, 1, 17, 23]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        root = bst.insert_value_into_binary_search_tree(root, 3)
        result = []
        bst.traverse_BST(root, result)
        expected = [-25, -10, -5, -3, -1, 0, 3, 5, 6, 9, 1, 17, 23]
        self.assertEqual(expected, result)

    def test_s_duplicte_node(self):
        print("\n*** TC: Insert a duplicate node in a BST")
        """
        """
        nums = [-25, -10, -5, -3, -1, 0, 5, 6, 9, 1, 17, 23]
        bst = BinarySearchTree()
        root = bst.sorted_array_to_BST(nums)
        root = bst.insert_value_into_binary_search_tree(root, 5)
        result = []
        bst.traverse_BST(root, result)
        expected = [-25, -10, -5, -3, -1, 0, 5, 5, 6, 9, 1, 17, 23]
        self.assertEqual(expected, result)