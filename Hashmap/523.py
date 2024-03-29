class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #edge case
        if not nums or len(nums) < 2:
            return False

    
        #var def
        #init with -1 to count the range
        lookup = {0: -1}
        currSum = 0

        for i in range (len(nums)):
            currSum += nums[i]
            mod = currSum % k 

            if mod in lookup:
                if i - lookup[mod] >= 2:
                    return True
            else:
                lookup[mod] = i
        
        return False




        
        