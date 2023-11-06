Here's the implementation of the `count_islands()` function:

```python
def count_islands(grid):
    visited = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                islands += 1
                explore(grid, row, col, visited)
    return islands
```

This function uses a set `visited` to keep track of the visited cells. It iterates through each cell in the grid and if the cell value is 1 and it hasn't been visited, it increments the `islands` count and calls the `explore()` function to explore the island. Finally, it returns the count of islands.

You can use this `count_islands()` function to calculate the number of islands in a given grid.

 tokens:184