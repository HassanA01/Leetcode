from typing import List

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given an array of integers, <prices> where <prices[i]> is the price of the stock on the i'th day,
        figure out the maximum profit you can make.

        That is, figure the best day to buy the stock and the best day to sell the stock after the day you buy. 

        Return the max profit, and 0 if there can be no profit.
        """

        max_profit = 0

        buyDay = 0
        sellDay = 1

        while sellDay < len(prices):
            
            current_profit = prices[sellDay] - prices[buyDay]

            if prices[buyDay] < prices[sellDay]:
                max_profit = max(max_profit, current_profit)
            else:
                buyDay = sellDay
            
            sellDay += 1

        return max_profit