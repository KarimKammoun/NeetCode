class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph= {i:set() for i in range (n)}
        visited= [0]*n

        for i in range (len(edges)):
            graph [edges[i][0]].add(edges[i][1])
            graph [edges[i][1]].add(edges[i][0])

        
        print(graph)



        def dfs(node,parent):
            if node == parent:
                return False
            
            if visited[node]==1:
                return False


            visited [node]=1

            for j in graph[node]:
                if j==parent:
                    continue
                if not dfs(j,node):
                    return False
            
            return True

        
        if not dfs(0,n+1) or sum(visited)<n:
            return False

        return True
