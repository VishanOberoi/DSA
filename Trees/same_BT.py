# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
       
       if not p and not q:
        return True

       if not p or not q:
        return False

       if (p and q) and p.val != q.val:
        return False

       if p.val == q.val: #if roots are equal
        left =  self.isSameTree(p.left, q.left) #check left
        right = self.isSameTree(p.right, q.right) #check right

        return left and right

