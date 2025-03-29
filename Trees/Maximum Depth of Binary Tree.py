# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.smax = 0 
        self.s = 0  

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root==None):
            return 0
        
        self.s=self.s+1
        if(self.s>self.smax):
            self.smax=self.s
        
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.s=self.s-1

        return self.smax