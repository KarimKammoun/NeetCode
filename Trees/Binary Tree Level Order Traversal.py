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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if (root == None):
            self.p=self.p-1
            return self.res

        if self.p>=len(self.res):
            self.res.append([])
        self.res[self.p].append(root.val)

        self.p+=1
        self.levelOrder(root.left)
        self.p+=1
        self.levelOrder(root.right)
        self.p-=1

        return self.res