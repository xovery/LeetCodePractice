class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        #edge case
        if not grid:
            return -1

        #define var
        player = (None, None)
        box = (None, None)
        target = None
        graph = set()
        visited = set()

        #init var
        for r in range (len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "#":
                    continue
                elif grid[r][c] == "T":
                    target = (r, c)
                elif grid[r][c] == "S":
                    player = (r, c)
                elif grid[r][c] == "B":
                    box = (r, c)
                graph.add((r, c))

        minheap = [(0, *player, *box)]
        
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        while minheap:
            pushes, curr_player_row, curr_player_col, curr_box_row, curr_box_col = heapq.heappop(minheap)
            if(curr_box_row, curr_box_col) == target:
                return pushes
            elif (curr_player_row, curr_player_col, curr_box_row, curr_box_col) in visited:
                continue
            visited.add((curr_player_row, curr_player_col, curr_box_row, curr_box_col))

            for r, c in directions:
                next_player_pos = (curr_player_row + r, curr_player_col + c)
                next_box_pos = (curr_box_row + r, curr_box_col + c)
                if next_player_pos == (curr_box_row, curr_box_col) and next_box_pos in graph :
                    heapq.heappush(minheap, (pushes+1, *next_player_pos, *next_box_pos))
                elif  next_player_pos != (curr_box_row, curr_box_col) and next_player_pos in graph:
                    heapq.heappush(minheap, (pushes, *next_player_pos,  curr_box_row, curr_box_col))

        return -1



