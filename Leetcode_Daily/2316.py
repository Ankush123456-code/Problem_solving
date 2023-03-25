import collections
from typing import List



class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        mp = collections.defaultdict(list)
        for node in edges:
            mp[node[0]].append(node[1])
            mp[node[1]].append(node[0])
        vis = set()
        count=0
        def dfs(src):
            nonlocal mp, vis,count
            vis.add(src)
            count += 1
            for child in mp[src]:
                if child not in vis:
                    dfs(child)

        ans = 0
        to = 0
        for i in range(n):
            count=0
            if i not in vis:
                dfs(i)
            ans += count * (n - count - to)
            to += count
        return ans

