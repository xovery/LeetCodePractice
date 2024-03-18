class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        curr_ptr = 0
        i = len(nums)
        for num in nums:
            if (num != val):
                nums[curr_ptr] = num
                curr_ptr += 1        
        return curr_ptr