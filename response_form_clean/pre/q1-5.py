Implement the find_next function to systematically traverse the binary search tree from root to uncover the immediate successor element that contains a larger numeric value than the input variable v. The algorithm should meticulously search and discover the next highest integer value within the binary search tree's structure; if such an element is non-existent, the function must generate a None type.

class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v; self.left = l; self.right = r

def insert(root, v):
    if not root: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def find_next(root, v, succ=None):
    pass

def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r