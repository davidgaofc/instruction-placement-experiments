Here is the implementation of the `find_next` function to find the minimal element exceeding the specified value `v` in the binary search tree:

```python
class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def insert(root, v):
    if not root:
        return Node(v)
    if v < root.val:
        root.left = insert(root.left, v)
    else:
        root.right = insert(root.right, v)
    return root

def find_min(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node

def find_next(root, v, succ=None):
    if root is None:
        return None
    
    if root.val == v:
        if root.right:
            return find_min(root.right)
        else:
            return succ
    
    if root.val > v:
        succ = root
        return find_next(root.left, v, succ)
    
    return find_next(root.right, v, succ)

def build_tree(arr):
    r = None
    for x in arr:
        r = insert(r, x)
    return r
```

In the `find_next` function, we perform a recursive search in the binary search tree starting from the root node. 
- In each recursive call, we compare the current node's value with the target value `v`. 
- If the current node value is equal to `v`, we check if the right subtree exists. If it does, we find the minimum value in the right subtree using the `find_min` function. Otherwise, we return the successor node which is the node passed as `succ` (initially set to `None`). 
- If the current node value is greater than `v`, we update the `succ` variable to the current node and recursively search in the left subtree. 
- If the current node value is less than `v`, we continue searching in the right subtree. 
- Finally, if we reach a leaf node without finding the value `v` or a greater value, we return `None`.

You can use the `build_tree` function to create a binary search tree from an array of values, and then call the `find_next` function to find the minimal element exceeding a specified value `v`.

 tokens:495