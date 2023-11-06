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

    if root.val > v:
        if succ is None or root.val < succ:
            succ = root.val

    if root.val > v:
        return find_next(root.left, v, succ)
    else:
        return find_next(root.right, v, succ)
def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r

