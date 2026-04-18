class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)-1
        COLUMNS=len(grid[0])-1
        def dfs(r,c):
            if r < 0 or r > ROWS or c < 0 or c > COLUMNS:
                return
            if grid[r][c] == "#" or grid[r][c] == "0":
                return
            else:
                grid[r][c]="#"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        res=0
        for i in range(ROWS+1):
            for j in range(COLUMNS+1):
                if grid[i][j]=="1":
                    print(grid)
                    res+=1
                    dfs(i,j)
        return res