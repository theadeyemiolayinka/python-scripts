from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def BFS(self, s):
        visited = set()
        queue = deque()

        visited.add(s)
        queue.append(s)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

# Usage
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Breadth First Traversal starting from vertex 2:")
g.BFS(2)
