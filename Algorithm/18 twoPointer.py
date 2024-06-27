class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        length = len(nums)
        if length < 4:
            return []

        nums.sort()
        
        for i in range (length-3 ):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range (i+1, length-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = length -1

                while left < right:
                    sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if sum == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1

        return res