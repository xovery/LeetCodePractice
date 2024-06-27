class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        #TC = O(N)
        #SC = O(1))

        #minimalLength = len(nums)
        minimalLength = math.inf

        #if sum(nums) < target:
        #    return 0

        start = 0
        end = 0
        currLen = 0
        currVal = 0        

        for i in range(len(nums)):
            currVal += nums[end]
            currLen = end - start + 1
            
            while currVal >= target and start <= end:
                minimalLength = min(minimalLength, currLen)
                currVal -= nums[start]
                start += 1
                currLen = end - start + 1
            
            end += 1

        if minimalLength == math.inf:
            return 0

        return minimalLength




        


        