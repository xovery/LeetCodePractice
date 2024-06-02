class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        length = len(nums)
        i = 0

        while i < length:
            pos = nums[i] - 1
            if nums[i] > 0 and nums[i] < length and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i+=1

        for i in range(length):
            if nums[i] != i+1:
                return i+1
        
        return length+1




        