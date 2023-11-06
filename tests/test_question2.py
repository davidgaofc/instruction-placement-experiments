
def test_findShortestPath():
    graph = Graph(6)
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
    for u, v in edges:
        graph.addEdge(u, v)

    test_cases = [
        (0, 4, [0, 1, 4]),
        (0, 5, [0, 3, 5]),
        (5, 0, [5, 3, 0]),
        (1, 3, [1, 0, 3]),
        (2, 5, [2, 4, 5]),
        (0, 1, [0, 1]),
        (4, 3, [4, 1, 0, 3]),
        (1, 5, [1, 4, 5]),
        (2, 3, [2, 0, 3]),
        (5, 2, [5, 4, 2]),
    ]

    for i, (s, d, expected) in enumerate(test_cases, 1):
        result = graph.findShortestPath(s, d)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: expected {expected}, got {result}")


test_findShortestPath()