import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        pq = collections.deque()
        pq.append(root)
        res = []
        while len(pq):
            sz = len(pq)
            sumi = 0
            for i in range(sz):
                neigh = pq.popleft()
                if neigh:
                    sumi += neigh.val
                if neigh.left:
                    pq.append(neigh.left)
                if neigh.right:
                    pq.append(neigh.right)
            avg = sumi / sz
            res.append(avg)
        return res
