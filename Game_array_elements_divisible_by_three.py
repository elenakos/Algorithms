'''
Game:
- Given an array of integers, check if a[i]]*a[i+1] are divisible by 3
- If yes - replace a[i]] with a[i]]*a[i+1]
- Do verification for all elements
- Do as many iterations as needed until all elements are divisible by 3
- Return number of iterations
'''

import unittest
def game_divisible_by_three(arr):
    n = len(arr)
    count = 0
    while True:
        for i in range(n-1):
            product = arr[i] * arr[i+1]
            if product % 3 == 0:
                # print("==> product: {}".format(product))
                arr[i] = product
        count += 1
        if all_elements_divisible_by_three(arr):
            print("==> Solution is in {} iterations".format(count))
            return count
        # Stop after 10 iterations
        if count > 10:
            print("==> Looks like there is no solution; abort")
            return 0

def all_elements_divisible_by_three(arr):
    n = len(arr)
    for i in range(n):
        if arr[i]  % 3 != 0:
            return False
    return True


class TestGame(unittest.TestCase):
    def test_one_iteration(self):
        print("\n*** TC: Test one iteration")
        arr = [1, 3, 6]
        expected = 1
        actual = game_divisible_by_three(arr)
        self.assertEqual(actual, expected)

    def test_two_iterations(self):
        print("\n*** TC: Test 2 iterations")
        arr = [1, 2, 6]
        expected = 2
        actual = game_divisible_by_three(arr)
        self.assertEqual(actual, expected)

    def test_no_solution(self):
        print("\n*** TC: Test no solution ")
        arr = [1, 3, 7]
        expected = 0
        actual = game_divisible_by_three(arr)
        self.assertEqual(actual, expected)