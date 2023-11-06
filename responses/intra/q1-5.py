To implement the `find_next` function, we need to perform an inorder traversal of the binary search tree and keep track of the last visited node with a larger value than the input variable `v`. Here's the implementation:

```python
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
```

The `find_next` function takes three arguments - the `root` node of the binary search tree, the input variable `v`, and the `succ` (successor) node which is initially set to `None`.

To find the next highest integer value in the binary search tree, we iterate through the tree using an inorder traversal. If the value of the current node is greater than `v`, we update the `succ` node and recurse on the left subtree. This is because the successor node could potentially be in the left subtree. If the value of the current node is less than or equal to `v`, we recurse on the right subtree. This is because the next highest value will necessarily be in the right subtree (if it exists).

Finally, we return the `succ` node as the result.

The `build_tree` function is provided to build a binary search tree from an input array of values. It uses the `insert` function to insert each value into the tree and returns the root node of the constructed tree.

 tokens:370