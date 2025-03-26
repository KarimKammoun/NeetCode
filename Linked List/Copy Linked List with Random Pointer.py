"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None


        i = head
        while i:
            new_node = Node(i.val, i.next, None)
            i.next = new_node
            i = new_node.next 

        i = head
        while i:
            if i.random:
                i.next.random = i.random.next
            i = i.next.next  


        i = head
        new_head = head.next
        copy = new_head
        while i:
            i.next = i.next.next
            copy.next = copy.next.next if copy.next else None
            i = i.next
            copy = copy.next

        return new_head