class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        left = 0
        right = 1

        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]            
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
            

        return max_profit
        