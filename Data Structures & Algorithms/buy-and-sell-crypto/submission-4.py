class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxprofit = 0
        while l <= r and r < len(prices):
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1
            maxprofit = max(maxprofit, profit)
        return maxprofit
            

            