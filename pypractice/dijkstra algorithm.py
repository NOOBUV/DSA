parent=[-1]*4
value=[float('inf')]*4
processed=[False]*4
value[0]=0
class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v]=w
        self.graph[v][u]=w 
    def print_graph(self):
        print(self.graph)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 3)
    g.print_graph()
    print()
    # g.remove_edge(1, 4)
