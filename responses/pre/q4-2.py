One possible solution for the count_islands() function is as follows:

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
In this solution, we initialize an empty set called "visited" to keep track of visited cells. We also initialize a variable "islands" to keep track of the count of islands found.

We then iterate through each cell in the grid using nested loops. If a cell contains a 1 and has not been visited yet, we increment the islands count and call the explore() function to recursively explore the connected land cells and mark them as visited.

After visiting all cells in the grid, we return the count of islands.

 tokens:200