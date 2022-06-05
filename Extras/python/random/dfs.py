from typing import DefaultDict


class Graph:
    def __init__(self):
        self.graph = DefaultDict(list)
        self.vertices = len(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)

    def dfs(self, u, discovered):
        # if u not in discovered:
        #     discovered.append(u)
        #     if len(self.graph[u]) == 0:
        #         return
        #     next = self.graph[u].pop()
        #     self.dfs(next, discovered)
        for i in self.graph:
            if i not in discovered:
                discovered.append(i)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.print_graph()
    print()
    disc = []
    g.dfs(0, disc)
    print(disc)
