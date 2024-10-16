class Solution:
    def reverseList(self, head):
      
      def reverse(curr, prev):
         
        if curr is None:
            return prev
        
        nxt = curr.next
        curr.next = prev
        return reverse(nxt, curr)
      
      return reverse(head, None)


