class Solution:
    def reorderList(self, head) -> None:
        #find halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #second half starts at
        second = slow.next

        #flip second half

        prev = None
        slow.next = None #break the link betwen the 2 lists

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #once above finishes, the prev is last element, and second = None.

        first, second = head, prev
        while second: #once the second has been merged, we're done.
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

