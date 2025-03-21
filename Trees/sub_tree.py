# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
       


    def isSame(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            left = self.isSame(node1.left, node2.left)
            right = self.isSame(node1.right, node2.right)

            return left and right
        
        return False

        
