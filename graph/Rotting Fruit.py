class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]

        def dfs(x, y, minutes):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            if grid[x][y] == 0 or (grid[x][y] > 1 and grid[x][y] < minutes):
                return
            grid[x][y] = minutes
            dfs(x + 1, y, minutes + 1)
            dfs(x - 1, y, minutes + 1)
            dfs(x, y + 1, minutes + 1)
            dfs(x, y - 1, minutes + 1)

        # Start DFS from all initially rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dfs(i, j, 2)  # start from time = 2

        max_minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1  # fresh orange not reached
                max_minutes = max(max_minutes, grid[i][j])

        if max_minutes>2:
            return max_minutes - 2 
        else:
            return 0


            





        