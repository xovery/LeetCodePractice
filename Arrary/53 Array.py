class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxSum = -math.inf
        sum = 0

        #TC O(n)
        #SC O(1)

        for num in nums:
            sum += num

            if num > sum:
                sum = num
        
            maxSum = max(maxSum, sum)

        return maxSum
        