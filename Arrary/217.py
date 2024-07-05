class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return True if len(set(nums)) != len(nums) else False

        nums = sorted(nums)
        #TC (O(nlogn))
        #SC (O(n))
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False


        #TC (O(n^2))
        #SC (O(n))
        
        lookup = []
        for num in nums:
            if num in lookup:
                return True
            else:
                lookup.append(num)
        
        return False
        