from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={}
        res=[]

        def dfs(i,j,visited):
            if i==j :
                return False

            visited.add(i)

            for c in graph[i]:
                
                if c not in visited and dfs(c,j,visited)==False:
                    return False
            return True


        for i, j in edges:


            if i in graph and j in graph and dfs(i,j,set())==False:
                res= [i,j]

            if i not in graph:
                graph[i]=[j]
            else:
                graph[i].append(j)
            if j not in graph:
                graph[j]=[i]
                continue
            else:
                graph[j].append(i)

        return res
