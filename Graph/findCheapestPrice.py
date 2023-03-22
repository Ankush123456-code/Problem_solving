from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        from collections import defaultdict, deque
        dist = [1e9] * n
        adj = defaultdict(list)
        for flight in flights:
            s, t, p = flight[0], flight[1], flight[2]
            adj[s].append((t, p))
        qq = deque()
        qq.append((0, src, 0))
        while len(qq) != 0:
            stop, node, price = qq.popleft()
            if stop > k:
                continue
            for it in adj[node]:
                adjN = it[0]
                pr = it[1]
                if dist[adjN] > price + pr:
                    dist[adjN] = pr + price
                    qq.append((stop + 1, adjN, dist[adjN]))
        if dist[dst] == 1e9:
            return -1
        return dist[dst]

