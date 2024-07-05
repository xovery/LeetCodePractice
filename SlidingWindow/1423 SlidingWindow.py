class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        WindowsLength = len(cardPoints) - k
        currSum = sum(cardPoints[WindowsLength:]) 
        result = currSum           
        
        for i in range(k):
            currSum += cardPoints[i]
            currSum -= cardPoints[i+WindowsLength]
            result = max(result, currSum)
        
        return result