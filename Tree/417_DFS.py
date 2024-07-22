class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfsSort(r, c, visited, prev_h):
            if (
                (r, c) in visited
                or r < 0
                or r == rows
                or c < 0
                or c == cols
                or heights[r][c] < prev_h
            ):
                return
            visited.add((r, c))
            dfsSort(r + 1, c, visited, heights[r][c])
            dfsSort(r - 1, c, visited, heights[r][c])
            dfsSort(r, c + 1, visited, heights[r][c])
            dfsSort(r, c - 1, visited, heights[r][c])

        for col in range(cols):
            dfsSort(0, col, pacificSet, heights[0][col])
            dfsSort(rows - 1, col, atlanticSet, heights[rows - 1][col])

        for row in range(rows):
            dfsSort(row, 0, pacificSet, heights[row][0])
            dfsSort(row, cols - 1, atlanticSet, heights[row][cols - 1])
        # print(pacificSet)
        # print("\n")
        # print(atlanticSet)
        return list(pacificSet.intersection(atlanticSet))
