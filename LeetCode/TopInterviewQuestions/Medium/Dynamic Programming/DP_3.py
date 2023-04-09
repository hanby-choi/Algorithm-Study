# Coin Change
class Solution(object):
    def coinChange(self, coins, amount):
        d = [10001] * (amount + 1)
        d[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    d[i] = min(d[i-c] + 1, d[i])
        if d[amount] == 10001:
            return -1
        return d[amount]