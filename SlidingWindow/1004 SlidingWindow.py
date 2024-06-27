class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start = 0
        end = 0
        currLen = 0
        consecutive = 0
        maxLen = 0

        for end in range(len(nums)):

            if nums[end] == 0:
                consecutive += 1
                
            while consecutive > k and start <= end:
                if nums[start] == 0:
                    consecutive -= 1
                start += 1 
            
            currLen = end - start + 1            
            maxLen = max(maxLen, currLen)
        
        return maxLen


            



        