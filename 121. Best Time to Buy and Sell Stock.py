class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Calculate and update max profit

        return max_profit
