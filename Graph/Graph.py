from collections import defaultdict


class Graph:
    def __init__(self):
        self.__adj = defaultdict(list)

    def Add_edge(self, u, v):
        self.__adj[u].append(v)
        self.__adj[v].append(u)

    def get_adjency_list(self):
        return self.__adj


if __name__ == "__main__":
    g = Graph()
    g.Add_edge(0, 1)
    g.Add_edge(0, 2)
    g.Add_edge(1, 2)
    g.Add_edge(2, 3)
    print(g.get_adjency_list())
