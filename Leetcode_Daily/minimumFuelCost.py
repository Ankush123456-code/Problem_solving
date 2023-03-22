from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads, seats: int) -> int:
        adj = defaultdict(list)
        for it in roads:
            adj[it[0]].append(it[1])
            adj[it[1]].append(it[0])
        res = 0

        def dfs(node, parent):
            nonlocal res
            passenger = 0
            for neigh in adj[node]:
                if neigh != parent:
                    p = dfs(neigh, node)
                    passenger += p
                    res += int(ceil(p / seats))
            return passenger + 1

        dfs(0, -1)
        return res
