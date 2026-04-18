class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ROWS=len(grid)-1
        COLUMNS=len(grid[0])-1



        def dfs(r,c):
            print(r,c)
            if r < 0 or r > ROWS or c < 0 or c > COLUMNS:
                return 0
            
            if grid[r][c]==0 or grid[r][c]=="#":
                return 0
            
            if grid[r][c]==1:
                grid[r][c]="#"
                return 1 + dfs(r,c+1) + dfs(r,c-1) + dfs(r+1,c) + dfs(r-1,c)


        res = 0

        for i in range(ROWS+1):
            for j in range(COLUMNS+1):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))


        return res