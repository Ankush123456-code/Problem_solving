from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        vis = set()
        extra = set()
        dist = [0 for i in range(len(edges))]
        ans = -1

        def dfs(edges, node, dis):
            nonlocal extra, vis, dist, ans
            if node != -1:
                if node not in vis:
                    extra.add(node)
                    vis.add(node)
                    dist[node] = dis
                    dfs(edges, edges[node], dis + 1)
                elif node in extra:
                    ans = max(ans, dis - dist[node])

        for i in range(len(edges)):
            if i not in vis:
                extra.clear()
                dfs(edges, i, 0)
        return ans
