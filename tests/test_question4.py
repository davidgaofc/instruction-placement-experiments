from response_form_clean.pre import q4_1 as pre1
from response_form_clean.pre import q4_2 as pre2
from response_form_clean.pre import q4_3 as pre3
from response_form_clean.pre import q4_4 as pre4
from response_form_clean.pre import q4_5 as pre5

from response_form_clean.post import q4_1 as post1
from response_form_clean.post import q4_2 as post2
from response_form_clean.post import q4_3 as post3
from response_form_clean.post import q4_4 as post4
from response_form_clean.post import q4_5 as post5

from response_form_clean.intra import q4_1 as intra1
from response_form_clean.intra import q4_2 as intra2
from response_form_clean.intra import q4_3 as intra3
from response_form_clean.intra import q4_4 as intra4
from response_form_clean.intra import q4_5 as intra5

import json

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
def run_tests(function):
    counter = 0
    for i, (grid, expected) in enumerate(test_cases, 1):
        try:
            result = function.count_islands(grid)
            if(result == expected):
                counter += 1
            else:
                print(f"Test case {i} failed.")
        except:
            pass
    return counter
# Run the tests
test_iterator = {"pre": [pre1, pre2, pre3, pre4,pre5], "post": [post1, post2, post3, post4,post5], "intra": [intra1, intra2, intra3, intra4,intra5]}

results = {}
for key, value in test_iterator.items():
    results[key] = []
    for i in value:
        results[key].append(run_tests(i))

print(results)
try:
    with open('results/question4.json', 'w') as json_file:
        json.dump(results, json_file)
except:
    print("failed to write")