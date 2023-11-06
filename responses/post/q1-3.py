To solve this problem, we can use an iterative approach instead of a recursive one. 

The idea is to start traversing the tree from the root node. If the current node value is greater than the given value v, we update the succ variable to store the current node value and move to the left subtree. Otherwise, we move to the right subtree.

Here is the updated implementation of the find_next function:

def find_next(root, v, succ=None):
    curr = root
    while curr:
        if curr.val > v:
            succ = curr.val
            curr = curr.left
        else:
            curr = curr.right
    return succ

With this implementation, if there is a smaller element in the tree that is larger than v, it will be stored in the succ variable during the traversal. If there is no such element, succ will be None as initialized.

The time complexity of this algorithm is O(h), where h is the height of the tree. In the worst case, the tree can be skewed, resulting in a time complexity of O(n), where n is the number of nodes in the tree.

 tokens:229