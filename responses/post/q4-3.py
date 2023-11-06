To solve this problem, we can use a depth-first search (DFS) algorithm to explore the grid and mark visited cells. 

The count_islands() function can be implemented as follows:

1. Initialize a set called "visited" to keep track of visited cells.
2. Initialize a variable called "count" to keep track of the number of islands.
3. Iterate through each cell in the grid.
4. If the cell is not visited and contains '1' (land), increment the count and call the explore() function with the current cell's coordinates, the grid, and the visited set.
5. Implement the explore() function as follows:
   - If the current cell is visited or out of bounds, or if it contains '0' (water), return.
   - Add the current cell to the visited set.
   - Define a list of directions that represent the adjacent cells: up, down, left, right.
   - Iterate through each direction:
     - Calculate the neighboring cell's coordinates by adding the direction to the current cell's coordinates.
     - Call the explore() function recursively with the neighboring cell's coordinates, the grid, and the visited set.
6. Return the count.

Here is the implementation:

```python
def explore(grid, row, col, visited):
    if (row, col) in visited or row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] == '0':
        return
    visited.add((row, col))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        explore(grid, row + dr, col + dc, visited)

def count_islands(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == '1':
                count += 1
                explore(grid, row, col, visited)
    return count
```

Note: In this implementation, we assume that the grid is a list of lists representing a 2D grid. Each cell contains either '0' or '1'.

 tokens:470