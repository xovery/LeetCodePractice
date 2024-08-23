class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count1 = sum (1 if num == 1 else 0 for num in nums) 

        if count1 == 0:
            return 0

        # Initialize the window of size `total_ones` and count number of 1's in the initial window
        current_ones = sum(nums[:count1])
        print("currntones:{}".format(current_ones))
        max_ones_in_window = current_ones
        
        
        # Use sliding window to find the maximum number of 1's in any window of size `total_ones`
        for i in range(1, n):
            # Slide the window: remove the element going out and add the element coming in
            print("(i + count1 - 1) % n:{}, i-1:{}".format((i + count1 - 1) % n, i-1))
            current_ones += nums[(i + count1 - 1) % n] - nums[i - 1]
            print("currntones:{}".format(current_ones))
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # Minimum swaps needed is the size of the window minus the maximum number of 1's found in any window
        min_swaps_needed = count1 - max_ones_in_window
        return min_swaps_needed

  


        return count1
        

            

        




        return 0


        