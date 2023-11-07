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
        return succ

    if root.val == v:
        if root.right:
            # If the current node has a right child,
            # the next highest value must be in the right subtree
            succ = find_min(root.right)
        return succ

    elif root.val > v:
        # If the current node's value is greater than v,
        # the next highest value must be in the left subtree,
        # so update succ to the current node and recurse on the left subtree
        return find_next(root.left, v, root)

    else:
        # If the current node's value is less than v,
        # there may still be a larger value in the right subtree,
        # so just recurse on the right subtree
        return find_next(root.right, v, succ)

def build_tree(arr):
    r = None
    for x in arr: r = insert(r, x)
    return r

def find_min(root):
    # Helper function to find the minimum value in a BST
    if not root.left:
        return root
    return find_min(root.left)