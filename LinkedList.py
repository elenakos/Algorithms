'''
This file contains implementation of basic operations with linked lists:
- append, prepend, insert, delete, traverse
- reverse, find a middle node, find n-th mode
- sort, rotate to the right by k-place
'''
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        print("Verify if the list is empty")
        return self.head is None

    def prepend(self, item):
        print("Add item to the beginning of the list")
        temp = ListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        #print("Add item to the end of the list")
        temp = ListNode(item)
        temp.setData(item)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(temp)

    def size(self):
        print("Get the size of the list")
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def delete_item_in_position(self, pos):
        print("Delete item in a specific position")
        if pos < 0 or pos > self.size() - 1:
            return
        if pos == 0:
            self.head = self.head.getNext()
            return
        current = self.head
        count = 0
        while count < pos-1:
            count += 1
            current = current.getNext()
        next = current.getNext()
        next1 = next.getNext()
        current.setNext(next1)

    def insert(self, pos, item):
        print("Insert item at position %d" % pos)
        if pos > self.size() - 1 or pos < 0:
            raise IndexError("Index out of range")
        if pos == 0:
            self.prepend(item)
        else:
            if pos == self.size() - 1:
                self.append(item)
            else:
                temp = ListNode(item)
                temp.setData(item)
                count = 0
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.getNext()
                temp.setNext(current.getNext())
                current.setNext(temp)

    def create_list_from_array(self, array):
        print("Create list from array {}".format(array))
        for i in array:
            self.append(i)
        return self

    def create_list_as_array(self):
        myArray = []
        current = self.head
        while current is not None:
            myArray.append(current.getData())
            current = current.getNext()
        return myArray

    def find_element(self, item):
        print("Find element %d and return its position" % item)
        current = self.head
        count = 0
        while current is not None:
            if current.getData() == item:
                return count
            count += 1
            current = current.getNext()
        return -1

    def return_n_element_from_list(self, position):
        print("Return n element from list position %d" % position)
        if position > self.size() - 1:
            return None
        if position == 0:
            return self.head
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
            if count == position:
                return current.getData()
        return None


    def reverse_list(self, head):
        print("Reverse the list")
        # Keep track of previous, current, next
        previous = None
        current = head
        while current is not None:
            next = current.getNext()
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def rotate_right(self, head, k):
        print("Rotate right by %d element" % k)
        list_size = self.size()
        if k == 0:
            return
        if k > list_size - 1:
            return
        if head is None:
            return
        # Find the last element
        tail = head
        i = 0
        while i < list_size - 1:
            tail = tail.getNext()
            i += 1
        # Find the K-element, point the past element tp a head, and make k-elements as a head
        current = head
        while k > 0:
            current = current.getNext()
            k -= 1
        tail.next = head
        self.head = current.next
        current.next = None

    def is_palindrome(self):
        print("Check if a linked list is a palindrome")
        list = self.create_list_as_array()
        left = 0
        right = len(list) - 1
        while left <= right:
            if list[left] != list[right]:
                return False
            left += 1
            right -= 1
        return True

    def sort_list(self):
        print("Sort the list")
        # Create an array out of a list
        my_array = self.create_list_as_array()
        # Sort the array
        array_size = len(my_array)
        for i in range(array_size-1, 0, -1):
            for j in range(i):
                if my_array[j] > my_array[j+1]:
                    my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
        print("=== Sored array: ", my_array)
        # Create a new list from an array
        self.head = None
        self.create_list_from_array(my_array)

    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        print("Merge two sorted lists")
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Create a new head
        newHead = current = ListNode()
        current1 = list1.head
        current2 = list2.head

        # Traverse lists and attach elements from both links in order to a new head
        while current1 and current2:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        # In case one list is longer than the other:
        if current1:
            current.next = current1
        if current2:
            current.next = current2
        return newHead.next

    @staticmethod
    def traverse_list_from_head_return_array(head):
        print("Traverse the list")
        my_array = []
        current = head
        while current is not None:
            my_array.append(current.getData())
            current = current.next
        return my_array

    def remove_duplicates_from_sorted_list(self):
        print("Remove duplicate elements")
        if self.head is None:
            return
        current = self.head
        seen = set()
        seen.add(current.getData())
        previous = current
        current = current.next

        while current:
            if current.getData() in seen:
                previous.next = current.next
            else:
                seen.add(current.getData())
                previous = current
            current = current.next
        print("Done!")


