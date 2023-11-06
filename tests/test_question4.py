test_cases = [
    # Test case 1: No land
    ([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ], 0),

    # Test case 2: One big island
    ([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ], 1),

    # Test case 3: One single land
    ([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ], 1),

    # Test case 4: Two separate lands
    ([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ], 2),

    # Test case 5: A complex map
    ([
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ], 5),

    # Test case 6: Single row
    ([
        [0, 1, 0, 1, 0, 1, 0]
    ], 3),

    # Test case 7: Single column
    ([
        [0],
        [1],
        [0],
        [1],
        [0],
        [1]
    ], 3),

    # Test case 8: Diagonals don't connect
    ([
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ], 3),

    # Test case 9: Water pools inside land
    ([
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ], 1),

    # Test case 10: Complex with varying island sizes
    ([
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ], 9),
]

# Function to run the test cases
def run_tests():
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = count_islands(grid)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed.")

# Run the tests
run_tests()