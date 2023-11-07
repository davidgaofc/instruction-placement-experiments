class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v; self.left = l; self.right = r

def insert(root, v):
    if not root: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def find_next(root, v, succ=None):
    curr = root
    successor = succ

    while curr:
        if v < curr.val:
            successor = curr
            curr = curr.left
        else:
            curr = curr.right

    return successor.val if successor else None
def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r

