To find the smallest number larger than v in a binary search tree, we can perform an in-order traversal of the tree starting from the root node and keep track of the successor node.

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

def find_next(root, v, succ=None):
    if not root:
        return succ
    
    if root.val <= v:
        return find_next(root.right, v, succ)
    else:
        return find_next(root.left, v, root)

def build_tree(arr):
    r = None
    for x in arr:
        r = insert(r, x)
    return r

# Example usage:
arr = [5, 3, 8, 2, 7, 4]
root = build_tree(arr)

print(find_next(root, 6))  # Output: 7
print(find_next(root, 8))  # Output: None
```

In the `find_next` function, we traverse the tree recursively. If the current node's value is less than or equal to `v`, we continue searching in the right subtree, as the successor to `v` must be in the right subtree. If the current node's value is greater than `v`, we update the `succ` variable to the current node and continue searching in the left subtree, as there may still be a smaller successor node in the left subtree. Finally, if there is no successor node (i.e. `root` is None), we return the `succ` variable.

 tokens:394