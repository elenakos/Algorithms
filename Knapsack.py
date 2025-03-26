'''
This is an algorithm for the fractional knapsack problem.
'''

import unittest

class Knapsack:
    def maximize_knapsack_value(capacity, items):
        print("\nCalculate max value that can fit in a knapsack with capacity {}, with items {}".format(capacity, items)   )
        if capacity <= 0:
            print("==> Capacity value is wrong: {}".format(capacity))
            return 0
        if len(items) == 0:
            print("==> The items are wrong: {}".format(items))
            return 0
        # Calculate value/weight ratio
        value_per_weight = [(value / weight, value, weight) for value, weight in items]
        value_per_weight.sort(reverse=True)

        total_value = 0
        remaining_capacity = capacity
        for ratio, value, weight in value_per_weight:
            if remaining_capacity == 0:
                break
            if weight <= remaining_capacity:
                # Take the entire item
                total_value += value
                remaining_capacity -= weight
            else:
                # Take the fraction of an item
                fraction = remaining_capacity / weight
                total_value += fraction * value
                remaining_capacity = 0
        print("==> Total value: %d" % total_value)
        return total_value

class TestKnapsack(unittest.TestCase):
    def test_zeros(self):
        print("**** TC: Capacity value is zeros")
        capacity = 0
        items = [(60, 20), (100, 50), (120, 30)]
        expected = 0
        actual = Knapsack.maximize_knapsack_value(capacity, items)
        self.assertEqual(expected, actual)

    def test_knapsack_valid_1(self):
        print("**** TC: Valid values for capacity and items")
        capacity = 50
        items = [(60, 20), (100, 50), (120, 30)]
        expected = 180
        actual = Knapsack.maximize_knapsack_value(capacity, items)
        self.assertEqual(expected, actual)

    def test_knapsack_valid_2(self):
        print("**** TC: Valid values for capacity and items")
        capacity = 40
        items = [(10, 30), (20, 10), (30, 40), (40, 20)]
        expected = 67.5
        actual = Knapsack.maximize_knapsack_value(capacity, items)
        self.assertEqual(expected, actual)

    def test_one_item(self):
        print("**** TC: Use just one item")
        capacity = 10
        items = [(500, 30)]
        expected = 166.66666666666666
        actual = Knapsack.maximize_knapsack_value(capacity, items)
        self.assertEqual(expected, actual)
