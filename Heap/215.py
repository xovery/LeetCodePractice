class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
#method 1. use the sorted method.        
        #TC is O(log n) sorted method
#        nums = sorted(nums)

#        if k <= len(nums):
#            return nums[len(nums)-k]

#method 2. use the heap
        #heapq is a binary heap, with TC are O(log n) push and O(log n) pop
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        

        return min_heap[0]