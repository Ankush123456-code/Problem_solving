# from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        NOT_COLORED, BLUE, GREEN = 0, 1, -1

        def dfs(parent, col):
            color[parent] = col
            for src in adj[parent]:
                if color[src] == NOT_COLORED and (not dfs(src, -col)):
                    return False
                if color[src] == col:
                    return False
            return True

        if (n == 1) or not dislikes:
            return True

        adj = defaultdict(list)
        for p1, p2 in dislikes:
            adj[p1].append(p2)
            adj[p2].append(p1)
        color = defaultdict(int)

        for person_id in range(1, n + 1):
            if color[person_id] == NOT_COLORED and (not dfs(person_id, BLUE)):
                return False
        return True
