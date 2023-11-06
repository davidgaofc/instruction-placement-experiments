Here is the implementation of the `find_next` function:

```python
def find_next(root, v, succ=None):
    if root is None:
        return None
    
    if root.val > v:
        succ = root
        return find_next(root.left, v, succ)
    else:
        return find_next(root.right, v, succ) if root.right else succ
```

Explanation:
1. We start by checking if the root node is None. If it is, there are no elements in the tree so we simply return None.
2. If the value of the root node is greater than the input variable `v`, we update the `succ` variable to be the current root node and recursively call `find_next` on the left subtree to potentially find a smaller successor value.
3. If the value of the root node is less than or equal to `v`, we recursively call `find_next` on the right subtree. If there is no right subtree (i.e., the current node is the rightmost node), we return the `succ` variable which contains the next highest integer value.

To test the implementation, you can use the `build_tree` function to construct a binary search tree and then call `find_next` on the root node:

```python
arr = [5, 3, 8, 2, 4, 7, 9]
root = build_tree(arr)
v = 6
successor = find_next(root, v)
print(successor.val) if successor else print(None)
```

This will output `7` since it is the next highest value in the tree after `6`.

 tokens:337