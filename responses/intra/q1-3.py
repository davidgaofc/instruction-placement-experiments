To implement the `find_next` function, we can use a recursive approach. 

Here's the plan for the `find_next` function:
1. If the root node is None, return succ (which will be None if no larger element is found).
2. If the root value is less than or equal to v, recursively search the right subtree with the current root as the successor since the current root value is not greater than v.
3. If the root value is greater than v, set succ to the current root and recursively search the left subtree. This is because the current root is a potential successor as it is greater than v, but we need to check if there is a smaller successor in the left subtree.
4. Finally, return the result of the recursive calls.

Here's the updated code for the `find_next` function:

```
def find_next(root, v, succ=None):
    if not root:
        return succ
    
    if root.val <= v:
        return find_next(root.right, v, succ)
    else:
        return find_next(root.left, v, root)
```

Now, let's test the code with an example:

```python
arr = [4, 2, 6, 1, 3, 5, 7]
root = build_tree(arr)
v = 4

print(find_next(root, v).val)  # Output: 5

v = 7
print(find_next(root, v))  # Output: None
```

In the given example, the smallest element in the binary search tree that remains larger than 4 is 5. When searching for the next element after 7 (which is the largest element in the tree), there is no larger element, so the output is None.

 tokens:364