'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print("\nFind the best profit to buy/sell a stock: {}".format(prices))

        if len(prices) < 2:
            print("==> The price array is too short")
            return 0

        # Go over an array and find the biggest difference
        maxProfit = 0
        currentProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                else:
                    currentProfit = prices[j] - prices[i]
                    if currentProfit > maxProfit:
                        maxProfit = currentProfit
        print("==> The maximum profit is {}".format(maxProfit))
        return maxProfit

class TestSolution(unittest.TestCase):

    def test_solution(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(Solution().maxProfit(prices), 5)

    def test_solution_no_profit(self):
        prices = [7,6,4,3,1]
        self.assertEqual(Solution().maxProfit(prices), 0)

    def test_solution_no_data(self):
        prices = []
        self.assertEqual( Solution().maxProfit(prices), 0)

    def test_solution_one_price(self):
        prices = [3]
        self.assertEqual(Solution().maxProfit(prices), 0)
