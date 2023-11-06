Here is an implementation of the `find_next` function to find the smallest number bigger than `v` in a binary search tree:

```python
def find_next(root, v, succ=None):
    if not root:
        return succ
    
    if root.val > v:
        return find_next(root.left, v, root)
    else:
        return find_next(root.right, v, succ)
```

This function uses a recursive approach to traverse the tree. It compares the value of the current node `root` with `v`. If `root.val` is greater than `v`, it means there might be a smaller successor in the left subtree, so it recursively calls `find_next` on the left child with `root` as the new successor. If `root.val` is less than or equal to `v`, it means the smaller successor can be present in the right subtree or it may not exist at all. In this case, it recursively calls `find_next` on the right child with the current successor `succ` unchanged.

By starting at the root and following the appropriate path based on the value of `v`, the function will eventually find the smallest number greater than `v`. If no such number exists, the function will return `None`.

Note: This implementation assumes that the tree is a binary search tree where the left child of a node contains values less than the node, and the right child contains values greater than the node.

 tokens:294