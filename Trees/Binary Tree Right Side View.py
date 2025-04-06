# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=[]
        self.p=0
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
 
        if (root == None):
            self.p=self.p-1
            return self.res

        if self.p>=len(self.res):
            self.res.append(root.val)
 

        self.p+=1
        self.rightSideView(root.right)
        self.p+=1
        self.rightSideView(root.left)
        self.p-=1

        return self.res