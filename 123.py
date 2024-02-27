class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowb1 = float('inf')
        maxp1 = 0
        lowb2 = float('inf')
        maxp2 = 0

        for price in prices:
            lowb1 = min(lowb1, price)
            maxp1 = max(maxp1, price - lowb1)
            lowb2 = min(lowb2, price - maxp1)
            maxp2 = max(maxp2, price - lowb2)
        
        return maxp2
        
        