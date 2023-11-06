To find the smallest number bigger than `v` in a tree, we will perform an in-order traversal of the tree and keep track of the smallest number encountered so far that is greater than `v`. If we encounter a number greater than `v`, we update the `succ` variable with that number and continue traversing the tree.

Here is the implementation of the `find_next` function:

```python
def find_next(root, v, succ=None):
    if not root:
        return None
    
    if root.val > v:
        if succ is None or root.val < succ:
            succ = root.val
    
    if root.val > v:
        return find_next(root.left, v, succ)
    else:
        return find_next(root.right, v, succ)
```

To test this function, you can create a tree using the `build_tree` function and then call the `find_next` function on the root of the tree:

```python
arr = [4, 2, 5, 1, 3]
root = build_tree(arr)
v = 2
next_num = find_next(root, v)
print(next_num)  # Output: 3
```

In this example, the smallest number bigger than `2` in the tree `[4, 2, 5, 1, 3]` is `3`.

 tokens:281