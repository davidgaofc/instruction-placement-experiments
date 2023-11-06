Create a function find_next that searches for the smallest number larger than v in a binary search tree starting from root. If there isn't one, return None.

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