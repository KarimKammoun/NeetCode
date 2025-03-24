# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=head
        pres=None

        while(i!=None):
            suivant=i.next
            i.next=pres
            pres=i
            i=suivant
        return pres