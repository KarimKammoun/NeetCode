# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def dfs(node, k):

            temp = node
            for i in range(k):
                if not temp:
                    return node  
                temp = temp.next
            
            prev, curr = None, node
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            node.next = dfs(curr, k)
            return prev  

        return dfs(head, k)
