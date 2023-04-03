# Best Time to Buy and Sell Stock 2
class Solution(object):
    def maxProfit(self, prices):
        buy = -1
        profit = 0
        num = len(prices)
        if num == 0 or num == 1:
            return 0
        if prices[0] < prices[1]:
            buy = prices[0]
        for i in range(1, num - 1):
            if buy == -1: # didn't buy yet
                if prices[i] <= prices[i-1] and prices[i] < prices[i+1]:
                    buy = prices[i]
            else: # bought before (holding right now)
                if prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                    profit += prices[i] - buy
                    buy = -1
        if buy != -1 and prices[num - 2] < prices[num - 1]:
            profit += prices[num - 1] - buy
            buy = -1
        return profit