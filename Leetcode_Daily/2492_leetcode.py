import collections

from typing import List, Union, Any


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> Union[float, Any]:
        adj = collections.defaultdict(list)
        vis = set()
        pq = collections.deque()

        for i in roads:
            adj[i[0]].append([i[1], i[2]])
            adj[i[1]].append([i[0], i[2]])

        pq.append(1)
        vis.add(1)
        ans = 1e8
        # BFS you can use DFS also for the same this problem like you have to travel
        # all path minimum at once so that you can get minimum value for that path
        while pq:
            node = pq.popleft()
            curr_node = node
            for i in adj[curr_node]:
                ans = min(i[1], ans)
                if i[0] not in vis:
                    vis.add(i[0])
                    pq.append(i[0])
        if 1 in vis and n in vis:
            return ans
        return 1e8
