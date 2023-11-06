To implement the count_islands() function, we can perform a depth-first search (DFS) on the grid to explore all contiguous land masses. 

Here's an implementation of the count_islands() function:

```python
def count_islands(grid):
    visited = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1' and (row, col) not in visited:
                // Visit the land mass
                explore(grid, row, col, visited)
                // Increment the island count
                islands += 1
    // Reset the grid to the original state
    reset_grid(grid, visited)
    return islands
```

In this implementation, we iterate through each cell in the grid. If a cell contains '1' and has not been visited before, we initiate the exploration by calling the explore() function. We increment the island count by 1 after each exploration.

Finally, we reset the grid to the original state using the reset_grid() function and return the total number of islands detected.

Here's the complete code:

```python
def explore(grid, row, col, visited):
    if (row, col) in visited or row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] == '0':
        return
    visited.add((row, col))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        explore(grid, row + dr, col + dc, visited)

def count_islands(grid):
    visited = set()
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1' and (row, col) not in visited:
                explore(grid, row, col, visited)
                islands += 1
    reset_grid(grid, visited)
    return islands

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def reset_grid(grid, visited):
    for row, col in visited:
        if is_valid(grid, row, col):
            grid[row][col] = '1'

def is_isolated(grid, row, col):
    return all(grid[r][c] == '0' for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] for r, c in [(row + dr, col + dc)] if is_valid(grid, r, c))

def copy_grid(grid):
    return [row[:] for row in grid]

def flood_fill(grid, row, col, target, replacement):
    if not is_valid(grid, row, col) or grid[row][col] != target:
        return
    grid[row][col] = replacement
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        flood_fill(grid, row + dr, col + dc, target, replacement)

def find_land(grid):
    return next(((r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == '1'), None)

def perimeter(grid, row, col):
    if not is_valid(grid, row, col) or grid[row][col] == '0':
        return 0
    mark = 'v'
    grid[row][col] = mark
    perim = 4
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if is_valid(grid, nr, nc) and grid[nr][nc] == '1':
            perim -= 1
            perim += perimeter(grid, nr, nc)
    return perim

def replace(grid, target, replacement):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == target:
                grid[row][col] = replacement
```

 tokens:904