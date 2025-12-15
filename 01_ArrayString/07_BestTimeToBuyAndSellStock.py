# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = 10e5
        maxProfit = 0
        for x in prices:
            if x < mini:
                mini = x
            profit = x - mini
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
        
