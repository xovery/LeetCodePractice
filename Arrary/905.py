class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        curr = 0        
        if not nums:
            return nums

        for i in range (0, len(nums), +1):        
            if((nums[i] % 2) == 0):
                nums[i], nums[curr] = nums[curr], nums[i]               
                curr += 1
        return nums
