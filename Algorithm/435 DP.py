class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        remove = 0
        end = intervals[0][0]

        for interval in intervals:
            start = interval[0]

            if (start < end):
                remove += 1
            else:
                end = interval[1]
        
        #TC = O(nlogn) used in sorting algorithm
        #SC = O(n), used in sorting algorithm
        
        return remove