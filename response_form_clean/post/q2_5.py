class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def findShortestPath(self, s, d):
        visited = [False] * self.V
        queue = [(s, -1)]  # Use -1 as the initial previous vertex for the source vertex
        visited[s] = True
        prev = {}  # Dictionary to store the previous vertex for each visited vertex
        while queue:
            v, prev_v = queue.pop(0)
            if v == d:
                break
            for i in self.adj[v]:
                if not visited[i]:
                    visited[i] = True
                    prev[i] = v  # Store the previous vertex for i
                    queue.append((i, v))

        if d not in prev:
            return []  # No path exists between s and d

        path = []
        current = d
        while current != -1:  # Reconstruct the shortest path from d to s
            path.append(current)
            current = prev.get(current, -1)

        path.reverse()  # Reverse the path to get the shortest path from s to d
        return path

    def BFS(self, s, d):
        visited = [False] * self.V
        queue = [(s, 0)]
        visited[s] = True
        while queue:
            v, dist = queue.pop(0)
            if v == d:
                return dist
            for i in self.adj[v]:
                if not visited[i]:
                    queue.append((i, dist + 1))
                    visited[i] = True
        return float('inf')

    def printAllPaths(self, s, d):
        visited = [False] * self.V
        path = []
        self._printAllPathsUtil(s, d, visited, path)

    def _printAllPathsUtil(self, u, d, visited, path):
        visited[u], path = True, path + [u]
        if u == d:
            print(path)
        else:
            for i in self.adj[u]:
                if not visited[i]:
                    self._printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False
