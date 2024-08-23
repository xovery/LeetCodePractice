class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        
        def quickSort(nums):
            if len(nums) <= 1:
                 return nums
            
            less, equal, greater = [], [], []

            pivot = random.choice(nums)

            for num in nums:

                if num < pivot:
                    less.append(num)
                elif num > pivot:
                    greater.append(num)
                else:
                    equal.append(num)
            
            return quickSort(less) + equal + quickSort(greater)


        nums = quickSort(nums)

        return nums
        