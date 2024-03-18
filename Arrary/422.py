class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        #idea 1, use the sorted arryr to find the duplicated num
        nums = sorted(nums)
        tmp = nums[0]
        output = []

        for i in range(1, len(nums), +1):
            if(nums[i] == tmp):
                output.append(tmp)
            else:
                tmp = nums[i]
                
        return output    

        #use flag as idea 2.
        for i in range(len(nums)):
            idx = abs(nums[i])-1

            if(nums[idx] < 0):
                output.append(idx+1)
            else:
                nums[idx] = -nums[idx]
        
        return output            