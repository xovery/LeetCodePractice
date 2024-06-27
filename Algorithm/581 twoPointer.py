class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length -1   
        
        #method 2 pointer
        subMin = float('inf')
        subMax = float('-inf')

        while left < right and nums[left] <= nums[left+1]:
            left += 1
        
        if left == right:
            return 0
        
        while right and left < right and nums[right] >= nums[right-1]:
            right -= 1
                
        for i in range(left, right+1):
            subMin = min(subMin, nums[i])
            subMax = max(subMax, nums[i])
        
        #extend the left to find the correct pos of left
        while left > 0 and nums[left-1] > subMin:
            left -= 1
        
        #extend the right to find the correct pos of right
        while right < length-1 and nums[right+1] < subMax:
            right += 1
        
        return right - left + 1



        #method sort
        #TC nlogn
        #SC n
     
        #SortedNum = sorted(nums)  
        SortedNum = nums.copy()
        SortedNum.sort()

        posLeft = 0       

        while left < length:
            if SortedNum[left] != nums[left]:
                posLeft = left
                break;
            else:
                left += 1
        
        while right > left:
            if SortedNum[right] != nums[right]:
                break
            else:
                right -= 1

        return right - left + 1
        
        





        
        