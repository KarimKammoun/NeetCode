# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def __init__(self):
        self.test = False  

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False  

        def isSameTree(p, q):
            self.res = True  

            def dfs(curr1, curr2):
                if curr1 is None and curr2 is None:
                    return
                if (curr1 is None and curr2 is not None) or (curr2 is None and curr1 is not None) or (curr1.val != curr2.val):
                    self.res = False
                    return

                dfs(curr1.left, curr2.left)
                dfs(curr1.right, curr2.right)

            dfs(p, q)
            return self.res

        s = isSameTree(root, subRoot)
        if s:
            self.test = True 
            return True  

        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)

        return self.test 