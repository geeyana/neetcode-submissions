class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = profit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left] and right != len(prices)-1:
                left = right
                right = left + 1

            profit = prices[right] - prices[left]

            ans = max(ans, profit)

        return ans