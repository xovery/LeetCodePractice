class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #for i in range (len(nums)):
        #    nums[i] = nums[i] * nums[i]
        #return sorted(nums)
        # TC O(nlogn)
        # SC O(1)

        result = []
        left = 0
        right = len(nums) -1

        while left <= right:
            if(nums[left]**2 < nums[right]**2):
                result.append(nums[right]**2)
                right -= 1
            else:
                result.append(nums[left]**2)
                left +=1
            
        return reversed(result)
        
        # TC O(n)
        # SC O(1)