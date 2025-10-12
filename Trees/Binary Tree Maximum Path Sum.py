# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res=-10000



        def dfs(root):
            nonlocal res
            if root==None:
                return 0
            
            
            


            l=dfs(root.left)
            r=dfs(root.right)
            a=max(root.val,root.val+l+r,root.val+r,root.val+l)

            if a>res:
                res=a



            return max(root.val,root.val+l,root.val+r)


        dfs(root)

        return res
        