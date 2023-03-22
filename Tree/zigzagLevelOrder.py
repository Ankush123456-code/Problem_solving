import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        pq = collections.deque()
        pq.append(root)
        res = []
        level = 0
        while len(pq):
            sz = len(pq)
            ans = []
            for i in range(sz):
                neigh = pq.popleft()
                if neigh:
                    ans.append(neigh.val)
                if neigh.left:
                    pq.append(neigh.left)
                if neigh.right:
                    pq.append(neigh.right)
            if level % 2 == 0:
                res.append(ans)
            else:
                ans.reverse()
                res.append(ans)
            level += 1
        return res
