class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
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