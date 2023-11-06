Here's the implementation of the `find_next` function:

```python
def find_next(root, v, succ=None):
    if not root:
        return None

    if root.val <= v:
        return find_next(root.right, v, succ)
    else:
        succ = root
        return find_next(root.left, v, succ) or succ

```

In this function, we recursively traverse the tree starting from the root and update the current smallest number larger than `v` as we go. 

If the value of the current node is less than or equal to `v`, we continue searching in the right subtree to find a larger number. If the value is greater than `v`, we update the successor value to the current node and continue searching in the left subtree. This process continues until we reach a leaf node or the value is found. 

If no successor is found (i.e., no number larger than `v` exists in the tree), we return `None`. Otherwise, we return the successor value.

 tokens:210