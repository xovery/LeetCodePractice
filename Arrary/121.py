class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0

        for price in prices:
            minP = min(minP, price)
            maxP = max(maxP, price-minP)
        
        return maxP

        #TC - O(N)
        #SC - O(N)
        