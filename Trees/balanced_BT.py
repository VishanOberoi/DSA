# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(node):
            if not node:
                return True, 0
            
            left, right = dfs(node.left), dfs(node.right)

            if left[0] and left[0] and abs(left[1] - right[1]) <= 1:
                return True, 1 + max(left[1], right[1])

            else:
                return False, 1 + max(left[1], right[1])
        
        return dfs(root)[0]


        