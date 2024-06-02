class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        merge = []

        # TC O(n)
        # SC O(n)
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merge.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        merge.append(newInterval)

        while i < len(intervals):
            merge.append(intervals[i])
            i += 1

        return merge



        # TC O(nlogn)        
        intervals.append(newInterval)
        intervals.sort()
        i = 1
        while i < len(intervals):
            if(intervals[i][0] <= intervals[i-1][1]):
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        

        return intervals