class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # O(n log n)
        i = 1
        while i < len(intervals): # O(n)
            if(intervals[i][0] <= intervals[i-1][1]):
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

        # TC : O(n log n)
        # SC : O(n) python 的 sorting space 為 n