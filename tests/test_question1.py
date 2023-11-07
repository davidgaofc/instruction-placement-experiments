from response_form_clean.pre import q1_1 as pre1
from response_form_clean.pre import q1_2 as pre2
from response_form_clean.pre import q1_3 as pre3
from response_form_clean.pre import q1_4 as pre4
from response_form_clean.pre import q1_5 as pre5

from response_form_clean.post import q1_1 as post1
from response_form_clean.post import q1_2 as post2
from response_form_clean.post import q1_3 as post3
from response_form_clean.post import q1_4 as post4
from response_form_clean.post import q1_5 as post5

from response_form_clean.intra import q1_1 as intra1
from response_form_clean.intra import q1_2 as intra2
from response_form_clean.intra import q1_3 as intra3
from response_form_clean.intra import q1_4 as intra4
from response_form_clean.intra import q1_5 as intra5

import json

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

def run_tests(function):
    counter = 0
    for i, (elements, v, expected) in enumerate(test_cases, 1):
        try:
            tree = function.build_tree(elements)
            next_node = function.find_next(tree, v)
            actual = next_node.val if next_node else None
            if(actual == expected):
                counter += 1
            else:
                print(f"Test {i} failed. Expected {expected}, got {actual}")
        except:
            pass
    return counter

test_iterator = {"pre": [pre1, pre2, pre3, pre4,pre5], "post": [post1, post2, post3, post4,post5], "intra": [intra1, intra2, intra3, intra4,intra5]}

results = {}
for key, value in test_iterator.items():
    results[key] = []
    for i in value:
        results[key].append(run_tests(i))

print(results)
try:
    with open('results/question1.json', 'w') as json_file:
        json.dump(results, json_file)
except:
    print("failed to write")