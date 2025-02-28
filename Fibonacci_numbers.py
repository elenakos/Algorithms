'''
Return n-element from the Fibonacci sequence
This file contains three solutions
'''

import unittest

class Solution():

    def returnElementFromFibonacci(self, n):
        print("\nReturn {}th element from the Fibonacci sequence".format(n))
        if n <= 1:
            return n

        # Seed the sequence
        a = 0
        b = 1
        i = 1
        print("==> 1 element is 1")
        while i < n:
            a, b = b, a+b
            i += 1
            print("==> {} element is {}".format(i, b))
        return b

    def returnElementFromFibonacciRecurs(self, n):
        print("\n!!! Return {}th element from the Fibonacci sequence using recursive".format(n))
        if n <= 1:
            return n
        else:
            return self.returnElementFromFibonacciRecurs(n-1) + self.returnElementFromFibonacciRecurs( n-2)

    def returnElementFromFibonacciList(self, n):
        print("\nReturn {}th element from the Fibonacci sequence".format(n))
        if n <= 1:
            return n
        elements = [0, 1]
        for i in range(2, n+1):
            elements.append(elements[i-1] + elements[i-2])
        return elements[n]


class TestSolution(unittest.TestCase):
    def test_case_0(self):
        n = 0
        expected = 0
        actual = Solution().returnElementFromFibonacci(n)
        self.assertEqual(expected, actual)

    def test_case_1(self):
        n = 1
        expected = 1
        actual = Solution().returnElementFromFibonacci(n)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        n = 5
        expected = 5
        actual = Solution().returnElementFromFibonacci(n)
        self.assertEqual(expected, actual)

    def test_case_20(self):
        n = 20
        expected = 6765
        actual = Solution().returnElementFromFibonacci(n)
        self.assertEqual(expected, actual)

    def test_recursive_case_1(self):
        n = 1
        expected = 1
        actual = Solution().returnElementFromFibonacciRecurs(n)
        self.assertEqual(expected, actual)

    def test_recursive_case_5(self):
        n = 5
        expected = 5
        actual = Solution().returnElementFromFibonacciRecurs(n)
        self.assertEqual(expected, actual)

    def test_recursive_case_20(self):
        n = 20
        expected = 6765
        actual = Solution().returnElementFromFibonacciRecurs(n)
        self.assertEqual(expected, actual)

    def test_case_5_list(self):
        n = 5
        expected = 5
        actual = Solution().returnElementFromFibonacciList(n)
        self.assertEqual(expected, actual)

    def test_recursive_case_20_list(self):
        n = 20
        expected = 6765
        actual = Solution().returnElementFromFibonacciList(n)
        self.assertEqual(expected, actual)