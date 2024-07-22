class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1


#method2
        if nums[right] > nums[left]:
            return nums[left]

        if len(nums) == 1:
            return nums[0]

        while left < right:
            mid = (right+left)//2    

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

#method 1        
'''
        while left != right:
            if nums[left] > nums[right]:
                left +=1
            else:
                right -=1

        return nums[left]
'''
        