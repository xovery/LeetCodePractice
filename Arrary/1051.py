class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortH = sorted(heights)
        count = 0

        for i in range(0, len(heights)):
            if(sortH[i] != heights[i]):
                count += 1

        return count

        #TC O(nlogn)
        #SC O(n)
