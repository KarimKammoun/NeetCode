# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i=head

        while (i!=None and -1000<i.val<1000):
            i.val=-2000
            i=i.next
        
        if i==None :
            return False
        else:
            return True