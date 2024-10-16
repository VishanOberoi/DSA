class Solution:
    def reverseList(self, head):
      prev, curr = None, head
      while curr is not None:
         nxt = curr.next
         curr.next = prev
         prev = curr
         curr = nxt
      return prev