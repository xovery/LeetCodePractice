class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        val = -999
        for num in nums:
            if(val != num):
                nums[ptr] = num
                val = num
                ptr += 1

        return ptr                