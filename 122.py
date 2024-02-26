class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0
        GainP = 0

        for i in range (1, len(prices)):
            if(prices[i] > prices[i-1]):
                GainP += prices[i] - prices[i-1]
        
        return GainP
        
        #TC - O(n)
        #SC - O(1)