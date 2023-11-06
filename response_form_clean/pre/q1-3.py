Develop the function find_next to identify the smallest element in a binary search tree that remains larger than the given value v. Begin your search at the root. If there doesn't exist a larger element, the implemented function should return None.

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