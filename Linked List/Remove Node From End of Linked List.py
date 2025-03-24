# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nl=0
        i=head
        
        while i!=None :
            nl=nl+1
            i=i.next

        if n==nl:
            return head.next
        elif nl==2 and n==1:
            head.next=None
            return head
        elif nl==2 and n==2:
            return head.next

        i=head
        for j in range(nl-n-1):
            i=i.next

        i.next=i.next.next

        return head