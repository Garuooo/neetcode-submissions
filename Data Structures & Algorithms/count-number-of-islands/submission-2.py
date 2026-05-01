class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, columns = len(grid),len(grid[0])
        def dfs(r,c):
            if r >= rows or c >= columns or c < 0 or r < 0:
                return 0
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            if grid[r][c] == "0":
                return 0 

            if grid[r][c] == "1":
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

            
            return 0
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print(visited)
                    print("s")
                    dfs(r,c)
                    res += 1
        
        return res