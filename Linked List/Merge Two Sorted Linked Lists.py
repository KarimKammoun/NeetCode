# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            res = list1
            i = list1
            ox = list2
        else:
            res = list2
            i = list2
            ox = list1

        while i.next is not None and ox is not None:
            if ox.val < i.next.val:
                ox1 = i.next
                i.next = ox
                ox = ox1  
            i = i.next  

        if i.next is None:
            i.next = ox 

        return res