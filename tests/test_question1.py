
test_cases = [
    ([20, 10, 30, 5, 15, 25, 35], 15, 20),  # Test in-between values
    ([50, 30, 70, 20, 40, 60, 80], 65, 70),  # Test value between nodes
    ([40, 20, 10, 30, 60, 50, 70], 40, 50),  # Test exact match
    ([15, 10, 20, 8, 12, 16, 25], 17, 20),   # Test no direct successor
    ([10, 5, 3, 7, 20, 15, 30], 20, 30),     # Test right subtree
    ([30, 20, 40, 10, 25, 35, 50], 25, 30),  # Test left subtree
    ([5, 3, 8, 2, 4, 6, 10], 1, 2),          # Test lower boundary
    ([8, 7, 9], 9, None),                    # Test upper boundary
    ([10, 5, 15, 2, 7, 12, 18, 1], 15, 18),  # Test middle value
    ([100, 50, 150, 25, 75, 125, 175], 160, 175) # Test value close to upper boundary
]

def run_tests():
    for i, (elements, v, expected) in enumerate(test_cases, 1):
        tree = build_tree(elements)
        next_node = find_next(tree, v)
        actual = next_node.val if next_node else None
        assert actual == expected, f"Test case {i} failed: expected {expected}, got {actual}"
        print(f"Test case {i} passed.")

# Assuming build_tree and find_next functions are defined above
run_tests()