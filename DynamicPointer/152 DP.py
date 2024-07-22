class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMax = nums[0]
        currMin = nums[0]
        finalRlt = nums[0]
        
        #TC O(n)
        #SC O(1)
        for i in range(1, len(nums)):
            nextMax = currMax * nums[i]
            nextMin = currMin * nums[i]
            currMax = max(nums[i], nextMax, nextMin)
            currMin = min(nums[i], nextMax, nextMin)
            finalRlt = max(finalRlt, currMax)
        return finalRlt