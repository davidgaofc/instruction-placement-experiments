from response_form_clean.pre import q2_1 as pre1
from response_form_clean.pre import q2_2 as pre2
from response_form_clean.pre import q2_3 as pre3
from response_form_clean.pre import q2_4 as pre4
from response_form_clean.pre import q2_5 as pre5

from response_form_clean.post import q2_1 as post1
from response_form_clean.post import q2_2 as post2
from response_form_clean.post import q2_3 as post3
from response_form_clean.post import q2_4 as post4
from response_form_clean.post import q2_5 as post5

from response_form_clean.intra import q2_1 as intra1
from response_form_clean.intra import q2_2 as intra2
from response_form_clean.intra import q2_3 as intra3
from response_form_clean.intra import q2_4 as intra4
from response_form_clean.intra import q2_5 as intra5

import json
def test_findShortestPath(function):
    graph = function.Graph(6)
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
    counter = 0
    for i, (s, d, expected) in enumerate(test_cases, 1):
        try:
            result = graph.findShortestPath(s, d)
            if(type(result) == list):
                # print("list", result, expected)
                if(result == expected):
                    counter += 1
            elif(type(result) == int):
                # print("int", result, expected)
                if(result == len(expected)-1):
                    counter += 1
            else:
                pass
                print(f"Test case {i} passed: expected {expected}, got {result}")
        except:
            pass
    return counter

test_iterator = {"pre": [pre1, pre2, pre3, pre4,pre5], "post": [post1, post2, post3, post4,post5], "intra": [intra1, intra2, intra3, intra4,intra5]}

results = {}
for key, value in test_iterator.items():
    results[key] = []
    for i in value:
        results[key].append(test_findShortestPath(i))

print(results)
try:
    with open('../results/question2.json', 'w') as json_file:
        json.dump(results, json_file)
except:
    print("failed to write")
