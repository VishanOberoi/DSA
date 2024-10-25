# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        self.vals = []
        
        def in_order(node):
            if not node:
                return None
            
            if node.left:
                in_order(node.left)
            
            self.vals.append(node.val)

            if node.right:
                in_order(node.right)
            

        in_order(root)
        return self.vals[k-1]
            

            
            

            