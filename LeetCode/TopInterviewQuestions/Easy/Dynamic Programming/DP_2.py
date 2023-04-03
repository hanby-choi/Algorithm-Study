# Best Time to Buy and Sell Stock
class Solution(object):
   def maxProfit(self, prices):
        profit = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
        return profit
   def maxProfit2(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_buy = prices[0]
        for p in prices[1:]:		
            max_profit = max(max_profit, p - min_buy)
            min_buy = min(min_buy, p)
        return max_profit