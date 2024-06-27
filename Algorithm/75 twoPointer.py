class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #TC O(n)
        #SC O(1)
        left = 0
        right = len(nums)-1
        idx = 0        
        while idx <= right:
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                idx += 1
                left += 1
            elif nums[idx] == 2:
                nums[idx], nums[right] = nums[right], nums[idx]                
                right -= 1
            else:
                idx  += 1
        