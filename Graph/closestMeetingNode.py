class Solution:
    def closestMeetingNode(self, edges, node1, node2: int):
        dist1 = [-1] * len(edges)
        dist2 = [-1] * len(edges)

        def dfs(node, distance, dist):
            if node == -1 or node in vis:
                return
            vis.add(node)
            dist[node] = distance
            dfs(edges[node], distance + 1, dist)

        print("hello")
        vis = set()
        dfs(node1, 0, dist1)
        vis = set()
        dfs(node2, 0, dist2)
        ans = 0
        value = len(edges)
        for i in range(len(dist1)):
            if dist1[i] != -1 and dist2[i] != -1:
                if max(dist1[i], dist2[i]) < value:
                    value = max(dist1[i], dist2[i])
                    ans = i
        return ans
