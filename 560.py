class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0
        
        count = 0
        currSubSum = 0
        lookup = {0:1}

        for num in nums:
            currSubSum += num

            if currSubSum - k in lookup:
                count += lookup[currSubSum - k ]
            
            lookup[currSubSum] = lookup.get(currSubSum, 0) + 1
                
        return count

        # TC O(n)
        # SC O(n)