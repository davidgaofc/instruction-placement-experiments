To count the number of distinct islands in a given 2D grid, we can use a depth-first search (DFS) algorithm to explore each island. 

In the count_islands() function, we will create a set to keep track of the visited cells. Then, we will iterate through each cell in the grid and if the cell is a land (1) and has not been visited, we will call the explore() function to recursively explore and mark all the connected land cells.

Finally, we will return the number of islands, which is the size of the visited set.

Here is the implementation of the count_islands() function:

```python
def count_islands(grid):
    visited = set()
    islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == 1:
                explore(grid, row, col, visited)
                islands += 1

    return islands
```

Note: The explore() function is already provided as part of the helper functions.

You can now call the count_islands() function with a 2D grid to get the count of distinct islands.

 tokens:249