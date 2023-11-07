class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v; self.left = l; self.right = r

def insert(root, v):
    if not root: return Node(v)
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def find_next(root, v, succ=None):
    # Base case: if the root is None, return the successor node
    if not root:
        return succ

    # If the root value is equal to the input variable v
    # or greater than v, update the successor and recurse on the left subtree
    if root.val > v:
        succ = root
        return find_next(root.left, v, succ)

    # Otherwise, recurse on the right subtree
    return find_next(root.right, v, succ)
def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r

