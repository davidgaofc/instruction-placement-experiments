To implement the `find_next` function, we can use the following steps:

1. Initialize a variable `curr` to keep track of the current node in the tree, starting with the root.
2. Initialize a variable `successor` to None.
3. Loop until `curr` is not None:
   - If `v` is less than the current node's value (`curr.val`), update `successor` to the current node (`curr`) and move to the left child of the current node (`curr = curr.left`).
   - Otherwise, move to the right child of the current node (`curr = curr.right`).
4. At the end of the loop, `successor` will either be the smallest number larger than `v` or None if there isn't one. Return `successor`.

Here's the updated code for the `find_next` function:

```python
def find_next(root, v, succ=None):
    curr = root
    successor = succ

    while curr:
        if v < curr.val:
            successor = curr
            curr = curr.left
        else:
            curr = curr.right

    return successor.val if successor else None
```

You can then use this function in your code wherever you need to find the next smallest number.

 tokens:265