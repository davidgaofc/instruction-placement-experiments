Here is the missing implementation for the `find_next` function:

```python
def find_next(root, v, succ=None):
    if not root:
        return succ
    if root.val > v:
        succ = root
        return find_next(root.left, v, succ)
    else:
        return find_next(root.right, v, succ)
```

This function recursively traverses the binary search tree to find the smallest element that is greater than `v`. It keeps track of the potential successor (`succ`) while traversing. If the current node's value is greater than `v`, it updates the potential successor and continues searching in the left subtree. If the current node's value is less than or equal to `v`, it continues searching in the right subtree. If there is no superior element, the function returns `None`.

Also, here is an example usage of the functions:

```python
arr = [5, 3, 8, 2, 4, 7, 9, 1, 6]
root = build_tree(arr)
v = 5
successor = find_next(root, v)
if successor:
    print(successor.val)
else:
    print("No superior element found")
```

This will output `6`, which is the smallest element greater than `5` in the binary search tree.

 tokens:276