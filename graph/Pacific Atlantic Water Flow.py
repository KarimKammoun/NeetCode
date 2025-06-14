from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        n,m=len(heights),len(heights[0])
        pacific_reachable=set()
        atlantic_reachable=set()

        def dfs(i,j,visited,prev_height):

            if (i<0 or i>=n or j<0 or j>=m or (i, j) in visited or heights[i][j]<prev_height):
                return

            visited.add((i,j))

            dfs(i,j+1,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
            dfs(i+1,j,visited,heights[i][j])
            dfs(i-1,j,visited,heights[i][j])



        for i in range(n):
            dfs(i,0,pacific_reachable,heights[i][0])
        for j in range(m):
            dfs(0,j,pacific_reachable,heights[0][j])

        for i in range(n):
            dfs(i,m-1,atlantic_reachable,heights[i][m-1])
        for j in range(m):
            dfs(n-1,j,atlantic_reachable,heights[n-1][j])

        result=list(pacific_reachable & atlantic_reachable)
        
        return [list(i) for i in result]




