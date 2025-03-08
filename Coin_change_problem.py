'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

import unittest

class Solution(object):
    def coin_change_dp(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        print("\nDynamic solution for {} using {} coins ".format(amount, coins))
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coin_change(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        coins.sort()
        reminder = amount
        counter = 0
        array_size = len(coins)

        result =  {}

        for i in range(array_size-1, -1, -1):
            if reminder >= coins[i]:
                num = reminder//coins[i]
                reminder = reminder - num*coins[i]
                counter = counter + num
                result[coins[i]] = num
        if reminder != 0:
            return -1
        if counter == 0:
            return -1
        print(" ==> Resulting set of coins: {}".format(result))
        return counter

class TestSolution(unittest.TestCase):
    def test_case_valid_data_1(self):
        print("\n*** TC: Valid data with a solution for 11")
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        actual = Solution().coin_change(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_valid_data_1_dp(self):
        print("\n*** TC: Valid data with a solution for 11")
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        actual = Solution().coin_change_dp(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_valid_data_2(self):
        print("\n*** TC: Valid data with bigger amount with a solution for 78")
        coins = [1, 2, 5]
        amount = 78
        expected = 17
        actual = Solution().coin_change(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_valid_data_2_dp(self):
        print("\n*** TC: Valid data with bigger amount with a solution for 78")
        coins = [1, 2, 5]
        amount = 78
        expected = 17
        actual = Solution().coin_change_dp(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_valid_data_for_dp(self):
        print("\n*** TC: Valid data with a solution")
        coins = [186,419,83,408]
        amount = 6249
        expected = 20
        actual = Solution().coin_change_dp(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_amount_zero(self):
        print("\n*** TC: Amount is zero")
        coins = [1]
        amount = 0
        expected = 0
        actual = Solution().coin_change(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_no_solution_no_one_cents(self):
        print("\n*** TC: The set doesn't have one cents")
        coins = [2, 5]
        amount = 6
        expected = -1
        actual = Solution().coin_change(coins, amount)
        self.assertEqual(actual, expected)

    def test_case_no_solution_coins_too_large(self):
        print("\n*** TC: Coins too large for the amount")
        coins = [25, 50]
        amount = 20
        expected = -1
        actual = Solution().coin_change(coins, amount)
        self.assertEqual(actual, expected)