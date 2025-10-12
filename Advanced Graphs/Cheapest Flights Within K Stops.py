class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph={}
        visited=set()
        res=1000000

        for i in (flights):
            if i[0] not in graph:
                graph[i[0]]=[(i[1],i[2])]
            else:
                graph[i[0]].append((i[1],i[2]))
            

        print(graph)
        def dfs(k,node,s):
            print(visited)
            nonlocal res

            print(res)

            if node in visited:
                return
            
            if node==dst and s<res:
                res=s
            if k==0:
                return
            if node not in graph:
                return

            visited.add(node)

            for i in graph[node]:
                
                dfs(k-1,i[0],s+i[1])
            visited.remove(node)




        dfs(k+1,src,0)
        if res==1000000:
            return -1
        return res
        