import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        pq = collections.deque()
        pq.append(root)
        res = []
        while len(pq):
            sz = len(pq)
            level = []
            for i in range(sz):
                neigh = pq.popleft()
                if neigh:
                    level.append(neigh.val)
                if neigh.left:
                    pq.append(neigh.left)
                if neigh.right:
                    pq.append(neigh.right)
            res.append(level)

        return res[::-1]