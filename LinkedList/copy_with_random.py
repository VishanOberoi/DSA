class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        curr = head
        old_to_copy = {}

        while curr:
            node = Node(curr.val)
            old_to_copy[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                old_to_copy[curr].next = old_to_copy[curr.next]
            if curr.random:
                old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next
        
        return old_to_copy[head] if head else None
