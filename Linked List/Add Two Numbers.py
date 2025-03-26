# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)  
        k = res  
        reste = 0  

        i = l1
        j = l2

        while i!=None or j!=None or reste:
            if i!=None:
                val1 = i.val 
            else:
                val1 =0
            if j!=None:
                val2 = j.val 
            else:val2= 0
            s = val1 + val2 + reste  

            reste = s // 10  
            n_element = ListNode(s % 10)  

            k.next = n_element
            k = k.next  

            if i!=None:
                i = i.next
            if j!=None:
                j = j.next
        
        return res.next  