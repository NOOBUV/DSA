from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def dfs(self, u, discovered, visited):
        if visited[u] == False:
            visited[u] = True
            discovered.append(u)
            for next in self.graph[u]:
                self.dfs(next, discovered, visited)

    def iterative_dfs(self, u, discovered, visited):
        stack = []
        stack.append(u)
        while len(stack) != 0:
            popped = stack.pop()
            if visited[popped] == True:
                continue
            visited[popped] = True
            discovered.append(popped)
            for next in self.graph[popped]:
                stack.append(next)

    def bfs(self, u, discovered, visited):
        queue = []
        queue.insert(0, u)
        while len(queue) != 0:
            popped = queue.pop()
            if visited[popped] == True:
                continue
            visited[popped] = True
            discovered.append(popped)
            for next in self.graph[popped]:
                queue.insert(0, next)

    def dfsCycle(self, u, color):
        color[u] = "gray"
        for v in self.graph[u]:
            if color[v] == "gray":
                return True
            elif color[v] == "white" and self.dfsCycle(v, color) == "black":
                return True
        color[u] = "black"
        return False

    def isCyclic(self):
        color = ["white"]*self.V
        for i in range(self.V):
            if color[i] == "white":
                if self.dfsCycle(i, color) == True:
                    return True
        return False

    def isBipartite(self):
        queue = []
        queue.append(0)
        color = [-1]*self.V
        color[0] = 1
        while len(queue) != 0:
            u = queue.pop(0)
            for v in self.graph[u]:
                if color[v] == -1:
                    color[v] = 1-color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
            if len(queue) == 0:
                for u in color:
                    if color[u] == -1:
                        queue.append(u)
                        color[u] = 1

            return True

    def topologicalDfs(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] == False:
                self.topologicalDfs(v, visited, stack)
        stack.append(u)

    def topologicalSorting(self):
        visited = [False]*self.V
        stack = []

        for u in range(self.V):
            if visited[u] == False:
                self.topologicalDfs(u, visited, stack)

        print(stack)

    def topologicalSortBfs(self):
        indegree = [0]*self.V
        queue = []
        topologicalOrder = []

        # filling indegree
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1
        # filling nodes with 0 indegree
        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)
        # processing queue
        visited = 0
        while len(queue) != 0:
            u = queue.pop(0)
            visited += 1
            topologicalOrder.append(u)
            for v in self.graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if visited != self.V:
            print("cyclic graph")

        print(topologicalOrder)

    def unionFind(self):
        # class tupArr:
        #     def __init__(self,index):
        #         self.arr = [(-1,-1)]
        #         self.index = index
        #     def parent(self,value):
        #         self.arr[self.index][0] = value
        #         return self.arr[self.index][0]
        #     def range(self,rvalue):
        #         self.arr[self.index][1] = rvalue
        #         return self.arr[self.index][1]
        def find(parent, u):
            if parent[u] != u:
                parent[u] = find(parent, parent[u])
            return parent[u]

        def union(parent, u, v):
            uParent = find(parent, u)
            vParent = find(parent, v)
            parent[uParent] = vParent

        def pathCompfind(subsets, index):
            if subsets[index].parent != index:
                subsets[index].parent = find(subsets, subsets[i].parent)
            return subsets[index].parent

        def rankUnion(subsets, uroot, vroot):
            if subsets[uroot].rank < subsets[vroot].rank:
                subsets[uroot].parent = vroot
            elif subsets[uroot].rank > subsets[vroot].rank:
                subsets[vroot].parent = uroot
            else:
                subsets[vroot].parent = uroot
                subsets[uroot].rank += 1


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
    # discovered = []
    # g.dfs(0, discovered, [False, False, False, False])
    # g.bfs(0, discovered, [False, False, False, False])
    # print(discovered)
    # print("Graph contains cycle" if g.isCyclic()
    #       else "Graph doesn't contains cycle")
    print("Graph is bipartite" if g.isBipartite()
          else "Graph is not bipartite.")
    g.topologicalSortBfs()
