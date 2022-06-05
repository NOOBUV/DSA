from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def print_graph(self):
        print(self.graph)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)

    def dijkstra(self, src, dest):
