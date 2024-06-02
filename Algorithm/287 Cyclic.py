class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        #TC n*n
        #SC 1
        i = 0
        length = len(nums)
        
        while i < length:
            j = nums[i]
            if nums[j] < length and nums[i] == nums[j]:
                return nums[i]
            elif nums[j] < length and nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        return length

