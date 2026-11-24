class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, left, right = 0, 0, 1
        n = len(prices)
        if n <= 1: return 0

        while right < n:
            if prices[left] < prices[right]:
                value = prices[right] - prices[left]
                profit = max(profit, value)
            else:
                left = right
            right += 1

        return profit
        


