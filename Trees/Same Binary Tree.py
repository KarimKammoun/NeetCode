# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res=True

        def dfs(curr1,curr2):
            if (curr1==None and curr2==None):
                return
            if (curr1==None and curr2!=None) or (curr2==None and curr1!=None):
                self.res=False
                return
            if (curr1.val != curr2.val):
                self.res=False
                return

            dfs(curr1.left,curr2.left)
            dfs(curr1.right,curr2.right)
            
            return
        dfs(p,q)
        return self.res