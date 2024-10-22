from  collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        q = deque()
        res = []
        if root:
            q.append(root)
        
        while q:
            level_res = []

            for i in range(len(q)):
                removed = q.popleft()
                level_res.append(removed.val)
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)
            
            res.append(level_res)
        return res


            

