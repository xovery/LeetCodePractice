class Solution:
    def checkIslandSize(self, grid: List[List[int]], row, col, size, isLandTag) -> int:
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
            return 0
        
        directions = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]        
        size = 1
        grid[row][col] = isLandTag        
        
        for r, c in directions:            
                size += self.checkIslandSize(grid, r, c, 1, isLandTag)

        return size 


    def largestIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        maxSizeLand = 0
        rowLen = len(grid)
        colLen = len(grid[0])        
        lookup = {}
        # start from 2 
        isLandTag = 2 

        #find all island with a tag in lookup
        for row in range(rowLen):
            for col in range(colLen):
                if(grid[row][col] == 1):
                    size = self.checkIslandSize(grid, row, col, 1,isLandTag)
                    maxSizeLand = max(size, maxSizeLand)
                    lookup[isLandTag] = size
                    isLandTag += 1

        #find 0 in the grid and connect island if possible.
        for row in range(rowLen):
            for col in range(colLen):
                if(grid[row][col] == 0):
                    visited_tag = set()
                    directions = [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]
                    for r, c in directions:
                        if not r < 0 and not c < 0 and not r >= len(grid) and not c >= len(grid[0]) and grid[r][c] != 0:
                            visited_tag.add(grid[r][c])
                    
                    isLandSum = 0
                    
                    for tag in visited_tag:
                        isLandSum += lookup[tag]
                    isLandSum += 1
                    maxSizeLand = max(maxSizeLand, isLandSum)

        return maxSizeLand
                


        

        