To find the quickest route from 's' to 'd', we can modify the BFS algorithm to keep track of the shortest distance from 's' to each vertex and the previous vertex that leads to it. Then, we can backtrack from 'd' to 's' using the previous vertices to find the shortest path.

Here is the modified 'findShortestPath' method:

def findShortestPath(self, s, d):
    visited = [False] * self.V
    queue = [(s, 0)]
    previous = [-1] * self.V
    visited[s] = True
    while queue:
        v, dist = queue.pop(0)
        if v == d:
            path = []
            while v != -1:
                path.append(v)
                v = previous[v]
            return path[::-1]
        for i in self.adj[v]:
            if not visited[i]:
                queue.append((i, dist + 1))
                visited[i] = True
                previous[i] = v
    return []

In this modified BFS algorithm, we added the 'previous' list to keep track of the previous vertex that leads to each vertex while traversing the graph. 
When we reach the destination 'd', we backtrack from 'd' to 's' using the 'previous' list to find the shortest path by appending the vertices in reverse order.
Finally, we return the reversed 'path' to get the shortest path from 's' to 'd'.

Note: If there is no path from 's' to 'd', the method will return an empty list.

 tokens:328