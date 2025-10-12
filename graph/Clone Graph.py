class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        visited={}

    
        def dfs(node):

            clone=Node(node.val)

            if node.val in visited:
                return visited[node.val]

            if node.neighbors==None:
                return clone
            
            visited[clone.val]=clone

            for i in range (len(node.neighbors)):
                clone.neighbors.append(dfs(node.neighbors[i]))
            
            return clone


        if node==None:
            return None
        
        clone=dfs(node)
        return clone