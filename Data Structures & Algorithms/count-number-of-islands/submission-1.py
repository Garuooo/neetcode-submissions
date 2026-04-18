class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS=len(grid)
        COLUMNS=len(grid[0])
        counts=0
        def dfs(row,column):
            if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
                return
            if grid[row][column]=="0":
                return

            grid[row][column]="0"

            dfs(row+1,column)
            dfs(row-1,column)
            dfs(row,column+1)
            dfs(row,column-1)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]=="1":
                    counts+=1
                    dfs(i,j)
        
        return counts