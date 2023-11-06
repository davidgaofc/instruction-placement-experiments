To find the shortest path from node 's' to node 'd', we can use Dijkstra's algorithm. Here's the implementation:

1. Create a distance array dist[] and initialize all elements to infinity except for dist[s], which is initialized to 0. dist[i] represents the shortest distance from node 's' to node 'i'.
2. Create a priority queue minHeap and insert node 's' with distance 0 into the queue.
3. While minHeap is not empty, do the following:
   - Extract the node with the minimum distance from minHeap. Let's call this node 'u'.
   - For each neighbor 'v' of 'u', do the following:
     - Calculate the distance from node 's' to neighbor 'v' through node 'u'. Let's call this distance 'new_dist'.
     - If 'new_dist' is less than the current distance dist[v], update dist[v] to 'new_dist' and insert neighbor 'v' into minHeap with distance 'new_dist'.
4. After the loop ends, dist[d] will contain the shortest path distance from node 's' to node 'd'.

Here's the updated code with the implementation of the 'findShortestPath' function:

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def findShortestPath(self, s, d):
        dist = [float('inf')] * self.V
        dist[s] = 0

        minHeap = [(0, s)]

        while minHeap:
            curr_dist, u = heapq.heappop(minHeap)
            if u == d:
                return curr_dist

            for v in self.adj[u]:
                new_dist = curr_dist + 1
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(minHeap, (new_dist, v))

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

Note that we are using heapq module to implement the priority queue. You need to import heapq at the beginning of the code.

 tokens:583