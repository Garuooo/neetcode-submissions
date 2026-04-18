class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        visited=set()
        ROWS=len(grid)
        COLUMNS=len(grid[0])
        def dfs(row,column):
            if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
                return 0
            key = str((row,column))
            if key in visited:
                return 0
            visited.add(key)

            if grid[row][column]==0:
                return 0
            
            else:
                return 1 + dfs(row+1,column) +  dfs(row-1,column) +  dfs(row,column+1) +  dfs(row,column-1)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]==1:
                    area=max(area,dfs(i,j))

        return area            

        
        