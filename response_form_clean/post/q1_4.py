class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v; self.left = l; self.right = r

def insert(root, v):
    if not root: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def find_next(root, v, succ=None):
    if not root:
        return None

    if v <= root.val:
        return find_next(root.left, v, root)

    return find_next(root.right, v, succ) or succ or find_next(root.right.left, v, succ)

def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r
