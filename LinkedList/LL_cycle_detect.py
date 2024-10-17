# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        # visited = set()
        # while head:
        #     if head not in visited:
        #         visited.add(head)
        #         head = head.next
        #     else:
        #         return True
        # return False

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        return False
    
        
        