Write the count_islands() function to calculate how many islands appear in a grid. Islands are made up of connected 1s (land) and are surrounded by 0s (water). Use the given helper functions to aid in your task. Your function should return the count of these islands.

def explore(grid, row, col, visited):
    if (row, col) in visited or row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] == 0:
        return
    visited.add((row, col))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dr, dc in directions:
        explore(grid, row + dr, col + dc, visited)

def count_islands(grid):
    pass

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def reset_grid(grid, visited):
    for row, col in visited:
        if is_valid(grid, row, col):
            grid[row][col] = 1

def is_isolated(grid, row, col):
    return all(grid[r][c] == 0 for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] for r, c in [(row + dr, col + dc)] if is_valid(grid, r, c))

def copy_grid(grid):
    return [row[:] for row in grid]

def flood_fill(grid, row, col, target, replacement):
    if not is_valid(grid, row, col) or grid[row][col] != target:
        return
    grid[row][col] = replacement
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        flood_fill(grid, row + dr, col + dc, target, replacement)

def find_land(grid):
    return next(((r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 1), None)

def perimeter(grid, row, col):
    if not is_valid(grid, row, col) or grid[row][col] == 0:
        return 0
    mark = 'v'
    grid[row][col] = mark
    perim = 4
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if is_valid(grid, nr, nc) and grid[nr][nc] == 1:
            perim -= 1
            perim += perimeter(grid, nr, nc)
    return perim

def replace(grid, target, replacement):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == target:
                grid[row][col] = replacement