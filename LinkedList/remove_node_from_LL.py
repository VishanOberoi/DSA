class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = head

        #shift the right, to n ahead of head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        #now left is at pre-skip position, and right at null. The one after left must be skipped.
        
        left.next = left.next.next

        return dummy.next
        


        