To find the shortest path using the fewest steps from point 's' to point 'd', we can modify the BFS algorithm in the `findShortestPath` method. Here's the updated code:

```python
def findShortestPath(self, s, d):
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
```

In this modified BFS algorithm, we keep track of the distance from the starting point 's' to each point 'v' in the `dist` variable. The algorithm terminates once the destination point 'd' is reached and returns the minimum distance.

Make sure to add this code to the `Graph` class after the existing methods.

 tokens:213