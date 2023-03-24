import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for edge in connections:
            adj[edge[0]].append((edge[1], 1))
            adj[edge[1]].append((edge[0], 0))
        ans = 0

        def dfs(src, parent):
            nonlocal ans, adj
            for child in adj[src]:
                if parent != child[0]:
                    ans += child[1]
                    dfs(child[0], src)

        dfs(0, -1)
        return ans
