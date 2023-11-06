class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def findShortestPath(self, s, d):
        visited = [False] * self.V
        queue = [(s, [s])]
        visited[s] = True
        while queue:
            v, path = queue.pop(0)
            if v == d:
                return path
            for i in self.adj[v]:
                if not visited[i]:
                    queue.append((i, path + [i]))
                    visited[i] = True
        return []

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

 tokens:274