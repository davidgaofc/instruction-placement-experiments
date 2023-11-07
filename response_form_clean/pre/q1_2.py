
class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v; self.left = l; self.right = r

def insert(root, v):
    if not root: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def find_next(root, v, succ=None):
    succ = None
    while root:
        if v < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ.val if succ else None

def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r