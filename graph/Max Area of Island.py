class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        area=0
        
        n=len(grid)
        m=len(grid[0])

        def dfs(x,y):
            nonlocal area

            area+=1
            grid[x][y]=0

            if x>0 and grid[x-1][y]==1:
                dfs(x-1,y)
            if x<(n-1) and grid[x+1][y]==1:
                dfs(x+1,y)
            if y>0 and grid[x][y-1]==1:
                dfs(x,y-1)
            if y<(m-1) and grid[x][y+1]==1:
                dfs(x,y+1)
        
        
        for i in range(n):
            for j in range (m):
                
                if grid[i][j]==1:
                    area=0
                    dfs(i,j)
                    
                if area>max_area:
                    max_area=area

        return max_area