# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        res = []
        q = deque()
        if root:
            q.append(root)
        right_most = None
        
        while q:
            for i in range(len(q)):
                removed = q.popleft()
                right_most = removed
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)
            res.append(right_most.val)
        return res