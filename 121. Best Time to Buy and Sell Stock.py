# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0: 
            return 0
        else:
            profit = 0
            minBuy = prices[0]
            for i in range(len(prices)):
                profit = max(prices[i] - minBuy, profit)
                minBuy = min(minBuy, prices[i])
            return profit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
