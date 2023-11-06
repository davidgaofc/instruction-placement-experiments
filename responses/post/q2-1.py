Here is the code for the `findShortestPath` method:

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

In this method, we use a breadth-first search (BFS) algorithm to find the shortest path between the source vertex `s` and the destination vertex `d`.

First, we create a `visited` list to track the visited vertices and a `queue` to store the vertices to be visited. We initialize both lists with `False` values.

We set `visited[s] = True` to mark the source vertex as visited, and we add `(s, 0)` to the `queue` to indicate that we are starting from the source vertex and the distance is 0.

Then, we enter a `while` loop that continues until the `queue` is empty. In each iteration of the loop, we dequeue a vertex `v` and its corresponding distance `dist` from the front of the `queue`.

If `v` is equal to the destination vertex `d`, we have reached the destination and we return the distance `dist` as the shortest path.

Otherwise, for each adjacent vertex `i` of `v`, if `i` has not been visited yet, we enqueue `(i, dist + 1)` to the `queue` to explore it in the next iterations. We also mark `visited[i] = True` to indicate that we have visited `i`.

If we have not found the destination vertex during the BFS, we return `float('inf')` to indicate that there is no path between the source and destination vertices.

Note that this method returns the shortest path in terms of the number of steps taken, not the actual path itself. If you need to obtain the path as a list of vertices, you can modify the code to keep track of the parent of each vertex during the BFS.

 tokens:470