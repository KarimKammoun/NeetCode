class Solution:
    def islandsAndTreasure(self, grid) :
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y, dist):
            
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] < dist:
                return
            grid[x][y] = dist
            dfs(x + 1, y, dist + 1)
            dfs(x - 1, y, dist + 1)
            dfs(x, y + 1, dist + 1)
            dfs(x, y - 1, dist + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:  
                    dfs(i, j, 0)