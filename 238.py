class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        length = len(nums)
        left = [1]*length
        right = [1]*length
        result = [1]*length

        for i in range (1, length):
            left[i] = nums[i-1]*left[i-1]

        for j in range (length - 2 , -1, -1):
            right[j] = nums[j+1] * right[j+1]

        for k in range (length):
            result[k] = left[k] * right[k]
        return result

        
        