class TestUnorderedList(unittest.TestCase):
    def test_remove_duplicates_from_list(self):
        print("\nTest remove duplicate elements")
        array = [1, 2, 2, 3]
        mylist = UnorderedList()
        mylist.create_list_from_array(array)
        expected_list = [1, 2, 3]
        mylist.remove_duplicates_from_sorted_list()
        actual_list = mylist.create_list_as_array()
        self.assertEqual(expected_list, actual_list)

    def test_remove_duplicates_in_head_from_list(self):
        print("\nTest remove duplicate elements")
        array = [1, 1, 1, 2, 2, 3, 4, 3]
        mylist = UnorderedList()
        mylist.create_list_from_array(array)
        expected_list = [1, 2, 3, 4]
        mylist.remove_duplicates_from_sorted_list()
        actual_list = mylist.create_list_as_array()
        self.assertEqual(expected_list, actual_list)


    def test_merge_two_lists(self):
        print("\n*** TC: Merge two lists")
        list1 = UnorderedList()
        array1 = [1, 2, 3]
        list1.create_list_from_array(array1)
        list2 = UnorderedList()
        array2 = [1, 4, 5, 6]
        list2.create_list_from_array(array2)
        merged_list = UnorderedList()
        expected_list = [1, 1, 2, 3, 4, 5, 6]
        actual_list = merged_list.merge_two_sorted_lists(list1, list2)
        actual_array = UnorderedList().traverse_list_from_head_return_array(actual_list)
        self.assertEqual(expected_list, actual_array)

    def test_merge_two_lists_no_overlap(self):
        print("\n*** TC: Merge two lists with no over-lapping")
        list1 = UnorderedList()
        array1 = [1, 2, 3]
        list1.create_list_from_array(array1)
        list2 = UnorderedList()
        array2 = [15, 25, 65, 70, 80]
        list2.create_list_from_array(array2)
        merged_list = UnorderedList()
        expected_list = [1, 2, 3, 15, 25, 65, 70, 80]
        actual_list = merged_list.merge_two_sorted_lists(list1, list2)
        actual_array = UnorderedList().traverse_list_from_head_return_array(actual_list)
        self.assertEqual(expected_list, actual_array)

    def test_merge_two_lists_one_empty(self):
        print("\n*** TC: Merge two lists when one list is empty")
        list1 = UnorderedList()
        array1 = []
        list1.create_list_from_array(array1)
        list2 = UnorderedList()
        array2 = [1, 4, 5, 6]
        list2.create_list_from_array(array2)
        merged_list = UnorderedList()
        expected_list = [1, 4, 5, 6]
        actual_list = merged_list.merge_two_sorted_lists(list1, list2)
        actual_array = UnorderedList().traverse_list_from_head_return_array(actual_list)
        self.assertEqual(expected_list, actual_array)

    def test_case_sort_a_list(self):
        print("\n*** TC: Sort a list")
        my_array = [100, 2, -33, 44, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(my_array)
        mylist.sort_list()
        expected = [-33, 2, 5, 44, 100]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_verify_if_palindrome(self):
        print("\n*** TC: Verify if a linked list is a palindrome")
        myArray = [1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        expected = False
        actual = mylist.is_palindrome()
        self.assertEqual(expected, actual)

    def test_rotate_list(self):
        print("\n*** TC: Rotate the list")
        myArray = [1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        myHead = ListNode()
        myHead = mylist.return_n_element_from_list(0)
        mylist.rotate_right(myHead, 2)
        expected = [4, 5, 1, 2, 3]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_prepend_an_empty_list(self):
        print("\n*** TC: Prepend an empty list")
        mylist = UnorderedList()
        mylist.prepend(1)
        expected = [1]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_prepend_a_list(self):
        print("\n*** TC: Prepend a list")
        mylist = UnorderedList()
        mylist.prepend(1)
        mylist.prepend(0)
        expected = [0, 1]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_append_a_list(self):
        print("\n*** TC: Append a list")
        myArray = [0]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.append(1)
        expected = [0, 1]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_check_if_empty(self):
        print("\n*** TC: Check if a list is empty")
        mylist = UnorderedList()
        expected = True
        actual = mylist.is_empty()
        self.assertEqual(expected, actual)

    def test_array_to_list(self):
        print("\n*** TC: Array to list")
        myArray = [0, 1, 2, 3, 4, 5]
        mylist = UnorderedList()
        actual = mylist.create_list_from_array(myArray)
        expected = myArray
        self.assertEqual(expected, actual.create_list_as_array())

    def test_insert_node_in_the_middle(self):
        print("\n*** TC: Insert node in a middle")
        myArray = [0, 1, 2, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.insert(3, 3)
        expected = [0, 1, 2, 3, 4, 5]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_insert_node_as_a_head(self):
        print("\n*** TC: Insert node as a head")
        myArray = [1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.insert(0, 0)
        expected = [0, 1, 2, 3, 4, 5]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_insert_node_at_the_end(self):
        print("\n*** TC: Insert node at the end")
        myArray = [1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.insert(4, 6)
        expected = [1, 2, 3, 4, 5, 6]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_delete_node_in_position(self):
        print("\n*** TC: Delete a node in a position")
        myArray = [0, 1, 2, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.delete_item_in_position(3)
        expected = [0, 1, 2, 3, 4, 5]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_delete_head_node(self):
        print("\n*** TC: Delete a head node")
        myArray = [0, 1, 2, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.delete_item_in_position(0)
        expected = [1, 2, 2, 3, 4, 5]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_delete_last(self):
        print("\n*** TC: Delete the last element")
        myArray = [0, 1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        mylist.delete_item_in_position(5)
        expected = [0, 1, 2, 3, 4]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_find_element(self):
        print("\n*** TC: Find an element")
        myArray = [0, 1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        actual = mylist.find_element(3)
        expected = 3
        self.assertEqual(expected, actual)

    def test_find_element_not_in_a_list(self):
        print("\n*** TC: Find an element")
        myArray = [0, 1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        actual = mylist.find_element(9)
        expected = -1
        self.assertEqual(expected, actual)

    def test_reverse_list(self):
        print("\n*** TC: Reverse the list")
        myArray = [0, 1, 2, 3, 4, 5]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        myHead = ListNode()
        myHead = mylist.return_n_element_from_list(0)
        mylist.reverse_list(myHead)
        expected = [5, 4, 3, 2, 1, 0]
        actual = mylist.create_list_as_array()
        self.assertEqual(expected, actual)

    def test_return_n_element_from_list(self):
        print("\n*** TC: Return the Nth element")
        myArray = [0, 10, 25, 33, 4, 15]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        expected = 25
        actual = mylist.return_n_element_from_list(2)
        self.assertEqual(expected, actual)

    def test_return_extra_element_from_list(self):
        print("\n*** TC: Return the Nth element")
        myArray = [0, 10, 25, 33, 4, 15, 3]
        mylist = UnorderedList()
        mylist.create_list_from_array(myArray)
        expected = None
        actual = mylist.return_n_element_from_list(7)
        self.assertEqual(expected, actual)