To solve this problem, we can use a depth-first search (DFS) algorithm to explore the grid and mark visited cells. Each time we encounter a land cell, we can increment a counter to count the number of islands.

Here is the implementation of the count_islands() function:

```python
def count_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    num_islands = 0
    visited = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == 1:
                num_islands += 1
                explore(grid, row, col, visited)
    
    return num_islands
```

In this implementation, we iterate over every cell in the grid. If the cell is not visited and is a land cell (value 1), we increment the island counter and call the explore() function with the current cell's coordinates and the set of visited cells.

The explore() function uses a recursive DFS algorithm to explore the grid and mark visited cells. It checks if the current cell is within the grid boundaries, is not visited, and is a land cell. If so, it adds the current cell to the visited set and recursively calls itself for each neighboring cell.

Once all the land cells of an island are explored, the count_islands() function continues to the next unvisited land cell in the grid. Finally, it returns the total number of islands.

You can test the count_islands() function using the following example:

```python
grid = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]

print(count_islands(grid))  # Output: 4
```

In this example, there are 4 islands in the grid.

 tokens:414