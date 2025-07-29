class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)

        visited = [0] * numCourses  
        res = []

        def dfs(node):
            if visited[node] == 1:
                return False 
            if visited[node] == 2:
                return True   

            visited[node] = 1  
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2  
            res.append(node)   
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []  

        return res[::-1]  