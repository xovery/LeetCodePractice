class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        currMax = 0

        for num in nums:
            
            if(num == 0):
                maxNum = max(maxNum, currMax)
                currMax = 0
            else:
                currMax += 1
        
        maxNum = max(maxNum, currMax)

        return maxNum


        