class Solution:

    def CheckConnected(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return
        
        grid[row][col] = "0"
        directions = [(row, col+1), (row, col-1), (row-1, col), (row+1, col)]

        for r, c in directions:
            self.CheckConnected(grid, r, c)        

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rowLen = len(grid)
        colLen = len(grid[0])
        count = 0

        for row in range(rowLen):
            for col in range(colLen):
                if(grid[row][col] == "1"):
                    count += 1
                    self.CheckConnected(grid, row, col)

        return count


        