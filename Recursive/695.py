class Solution:
    def countIslandSize(self, grid, row, col, size):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        
        grid[row][col] = 0

        directions = [(row+1,col),(row-1, col), (row, col+1), (row, col-1)]

        for r, c in directions:
            size += self.countIslandSize(grid, r, c, 1) 
        
        return size



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rowLen = len(grid)
        colLen = len(grid[0])
        maxIsland = 0

        for row in range(rowLen):
            for col in range (colLen):
                if(grid[row][col] == 1):
                    islandSize = self.countIslandSize(grid, row, col, 1)
                    maxIsland = max(islandSize, maxIsland)
        return maxIsland

    




    


        