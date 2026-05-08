class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 0
        profit = 0

        for i in range(len(prices)):

            if i == 0:
                buy = prices [i]
                continue

            buy = min(buy, prices[i])
            sell = prices[i]

            profit = max(profit, sell-buy)

        return profit