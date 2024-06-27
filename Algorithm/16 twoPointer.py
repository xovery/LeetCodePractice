class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        nums.sort()
        diff = math.inf

        for idx in range(length-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left = idx+1
            right = length-1

            while left < right:
                sum = nums[idx]+nums[left]+nums[right]
                if abs(target - sum) < abs(diff):
                    diff = target - sum

                if diff == 0:
                    return target

                if sum < target:
                    left += 1
                else:
                    right -= 1
        
        #sum = target - diff
        #return sum
        return target - diff



            
            

        