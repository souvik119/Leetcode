'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
'''

# recursive dfs
# cannot just check immediate children also make sure overall comparison is okay
# -infinity and infinity as boundary and keep updating left, right boundary respectively
# O(n)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_ValidBST(root):

    # actual node for comparison and left, right boundaries
    def valid(node, left, right):
        if not node:
            # True because empty BST is still BST
            return True
        
        if not (node.val < right and node.val > left):
            return False
        
        # going to left subtree keep left boundary same and update right boundary
        # going to left subtree keep right boundary same and update left boundary
        return (valid(node.left, left, node.val) and
        valid(node.right, node.val, right))
    
    # intitial boundaries 
    return valid(root, float('-inf'), float('inf'))

