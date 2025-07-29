class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=0

        graph= {i:[] for i in range (n)}
        visited= [0]*n

        for i in range (len(edges)):
            graph [edges[i][0]].append(edges[i][1])
            graph [edges[i][1]].append(edges[i][0])

        
        print(graph)



        def dfs(node):
            if visited[node]==1:
                return

    
            visited [node]=1

            for j in graph[node]:

                dfs(j)

        for i in range(len(visited)):
            if visited[i]==1:
                continue
            else:
                dfs(i)
            res=res+1





        return res
    
        