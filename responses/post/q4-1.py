To count islands in a grid, we can iterate through each cell in the grid. If a cell is a 1 and has not been visited, we can explore the adjacent cells to determine the size of the island. After exploring the island, we mark the visited cells and continue to the next unvisited cell.

Here's the implementation of the count_islands() function:

```
def count_islands(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row, col) not in visited:
                explore(grid, row, col, visited)
                count += 1
                reset_grid(grid, visited)
    return count
```

In this implementation, we use a set called `visited` to store the visited cells, and a variable `count` to keep track of the number of islands.

Inside the nested for loop, if we encounter a cell with value 1 and it has not been visited, we call the `explore()` function to explore the island. After exploring, we increment the `count` variable and reset the visited cells in the grid using the `reset_grid()` function.

Note that the `explore()` function is already provided and performs a depth-first search to explore neighboring cells.

Hope this helps! Let me know if you have any questions.

 tokens:290