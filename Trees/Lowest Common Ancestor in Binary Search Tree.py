# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=TreeNode()
        self.test=False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root==None:
            return 0
        
        if ((root.val>p.val and root.val<q.val) or (root.val<p.val and root.val>q.val)) and self.test==False:
            self.res=root
            self.test=True


        if (root.val>q.val and root.val>p.val):
            self.lowestCommonAncestor(root.left,p,q)
        elif (root.val<q.val and root.val<p.val):
            self.lowestCommonAncestor(root.right,p,q)
        else:
            self.res=root
            self.test=True

        return self.res

