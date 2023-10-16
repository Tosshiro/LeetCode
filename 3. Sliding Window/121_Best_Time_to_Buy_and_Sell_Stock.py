'''
Description
LeetCode solution to 121. Best Time to Buy and Sell Stock

@author: Jw
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = 0
        highest = 1
        max_profit = 0

        while highest < len(prices):
            if prices[lowest] > prices[highest]:
                # Change lowest value to the correct value
                lowest = highest

            else:
                profit = prices[highest] - prices[lowest]
                # Comparing whether current profit made with current highest value is more than previous one
                max_profit = max(profit, max_profit)
            highest += 1

        return max_profit

# Time complexity: O(n)
# Memory complexity: O(1)