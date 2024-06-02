class Solution:
# 利用等差數列求和與SUM(nums)比較後得知missing num
    def missingNumber(self, nums: List[int]) -> int:        
        return len(nums)*(len(nums)+1)//2 - sum(nums)

#   cyclic algorithm TC n*n SC (1)
        i = 0
        length = len(nums)
        while i < length:
            j = nums[i]

            if nums[i] < length and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+= 1

        for k in range(length):
            if k != nums[k]:
                return k
        
        return length




#TC nlogn, SC(1)
        nums = sorted(nums)
        missingNum = 0
        for num in nums:
            if missingNum != num:
                return missingNum
            missingNum += 1
        
        return len(nums)
