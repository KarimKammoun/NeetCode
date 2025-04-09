# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=0
        self.n=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def dfs (root):
            if root==None:
                return

            dfs(root.left)
            self.n+=1
            if self.n==(k):
                self.res=root.val
                return
            dfs(root.right)
            



            return 
        dfs(root)
        print(self.n)

        return self.res