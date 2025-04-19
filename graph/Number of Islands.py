class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        n=len(grid)
        m=len(grid[0])

        def dfs(x,y):

            grid[x][y]="0"

            if x>0 and grid[x-1][y]=="1":
                dfs(x-1,y)
            if x<(n-1) and grid[x+1][y]=="1":
                dfs(x+1,y)
            if y>0 and grid[x][y-1]=="1":
                dfs(x,y-1)
            if y<(m-1) and grid[x][y+1]=="1":
                dfs(x,y+1)
            

        for i in range(n):
            for j in range (m):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1

        return res