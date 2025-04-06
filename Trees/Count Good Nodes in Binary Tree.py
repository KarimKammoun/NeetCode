# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=0
        self.pres=[]
    def goodNodes(self, root: TreeNode) -> int:

        if root==None:
            return self.res
        
        self.pres.append(root.val)
        if(root.val)>=max(self.pres):
            self.res+=1

        self.goodNodes(root.left)
        self.goodNodes(root.right)
        self.pres.pop()
        

    
        return self.res