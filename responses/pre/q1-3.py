Here's the implementation of the `find_next` function:

```
def find_next(root, v, succ=None):
    if not root:
        return succ
    if root.val <= v:
        return find_next(root.right, v, succ)
    else:
        return find_next(root.left, v, root.val)
```

Explanation:
- The `find_next` function takes in the root of the binary search tree (`root`), the value to compare (`v`), and the current successor (`succ`) as parameters.
- If the root is None, it means we have reached the end of the tree and there is no element larger than `v`. In this case, we return the current successor (`succ`).
- If the value of the root is less than or equal to `v`, it means that the smallest element larger than `v` must be in the right subtree. We recursively call `find_next` with the right subtree as the new root, `v` unchanged, and `succ` unchanged.
- If the value of the root is greater than `v`, it means that the smallest element larger than `v` could be either the root itself or in the left subtree. We recursively call `find_next` with the left subtree as the new root, `v` unchanged, and the value of the root as the new `succ`.
- By recursively calling `find_next`, we traverse down the tree until we find the smallest element larger than `v`.
- The function returns the smallest element larger than `v` or None if it doesn't exist.

Hope this helps! Let me know if you have any questions.

 tokens:335