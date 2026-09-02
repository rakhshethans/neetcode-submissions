class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # varible size sliding window
        # want to find smallest and largest in that order
        # as you go right, if you find a price smaller than the current left pointer, move it to that pointer

        # start with first 2
        if len(prices) == 1:
            return 0
        
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
                right += 1

        return maxProfit