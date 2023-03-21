'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # base conditions

    # if both p and q are empty then both are same
    if not p and not q:
        return True
    
    # if one of them is empty then they are different
    if not p or not q:
        return False
    
    # if the values are different then they are different
    if p.val != q.val:
        return False
    
    # return True only if both left and right subtrees are equal
    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))