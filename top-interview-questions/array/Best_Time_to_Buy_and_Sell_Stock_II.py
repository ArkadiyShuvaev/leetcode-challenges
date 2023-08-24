# You are given an integer array prices where prices[i]
# is the price of a given stock on the i-th day.

# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 10^4

# Algorithm:
# The idea is to find a maximum difference between max and min values for the given array by dividing the array into chunks.
# The next iteration divides the chunk again into sub-chunks.
# The first iteration takes the entire array and returns the positive difference between max and min values of the given array.
# The second iteration divides the array into two chunks and calculate the sum of positive differences between max and min values of each chunk
# The third iteration divides the array into three chunks and sums differences of three chunks.
# The maximum number of iterations is (floor(array.length / 2))
# To get rid of the issue of a sawtooth graph we should repeat all iterations starting from the 2nd one, moving the first element of the array one element to the right.


import math
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        idx_start = 0
        idx_end = len(prices) - 1

        max_profit = self.__get_profit_for_range(idx_start, idx_end, prices)
        return max_profit

    def __get_profit_for_range(self, idx_start, idx_end, prices):
        max_profit = 0
        if idx_end - idx_start < 2:
            return max_profit

        for iteration_number in range(idx_start, idx_end + 1):
            profit_for_left_part = self.__get_profit_for_range(idx_start, idx_start + iteration_number, prices)
            profit_for_subrange_of_left_part = self.__get_profit_for_range(idx_start, idx_start + iteration_number, prices)
            profit_for_right_part = self.__get_profit_for_range(idx_start + iteration_number + 1, idx_end, prices)

            iteration_profit = profit_for_left_part + profit_for_right_part
            if iteration_profit > max_profit:
                max_profit = iteration_profit

        return max_profit

    # def __get_profit_for_range(self, idx_start: int, idx_end: int, prices: List[int]) -> int:
    #     profit = 0

    #     range_length = idx_end - idx_start

    #     if range_length < 3:
    #         return profit

    #     idx_median = idx_start + math.ceil(range_length / 2) - 1

    #     profit_for_left_part = self.__get_max_profit_for_range(idx_start, idx_median, prices)
    #     profit_for_range = self.__get_profit_for_range(idx_start, idx_median, prices)
    #     profit_for_left_part = max(profit_for_left_part, profit_for_range)

    #     profit_for_right_part = self.__get_max_profit_for_range(idx_median + 1, idx_end, prices)
    #     profit_for_range = self.__get_profit_for_range(idx_median + 1, idx_end, prices)
    #     profit_for_right_part = max(profit_for_right_part, profit_for_range)

    #     return profit_for_left_part + profit_for_right_part

    def __get_max_profit_for_range(self, idx_start: int, idx_end: int, price_arr: List[int]) -> int:
        """
        Calculates the maximum profit for a given range of prices.

        Args:
        - idx_start (int): the starting index of the range (inclusive)
        - idx_end (int): the ending index of the range (inclusive)
        - price_arr (List[int]): the array of prices

        Returns:
        - int: the maximum profit for the given range of prices
        """
        max_value: int = price_arr[idx_start]
        min_value: int = price_arr[idx_start]

        for i in range(idx_start + 1, idx_end + 1):
            if price_arr[i] > max_value:
                max_value = price_arr[i]
            if price_arr[i] < min_value and i != idx_end: # in case of the last element, do not set new min am=nd max values
                min_value = price_arr[i]
                # reset maximum
                max_value = min_value

        if max_value - min_value < 0:
            return 0

        return max_value - min_value


solution = Solution()

print(solution.maxProfit([2,4,1])) # 2
print(solution.maxProfit([7,1,5,2,3,6,4,8])) # 11
print(solution.maxProfit([7,1,5,2,3,6,4,8,0])) # 11
print(solution.maxProfit([1,2,3,4,5])) # 4
print(solution.maxProfit([7,6,4,3,1])) # 0
print(solution.maxProfit([2,1,2,0,1])) # 2
print(solution.maxProfit([1,2,4,2,5,7,2,4,9,0])) #15
