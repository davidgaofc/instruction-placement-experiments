Here's an implementation of the find_next function:

```python
def find_next(root, v, succ=None):
    if not root:
        return succ
    
    if root.val == v:
        if root.right:
            # If the current node has a right child, 
            # the next highest value must be in the right subtree
            succ = find_min(root.right)
        return succ
    
    elif root.val > v:
        # If the current node's value is greater than v,
        # the next highest value must be in the left subtree,
        # so update succ to the current node and recurse on the left subtree
        return find_next(root.left, v, root)
    
    else:
        # If the current node's value is less than v,
        # there may still be a larger value in the right subtree,
        # so just recurse on the right subtree
        return find_next(root.right, v, succ)

def find_min(root):
    # Helper function to find the minimum value in a BST
    if not root.left:
        return root
    return find_min(root.left)
```

The find_next function takes in the root of the binary search tree, the value v to find the next highest value for, and an optional successor node that is initially None. It recursively searches the binary search tree based on the value of the input variable v. 

The base condition is if the root is None, which means we have reached the end of a subtree without finding a higher value. In this case, we return the successor node, which will be None if no higher value was found.

The next condition checks if the current node's value is equal to v. If it is, we check if the current node has a right child. If it does, we need to find the minimum value in the right subtree, as that will be the next highest value. We use the helper function find_min to find the minimum value in the right subtree and return it as the successor.

If the current node's value is greater than v, we update the successor node to the current node and recurse on the left subtree. This is because the next highest value must be in the left subtree.

If the current node's value is less than v, we don't update the successor node and just recurse on the right subtree. This is because there may still be a larger value in the right subtree.

Finally, we need a helper function find_min to find the minimum value in a subtree. It simply traverses the left subtree until it reaches a leaf node and returns that node as the minimum value.

 tokens:530