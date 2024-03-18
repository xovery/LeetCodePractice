class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        small = None

        for i in range (len(nums)-2, -1, -1):
            if(nums[i]<nums[i+1]):
                small = i
                break

        if small == None:
            nums.reverse()
            return

        for i in range (len(nums)-1, small, -1):
            if(nums[i] > nums[small]):
                nums[i], nums[small] = nums[small], nums[i]
                break

        nums[small+1:] = reversed(nums[small+1:])

