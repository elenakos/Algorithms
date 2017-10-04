'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''
import unittest

def insert_merge_non_overlapping_intervals(a, b):
    left = []
    right = []
    result = []
    start = None
    end = None
    # find the right part
    for each in a:
        if each[1] < b[0]:
            left.append(each)
        else:
            break    
    
    # find the left part
    for i in reversed(range(len(a))):
        if a[i][0] > b[1]:
            right.insert(0, a[i])
        else:
            break    

    # Then need to find a new interval
    mergedlist = []
    mergedlist.append(left)
    mergedlist.extend(right)
    if mergedlist != a:
        if len(a) != len(left):
            start = min(b[0], a[len(left)][0])
        else:
            start = b[0]    
        if len(a) != len(right):
            end   = max(b[1], a[len(a)-len(right)-1][1])
        else:
            end = b[1]    

    if len(left) != 0:
        result = left
    if start != None :
        result.append([start, end])
    if len(right) != 0:
        result.extend(right)        
    
    return result  


class MergeIntervalsTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_intervals_no_need_to_merge_duplicate_interval(self):
        a = [[1,2], [3, 5], [6,9]]
        b = [3,5]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,2], [3, 5], [6,9]])

    def test_intervals_merge_at_the_beginning(self):
        a = [[1,3],[6,9]]
        b = [2,5]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,5],[6,9]])

    def test_intervals_merge_at_the_end(self):
        a = [[1,3],[6,9]]
        b = [5, 12]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,3],[5, 12]])

    def test_intervals_merge_many_intervals_in_the_middle(self):
        a = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        b = [4,9]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,2],[3,10],[12,16]])

    def test_intervals_insert_interval_in_the_middle(self):
        a = [[1,2],[6,7],[8,10]]
        b = [3, 5]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,2],[3,5],[6,7],[8,10]])

    def test_intervals_insert_interval_at_the_beginning(self):
        a = [[3,5],[6,7],[8,10],[12,16]]
        b = [0, 2]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[0, 2], [3,5],[6,7],[8,10],[12,16]])

    def test_intervals_insert_interval_at_the_end(self):
        a = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        b = [20, 22]
        self.assertEqual(insert_merge_non_overlapping_intervals(a, b), [[1,2],[3,5],[6,7],[8,10],[12,16], [20, 22]])



if __name__=='__main__':
   unittest.main()        
  
