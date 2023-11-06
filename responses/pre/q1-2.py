To find the smallest number larger than v in a binary search tree, we can implement an iterative approach using an inorder traversal.

Here's the updated code:

```python
class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def insert(root, v):
    if not root:
        return Node(v)
    if v < root.val:
        root.left = insert(root.left, v)
    else:
        root.right = insert(root.right, v)
    return root

def find_next(root, v):
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
    for x in arr:
        r = insert(r, x)
    return r
```

The `find_next` function traverses the BST in an inorder manner and updates the `succ` variable whenever a larger value than `v` is encountered. If no such value is found, `succ` remains None. Finally, the `val` of the variable `succ` is returned if it exists, otherwise None is returned.

You can use the `build_tree` function to build a test BST and then pass it to the `find_next` function to find the smallest number larger than `v`.

 tokens:305