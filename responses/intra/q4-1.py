To count the number of islands in a grid, we can use a depth-first search (DFS) approach. Here is the updated code for the `count_islands()` function:

```python
def explore(grid, row, col, visited):
    if (row, col) in visited or row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] == 0:
        return
    visited.add((row, col))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dr, dc in directions:
        explore(grid, row + dr, col + dc, visited)

def count_islands(grid):
    visited = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                explore(grid, row, col, visited)
                islands += 1
    return islands
```

In the `count_islands()` function, we initialize a set `visited` to keep track of visited cells. We then iterate over each cell in the grid and if it is a 1 and has not been visited before, we call the `explore()` function to perform a DFS and mark all connected 1s (island) as visited. We increment the `islands` count each time we find a new island. Finally, we return the total number of islands found.

Helper functions `is_valid()`, `reset_grid()`, `is_isolated()`, `copy_grid()`, `flood_fill()`, `find_land()`, `perimeter()`, and `replace()` remain the same and can be used as-is for other operations on the grid.

 tokens:406