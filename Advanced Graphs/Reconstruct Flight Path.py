from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ["JFK"]
        graph = {}
        visited = {}
        n = len(tickets)

        for src, dst in tickets:
            if src not in graph:
                graph[src] = [dst]
            else:
                graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()
            visited[src] = [0] * len(graph[src])

        def dfs(city, t):
            if t == n:
                return True

            if city not in graph:
                return False

            for i in range(len(graph[city])):
                if visited[city][i] == 1:
                    continue

                visited[city][i] = 1
                next_city = graph[city][i]
                res.append(next_city)

                if dfs(next_city, t + 1):
                    return True

                visited[city][i] = 0
                res.pop()

            return False

        dfs("JFK", 0)
        return res
