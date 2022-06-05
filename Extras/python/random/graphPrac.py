from collections import defaultdict, deque


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def print_graph(self):
        print(self.graph)

    def dfs(self, src, discovered, visited):
        if not visited[src]:
            discovered.append(src)
            visited[src] = True
            for u in self.graph[src]:
                self.dfs(u, discovered, visited)

    def iterative_dfs(self, discovered, visited):
        stack = []
        for src in range(self.V):
            # if not visited[src]:
            stack.append(src)
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    discovered.append(u)
                    for v in self.graph[u]:
                        stack.append(v)

    def bfs(self, discovered, visited):
        q = deque([])
        for src in range(self.V):
            q.appendleft(src)
            while q:
                u = q.pop()
                if not visited[u]:
                    visited[u] = True
                    discovered.append(u)
                    for v in self.graph[u]:
                        q.appendleft(v)

    def dfsCycle(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v]:
                return True
            elif self.dfsCycle(v, visited):
                return True
        return False

    def isCyclic(self):
        visited = [False]*self.V
        for u in range(self.V):
            if not visited[u]:
                return self.dfsCycle(u, visited)
        return False

    # def dfsCycle1(self, u, visited):
    #     if visited[u] == 2:
    #         return True
    #     visited[u] = 1
    #     for v in self.graph[u]:
    #         if visited[v] == 1:
    #             visited[v] += 1
    #         if self.dfsCycle1(v, visited):
    #             return True
    #     return False

    # def isCyclic(self):  # for undirected graph
    #     visited = [0]*self.V
    #     # 0,1,2 = white,gray,black (graph coloring)
    #     for u in range(self.V):
    #         if not visited[u]:
    #             return self.dfsCycle1(u, visited)
    #     return False

    def isBipartite(self):
        q = deque([])
        color = [-1]*self.V
        # color[0] = 1
        for src in range(self.V):
            q.appendleft(src)
            while q:
                u = q.pop()
                color[u] = 1
                if color[u] == -1:
                    for v in self.graph[u]:
                        if color[v] == color[u]:
                            return False
                        q.appendleft(v)
                        color[v] = 1 - color[u]
        return True

    def topDfs(self, u, visited, ans):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.topDfs(v, visited, ans)
        ans.appendleft(u)

    def rectopologicalSort(self):
        visited = [False]*self.V
        ans = deque([])

        for u in range(self.V):
            if not visited[u]:
                self.topDfs(u, visited, ans)
        return ans

    def topologicalSort(self):
        q = deque([])
        indegree = [0]*self.V
        topologicalOrder = []
        for u in range(self.V):
            for v in self.graph[u]:
                indegree[v] += 1
        for u, indeg in enumerate(indegree):
            if indeg == 0:
                q.appendleft(u)
        visited = 0
        while q:
            u = q.pop()
            visited += 1
            topologicalOrder.append(u)
            for v in self.graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.appendleft(v)
        if visited != self.V:
            print("Cycle detected")
        return topologicalOrder

    def UnionFind(self):
        parent = [-1]*self.V
        for u in range(self.V):
            for v in self.graph[u]:
                parent[v] = u
        print(parent)

        def find(v):
            if parent[v] == -1:
                return v
            return find(parent[v])

        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parent[pu] = pv


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 3)
    g.add_edge(0, 2)
    g.add_edge(3, 1)
    g.add_edge(4, 1)
    g.add_edge(4, 2)
    g.add_edge(5, 0)
    g.add_edge(5, 2)
    # g.add_edge(2, 3)
    # g.add_edge(3, 3)
    g.print_graph()
    print()
    discovered = []
    # g.iterative_dfs(discovered, [False, False, False, False, False, False])
    g.bfs(discovered, [False, False, False, False, False, False])
    print(discovered)
    print("Graph contains cycle" if g.isCyclic()
          else "Graph doesn't contains cycle")
    print("Graph is bipartite" if g.isBipartite()
          else "Graph is not bipartite.")
    print(g.topologicalSort())
    print(g.UnionFind())
    # g.topologicalSortBfs()
