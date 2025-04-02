'''
Given an array of integer or float values
Return the length of the longest increment/decrement sequence 
The sequence is counted when a difference between neighboring elements is 1 
'''

import unittest
import math

def find_longest_sequence(arr):
    if len(arr) == 0: return 0
    if all(type(item)==int  or type(item)==float for item in arr) != True: return 0
    max_seq = 1
    current_seq = 1
    seq_up = False
    seq_down = False
    for i in range(len(arr)-1):
        if math.ceil(arr[i] - arr[i+1]) == 1:    # math.ceil() is for floating variables since 4.1-3.1 = 0.9999999996, not 1!
            if seq_down:
                current_seq += 1
                if  max_seq < current_seq:
                    max_seq = current_seq
            else:
                seq_down = True
                seq_up = False
                current_seq += 1
                                
        elif math.ceil(arr[i+1] - arr[i]) == 1:
            if seq_up:
                current_seq += 1
                if  max_seq < current_seq:
                    max_seq = current_seq
            else:
                seq_up = True
                seq_down = False
                current_seq += 1

        else:
            current_seq = 1
            seq_up = False
            seq_down = False
    return max_seq


class FindLongestSequenceTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_find_longest_sequence_integers_go_up_returns_length(self):
        self.assertEqual(find_longest_sequence([1, 2, 3, 6, 5]), 3)                # sequences go up 

    def test_find_longest_sequence_integers_go_down_returns_length(self):
        self.assertEqual(find_longest_sequence([-1, -2, -3, -4, 6, 5]), 4)         # negative and positive
 
    def test_find_longest_sequence_integers_go_up_and_down_returns_length(self):
        self.assertEqual(find_longest_sequence([1, 2, 3, 6, 5]), 3)                # sequences go up and down
 
    def test_find_longest_sequence_floats_go_up_and_down_returns_length(self):
        self.assertEqual(find_longest_sequence([1.1, 2.1, 3.1, 4.1, 15, 16]), 4)   # float numbers go up 

    def test_find_longest_sequence_no_sequence_returns_length_of_one(self):
        self.assertEqual(find_longest_sequence([11, 21, 31, 41, 51, 61]), 1)       # no sequence 

    def test_find_longest_sequence_empty_array_returns_length_of_zero(self):
        self.assertEqual(find_longest_sequence([]), 0)                             # empty array

    def test_find_longest_sequence_letters_in_array_returns_length_of_zero(self):
        self.assertEqual(find_longest_sequence(['a', 'b', 'c', '#']), 0)           # letters and special characters

    def test_find_longest_sequence_special_characters_in_array_returns_length_of_zero(self):
        self.assertEqual(find_longest_sequence([4, 5, 6, 7, 8, 9, 10, '#']), 0)    # numbers and special characters
        
                
if __name__=='__main__':
   unittest.main()        
